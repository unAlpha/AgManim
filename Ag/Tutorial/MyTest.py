from manimlib.imports import *

class WriteGeneralFormula(GeneralExample):
    CONFIG = {
        "plane_center" : 2*RIGHT,
        "x_label_range" : [],
        "y_label_range" : [],
        "unit_size" : 0.7,
        "number" : complex(2, 1),
    }
    def construct(self):
        self.add_plane()
        self.show_squaring()
        self.expand_square()
        self.draw_triangle()
        self.show_uv_to_triples()

    def show_squaring(self):
        self.force_skipping()
        self.square_point()
        dot = self.example_dot
        old_label = self.example_label
        line = self.example_line
        square_dot = self.square_dot
        old_square_label = self.square_label
        square_line = self.square_line
        z_to_z_squared = self.z_to_z_squared
        arrow = self.z_to_z_squared_arrow
        result_length_label = self.result_length_label
        self.clear()
        self.add(self.plane, self.plane.coordinate_labels)
        self.revert_to_original_skipping_status()

        label = TexMobject("u+vi")
        label.move_to(old_label, LEFT)
        label.add_background_rectangle()
        square_label = TexMobject("(u+vi)^2")
        square_label.move_to(old_square_label, LEFT)
        square_label.add_background_rectangle()

        self.add(label, dot, line)
        self.play(
            ShowCreation(arrow),
            FadeIn(z_to_z_squared)
        )
        self.play(*[
            ReplacementTransform(
                start.copy(), target,
                run_time = 1.5,
                path_arc = np.pi/2
            )
            for start, target in [
                (dot, square_dot),
                (line, square_line),
                (label, square_label),
            ]
        ])

        self.example_label = label
        self.square_label = square_label

    def expand_square(self):
        rect = Rectangle(
            height = 2.5, width = 7,
            stroke_width = 0,
            fill_color = BLACK,
            fill_opacity = 0.8,
        )
        rect.to_corner(UP+LEFT, buff = 0)
        top_line = TexMobject("(u+vi)(u+vi)")
        for i in 1, 7:
            top_line[0][i].set_color(U_COLOR)
            top_line[0][i+2].set_color(V_COLOR)
        top_line.next_to(rect.get_top(), DOWN)
        second_line = TexMobject(
            "\\big(", "u^2 - v^2", "\\big)", "+",
            "\\big(", "2uv", "\\big)", "i"
        )
        for i, j in (1, 0), (5, 1):
            second_line[i][j].set_color(U_COLOR)
        for i, j in (1, 3), (5, 2):
            second_line[i][j].set_color(V_COLOR)
        second_line.next_to(top_line, DOWN, MED_LARGE_BUFF)
        real_part = second_line[1]
        imag_part = second_line[5]
        for part in real_part, imag_part:
            part.add_to_back(BackgroundRectangle(part))

        z = self.number**2
        square_point = self.plane.number_to_point(z)
        zero_point = self.plane.number_to_point(0)
        real_part_point = self.plane.number_to_point(z.real)
        real_part_line = Line(zero_point, real_part_point)
        imag_part_line = Line(real_part_point, square_point)
        for line in real_part_line, imag_part_line:
            line.set_color(self.square_color)


        self.play(*list(map(FadeIn, [rect, top_line, second_line])))
        self.wait()
        self.play(
            real_part.copy().next_to, real_part_line.copy(), 
                DOWN, SMALL_BUFF,
            ShowCreation(real_part_line)
        )
        self.wait()
        self.play(
            FadeOut(VGroup(
                self.example_label, self.example_dot, self.example_line,
                self.z_to_z_squared, self.z_to_z_squared_arrow
            )),
            imag_part.copy().next_to, imag_part_line.copy(), 
                RIGHT, SMALL_BUFF,
            ShowCreation(imag_part_line)
        )
        self.wait()

        self.corner_rect = rect

    def draw_triangle(self):
        hyp_length = TexMobject("u", "^2", "+", "v", "^2")
        hyp_length.set_color_by_tex("u", U_COLOR)
        hyp_length.set_color_by_tex("v", V_COLOR)
        hyp_length.add_background_rectangle()
        line = self.square_line
        hyp_length.next_to(line.get_center(), UP, SMALL_BUFF)
        hyp_length.rotate(
            line.get_angle(),
            about_point = line.get_center()
        )
        triangle = Polygon(
            ORIGIN, RIGHT, RIGHT+UP,
            stroke_width = 0,
            fill_color = MAROON_B,
            fill_opacity = 0.5,
        )
        triangle.replace(line, stretch = True)

        self.play(Write(hyp_length))
        self.wait()
        self.play(FadeIn(triangle))
        self.wait()

    def show_uv_to_triples(self):
        rect = self.corner_rect.copy()
        rect.stretch_to_fit_height(FRAME_HEIGHT)
        rect.move_to(self.corner_rect.get_bottom(), UP)

        h_line = Line(rect.get_left(), rect.get_right())
        h_line.next_to(rect.get_top(), DOWN, LARGE_BUFF)
        v_line = Line(rect.get_top(), rect.get_bottom())
        v_line.shift(1.3*LEFT)
        uv_title = TexMobject("(u, v)")
        triple_title = TexMobject("(u^2 - v^2, 2uv, u^2 + v^2)")
        uv_title.scale(0.75)
        triple_title.scale(0.75)
        uv_title.next_to(
            h_line.point_from_proportion(1./6), 
            UP, SMALL_BUFF
        )
        triple_title.next_to(
            h_line.point_from_proportion(2./3),
            UP, SMALL_BUFF
        )

        pairs = [(2, 1), (3, 2), (4, 1), (4, 3), (5, 2), (5, 4)]
        pair_mobs = VGroup()
        triple_mobs = VGroup()
        for u, v in pairs:
            a, b, c = u**2 - v**2, 2*u*v, u**2 + v**2
            pair_mob = TexMobject("(", str(u), ",", str(v), ")")
            pair_mob.set_color_by_tex(str(u), U_COLOR)
            pair_mob.set_color_by_tex(str(v), V_COLOR)
            triple_mob = TexMobject("(%d, %d, %d)"%(a, b, c))
            pair_mobs.add(pair_mob)
            triple_mobs.add(triple_mob)
            pair_mob.scale(0.75)
            triple_mob.scale(0.75)
        pair_mobs.arrange(DOWN)
        pair_mobs.next_to(uv_title, DOWN, MED_LARGE_BUFF)
        triple_mobs.arrange(DOWN)
        triple_mobs.next_to(triple_title, DOWN, MED_LARGE_BUFF)

        self.play(*list(map(FadeIn, [
            rect, h_line, v_line, 
            uv_title, triple_title
        ])))
        self.play(*[
            LaggedStartMap(
                FadeIn, mob, 
                run_time = 5,
                lag_ratio = 0.2
            )
            for mob in (pair_mobs, triple_mobs)
        ])