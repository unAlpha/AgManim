#!/usr/bin/env python
# from manimlib.imports import *
from Ag.Grid import *


class ShowPassingFlashAroundExample(Scene):
    def construct(self):
        mobjects = VGroup(
                Circle(),
                Circle(fill_opacity=1),
                TextMobject("Text").scale(2)
            )
        mobjects.scale(1.5)
        mobjects.arrange_submobjects(RIGHT,buff=2)

        self.add(mobjects)

        self.play(
            *[ShowPassingFlashAround(mob) for mob in mobjects]
        )
        self.play(
            *[ShowCreationThenDestructionAround(mob) for mob in mobjects]
        )
        self.play(
            *[ShowCreationThenFadeAround(mob) for mob in mobjects]
        )
        self.play(
            *[ApplyWave(mob) for mob in mobjects]
        )
        self.play(
            *[WiggleOutThenIn(mob) for mob in mobjects]
        )
        self.play(
            *[TurnInsideOut(mob) for mob in mobjects]
        )

        self.wait()


class CircleIndicateExample(Scene):
    def construct(self):
        mobjects = VGroup(
            Dot(),
            TexMobject("x")
        ).scale(2)
        mobjects.arrange_submobjects(RIGHT,buff=2)

        self.add(mobjects)
        self.wait(0.2)

        for obj in mobjects:
            self.play(CircleIndicate(obj))


class FlashExample(Scene):
    def construct(self):
        mobjects = VGroup(
            Dot(),
            TexMobject("x")
        ).scale(2)
        mobjects.arrange_submobjects(RIGHT,buff=2)

        mobject_or_coord = [
            *mobjects,                    # Mobjects: Dot and "x"
            mobjects.get_right()+RIGHT*2  # Coord
        ]

        colors=[GRAY,RED,BLUE]

        self.add(mobjects)

        for obj,color in zip(mobject_or_coord,colors):
            self.play(Flash(obj,color=color,flash_radius=0.5))

        self.wait(0.3)


class IndicateExample(Scene):
    def construct(self):
        #                     0    1   2
        formula = TexMobject("f(","x",")")
        dot = Dot()

        VGroup(formula,dot)\
                           .scale(3)\
                           .arrange_submobjects(DOWN,buff=3)

        self.add(formula,dot)

        for mob in [formula[1],dot]:
            self.play(Indicate(mob))

        self.wait(0.3)


class FocusOnExample(Scene):
    def construct(self):
        mobjects = VGroup(
            Dot(),
            TexMobject("x")
        )
        mobjects.arrange_submobjects(RIGHT,buff=2)

        mobject_or_coord = [
            *mobjects,                    # Mobjects: Dot and "x"
            mobjects.get_right()+RIGHT*2  # Coord
        ]

        colors=[GRAY,RED,BLUE]

        self.add(mobjects)

        for obj,color in zip(mobject_or_coord,colors):
            self.play(FocusOn(obj,color=color))

        self.wait(0.3)


class ShrinkToCenterExample(Scene):
    def construct(self):
        mobjects = VGroup(
                Square(),
                RegularPolygon(fill_opacity=1),
                TextMobject("Text").scale(2)
            )
        mobjects.scale(1.5)
        mobjects.arrange_submobjects(RIGHT,buff=2)

        self.play(
            *[ShrinkToCenter(mob) for mob in mobjects]
        )

        self.wait()


class SpinInFromNothingExample(Scene):
    def construct(self):
        mobjects = VGroup(
                Square(),
                RegularPolygon(fill_opacity=1),
                TextMobject("Text").scale(2)
            )
        mobjects.scale(1.5)
        mobjects.arrange_submobjects(RIGHT,buff=2)

        self.play(
            *[SpinInFromNothing(mob,path_arc=PI/2) for mob in mobjects]
        )

        self.wait()


class GrowFromEdgeExample(Scene):
    def construct(self):
        mobjects = VGroup(
                Circle(),
                Circle(fill_opacity=1),
                TextMobject("Text").scale(2)
            )
        mobjects.arrange_submobjects(RIGHT,buff=2)

        directions=[UP,LEFT,DOWN,RIGHT]

        for direction in directions:
            self.play(
                *[GrowFromEdge(mob,direction) for mob in mobjects]
            )

        self.wait()


class GrowFromPointExample(Scene):
    def construct(self):
        mobjects = VGroup(
                Circle(),
                Circle(fill_opacity=1),
                TextMobject("Text").scale(2)
            )
        mobjects.arrange_submobjects(RIGHT,buff=2)

        directions=[UP,LEFT,DOWN,RIGHT]

        for direction in directions:
            self.play(
                *[GrowFromPoint(mob,mob.get_center()+direction*3) for mob in mobjects]
            )

        self.wait()


class FadeInFromLargeExample(Scene):
    def construct(self):
        mobjects = VGroup(
                Circle(),
                Circle(fill_opacity=1),
                TextMobject("Text").scale(2)
            )
        mobjects.scale(1.5)
        mobjects.arrange_submobjects(RIGHT,buff=2)

        scale_factors=[0.3,0.8,1,1.3,1.8]

        for scale_factor in scale_factors:
            t_scale_factor = TextMobject(f"\\tt scale\\_factor = {scale_factor}")
            t_scale_factor.to_edge(UP)

            self.add(t_scale_factor)
            # 对于for，play(*[])每次播放一个
            self.play(
                *[FadeInFromLarge(mob,scale_factor) for mob in mobjects]
            )

            self.remove(t_scale_factor)

        self.wait(0.3)


class FadeOutAndShiftExample(Scene):
    def construct(self):
        mobjects = VGroup(
                Circle(),
                Circle(fill_opacity=1),
                TextMobject("Text").scale(2)
            )
        mobjects.scale(1.5)
        mobjects.arrange_submobjects(RIGHT,buff=2)

        directions=[UP,LEFT,DOWN,RIGHT]

        self.add(mobjects)
        self.wait(0.3)

        for direction in directions:
            self.play(
                *[FadeOutAndShift(mob,direction) for mob in mobjects]
            )

        self.wait()


class FadeInFromExample(Scene):
    def construct(self):
        mobjects = VGroup(
                Circle(),
                Circle(fill_opacity=1),
                TextMobject("Text").scale(2)
            )
        mobjects.scale(1.5)
        mobjects.arrange_submobjects(RIGHT,buff=2)

        directions=[UP,LEFT,DOWN,RIGHT]

        for direction in directions:
            self.play(
                *[FadeInFrom(mob,direction) for mob in mobjects]
            )

        self.wait()


class UncreateExample(Scene):
    def construct(self):
        mobjects = VGroup(
                Circle(),
                Circle(fill_opacity=1),
                TextMobject("Text").scale(2)
            )
        mobjects.scale(1.5)
        mobjects.arrange_submobjects(RIGHT,buff=2)

        self.add(mobjects)

        self.wait(0.3)

        self.play(
            *[Uncreate(mob) for mob in mobjects]
        )

        self.wait()

class CoordScreen(Scene):
    def construct(self):
        screen_grid = ScreenGrid()
        self.add(screen_grid)

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(ShowCreation(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))


class HelloWorld(Scene):
    def construct(self):
        helloWorld = TexMobject("Hello World!", color=RED)

        rectangle = Rectangle(color=BLUE)
        rectangle.surround(helloWorld)

        group_HW_RCT = VGroup(helloWorld, rectangle)

        yesManim = TexMobject("Hello Manim", color=BLUE)
        yesManim.scale(2.5)

        self.play(Write(helloWorld))
        self.wait(1)
        self.play(FadeIn(rectangle))
        self.wait(1)
        self.play(ApplyMethod(group_HW_RCT.scale, 2.5))
        self.wait(1)
        self.play(Transform(helloWorld, yesManim))
        self.wait(1)


class UpdatersExample(Scene):
    def construct(self):
        decimal = DecimalNumber(
            0,
            #显示省略号
            show_ellipsis=True,
            #小数位数
            num_decimal_places=3,
            #包括符号
            include_sign=True,
        )
        square = Square().to_edge(UP)

        decimal.add_updater(lambda d: d.next_to(square, RIGHT))
        decimal.add_updater(lambda d: d.set_value(square.get_center()[1]))
        
        self.add(square, decimal)
        self.play(
            square.to_edge, DOWN,
            rate_func=there_and_back,
            run_time=5,
        )
        self.wait()


class BasicShapes(Scene):
    def construct(self):
        #make object
        annulus1 = Annulus(inner_radius=.4, outer_radius=1, color=BLUE)
        square1 = Square(color=ORANGE, fill_color=ORANGE, fill_opacity=.5)
        rect1 = Rectangle(height=3.2,width=1.2,color=PINK, fill_color=PINK, fill_opacity=0.5)

        line1 = Line(np.array([0,3.6,0]),np.array([0,2,0]),color=BLUE)
        line2 = Line(np.array([-0.98,2,0]),np.array([-1,-1,0]),color=BLUE)
        line3 = Line(np.array([0.98,2,0]),np.array([1,0.5,0]),color=BLUE)

        #position
        annulus1.shift(UP*2)
        square1.shift(LEFT+DOWN*2)
        rect1.shift(RIGHT+DOWN*(3.2/2-0.5))

        #Showing object
        self.add(line1)
        self.play(GrowFromCenter(annulus1))
        self.wait(0.5)
        self.play(FadeIn(line2),FadeIn(line3))
        self.wait(0.5)
        self.play(FadeInFromDown(square1))
        self.play(FadeInFromDown(rect1))
        self.wait()


class Shoot(Scene):
    def construct(self):
        #make aim_scope
        circle1 = Circle(color=BLUE)
        circle2 = Circle(color=RED, fill_color=RED, fill_opacity=1)
        circle2.scale(0.1)
        line1 = Line(np.array([-1,0,0]),np.array([1,0,0]),color=RED)
        line2 = Line(np.array([0,1,0]),np.array([0,-1,0]),color=RED)
        aim_scope = VGroup(circle1,circle2,line1,line2)

        #make target
        target_list = []
        for i in range(3):
            for j in range(5):
                target_ij = Circle(color=YELLOW, fill_color=YELLOW, fill_opacity=0.4)
                target_ij.scale(0.4)
                target_ij.shift(np.array([-4+j*2,-2+i*2,0]))
                self.play(FadeIn(target_ij),run_time=0.2)
                target_list.append(target_ij)
        self.wait(1)

        #move&shoot animation
        def shoot_ij(i,j):
            target_ij=target_list[j+i*5]
            self.play(ApplyMethod(aim_scope.next_to, target_ij, 0))
            self.play(ApplyMethod(target_ij.set_fill, GREY), ApplyMethod(target_ij.set_color, GREY))
            ij = TexMobject("(%d,%d)" % (i,j),color=GREY)
            ij.next_to(target_ij, DOWN)
            self.play(Write(ij))
            self.wait(1)
            return 0
        
        self.add(aim_scope)
        self.play(ApplyMethod(aim_scope.shift, DOWN*3+LEFT*6.1))
        shoot_ij(0,1)
        shoot_ij(2,0)
        shoot_ij(1,3)
        shoot_ij(0,0)
        shoot_ij(2,4)


class LoveDeathAndRobots(Scene):
    def construct(self):
        #make object
        circle1 = Circle(color=RED, fill_color=RED,fill_opacity=0.5)
        circle2 = Circle(color=RED, fill_color=RED,fill_opacity=0.5)
        square1 = Square(color=RED, fill_color=RED,fill_opacity=0.5)
        loveShape = VGroup(circle1, circle2,square1)

        rect1 = Rectangle(height=0.8, width=4, color=RED, fill_color=RED,fill_opacity=0.5)
        rect2 = Rectangle(height=0.8, width=4, color=RED, fill_color=RED,fill_opacity=0.5)
        death = VGroup(rect1, rect2)

        square2 = Square(color=RED, fill_color=RED,fill_opacity=0.5)
        square2.scale(1.6)
        c1 = Circle(color=RED, fill_color=BLACK,fill_opacity=0.5)
        c2 = Circle(color=RED, fill_color=BLACK,fill_opacity=0.5)
        c1.scale(0.45)
        c2.scale(0.45)
        robots = VGroup(square2, c1, c2)

        line1 = Line(np.array([-6,-2.4,0]), np.array([6,-2.4,0]), color=RED)
        line1.set_height(0.2)

        text1 = TextMobject("LOVE\nDEATH\n+\nROBOTS", color=RED)
        text1.scale(1.8)

        groupShape = VGroup(loveShape, death, robots)
        groupAll = VGroup(loveShape, death, robots, line1, text1)

        #position
        circle1.shift((UP+LEFT)*np.sqrt(2)/2)
        circle2.shift((UP+RIGHT)*np.sqrt(2)/2)
        square1.rotate(np.pi/4)

        rect1.rotate(np.pi/4)
        rect2.rotate(-np.pi/4)

        c1.shift(np.array([-0.72,0.6,0]))
        c2.shift(np.array([0.72,0.6,0]))
        robots.shift(RIGHT*4)

        text1.shift(DOWN*2.5)

        self.play(ShowCreation(circle1),ShowCreation(circle2),ShowCreation(square1))
        self.wait(1)
        self.play(ApplyMethod(loveShape.shift, LEFT*4))
        self.wait(1)

        self.play(ShowCreation(rect1),ShowCreation(rect2))
        self.wait(1)

        self.play(ShowCreation(square2))
        self.play(ShowCreation(c1),ShowCreation(c2))
        self.wait(1)

        self.play(ApplyMethod(groupShape.set_opacity,1))
        self.wait(1)

        self.play(ShowCreation(line1))
        self.wait(1)
        self.play(Transform(line1,text1))
        self.wait(1)
        self.play(ApplyMethod(groupAll.shift, UP*0.5))
        self.wait(1)
        

class TextLuXun(Scene):
    def construct(self):
        quote1 = TextMobject("使用Manim制作数学动画很有意思")
        quote1.set_color(RED)
        quote1.to_edge(UP)
        quote2 = TextMobject("Making animation by manim is funny.")
        quote2.set_color(BLUE)
        author = TextMobject("-鲁迅", color=PINK)

        author.next_to(quote1.get_corner(DOWN+RIGHT),DOWN)

        self.add(quote1)
        self.add(author)
        self.wait(2)
        self.play(Transform(quote1,quote2),ApplyMethod(author.move_to,quote2.get_corner(DOWN+RIGHT)+DOWN))

        self.play(ApplyMethod(author.scale,1.5))
        self.wait(1)
        author.match_color(quote2)
        self.wait(1)
        self.play(FadeOut(quote1),FadeOut(author))
        self.wait()
        

class LabelShape(Scene):
    def construct(self):
        #side_length 边长
        square1 = Square(side_length=5, fill_color=BLUE, fill_opacity=0.5)

        label1 = TextMobject("扭一下身体")
        label1.bg = BackgroundRectangle(label1, fill_opacity=1)
        #VGroup的参数顺序就是前后的叠层顺序
        label1_group = VGroup(label1.bg, label1)
        label1_group.rotate(TAU/8)

        label2 = TextMobject("加个边框", color=BLACK)
        label2.bg = SurroundingRectangle(label2, color=BLUE, fill_color=RED, fill_opacity=1)
        label2_group = VGroup(label2.bg, label2)
        label2_group.next_to(label1_group,DOWN)

        label3 = TextMobject("变成彩虹")
        label3.set_color_by_gradient(RED, ORANGE, YELLOW, BLUE, PURPLE)
        label3.to_edge(DOWN)

        self.add(square1)
        self.play(FadeIn(label1_group))
        self.play(FadeIn(label2_group))
        self.play(FadeIn(label3))
        self.wait(1)


class LatexTmp(Scene):
    def construct(self):
        title = TextMobject("This is some \\LaTeX")
        basel = TexMobject(
            "\\sum_{n=1}^\\infty "
            "\\frac{1}{n^2} = \\frac{\\pi^2}{6}"
        )
        #使basel在title下面
        VGroup(title, basel).arrange(DOWN)
        self.play(
            Write(title),
            FadeInFrom(basel, UP)
        )
        self.wait()


class NaturalNumberCube(Scene):
    def construct(self):
        equal = TextMobject("=", color=RED)
        eq_left1 = TextMobject("$1^3+2^3+3^3+\\dots+n^3$", color = GREEN)
        eq_right1= TextMobject("$(1+2+3+\\dots+n)^2$", color=YELLOW)

        eq_left2 = TextMobject("$\\Sigma_{i=1}^{n} i^{3}$", color=GREEN)
        eq_right2= TextMobject("$(\\Sigma_{i=1}^{n} i)^{2}$", color=YELLOW)
        equation2= VGroup(equal,eq_left2,eq_right2)

        eq_left1.next_to(equal,LEFT)
        eq_right1.next_to(equal,RIGHT)
        eq_left2.next_to(equal,LEFT)
        eq_right2.next_to(equal,RIGHT)

        self.play(FadeIn(equal),FadeIn(eq_left1),FadeIn(eq_right1))
        self.wait(1)
        self.play(ReplacementTransform(eq_left1,eq_left2))
        self.play(ReplacementTransform(eq_right1,eq_right2))
        self.wait(1)
        self.play(ApplyMethod(equation2.scale,2.0))
        self.wait(1)


class PlotFunc(GraphScene):
    CONFIG = {
        "x_min" : -10,
        "x_max" : 10.3,
        "y_min" : -1.5,
        "y_max" : 1.5,
        "graph_origin" : ORIGIN,
        "function_color" : RED,
        "axes_color" : GREEN,
        "x_labeled_unms" : range(-10,12,2)
    }
    def construct(self):
        self.setup_axes(animate=True)
        #获得图线
        func_cos_graph = self.get_graph(self.func_cos, self.function_color)
        func_sin_graph = self.get_graph(self.func_sin)
        #设置垂线
        vert_line = self.get_vertical_line_to_graph(TAU, func_cos_graph, color=YELLOW)
        #设置标签
        cos_label = self.get_graph_label(func_cos_graph, label="\\cos(x)")
        sin_label = self.get_graph_label(func_sin_graph, label="\\sin(x)", x_val=-10, direction=UP/2)

        twoPI = TexMobject("x=2\\pi")

        #获得坐标点的位置
        label_Coord = self.input_to_graph_point(TAU,func_cos_graph)
        twoPI.shift(label_Coord, UP/3)

        self.play(ShowCreation(func_cos_graph), ShowCreation(func_sin_graph))
        self.play(ShowCreation(vert_line),
                ShowCreation(cos_label),
                ShowCreation(sin_label),
                ShowCreation(twoPI)
        )

    def func_cos(self, x):
        return np.cos(x)
    def func_sin(self, x):
        return np.sin(x)


class SunAndPlanet(ThreeDScene):
    def construct(self):
        rSun = 1.6
        rPlanet = 0.4
        rOrb = 3.5
        sun = Sphere(radius=rSun)
        planet = Sphere(radius=rPlanet)
        orbit = Circle(radius=rOrb)
        planet.shift(UP*rOrb)
        system = VGroup(sun, orbit, planet)
        system.shift(DOWN*2+LEFT*1.2)

        FVector = Vector(np.array([0,rSun-rOrb,0]), color=YELLOW)
        FVector.next_to(planet, DOWN*0.6)
        FFomula = TexMobject("\\vec{F}=G m_1 m_2\\frac{(\\vec{r_1}-\\vec{r_2})}{r^3}", color=RED)
        FFomula.rotate_about_origin(PI/2)
        FFomula.next_to(FVector,LEFT*0.4)

        self.set_camera_orientation(phi=10)
        self.play(ShowCreation(orbit))
        self.play(FadeIn(planet), FadeIn(sun))
        self.wait(1)
        self.play(ShowCreation(FVector))
        self.play(Write(FFomula))
        self.wait(1)


class ShowPicture(Scene):
        CONFIG = {
            'pic1' : 'assets\\pic\\pic1.png',
            'facebook' : 'assets\\pic\\Facebook.png',
            'power' : 'assets\\pic\\Power.png'
        }
        def construct(self):
            pic1 = ImageMobject(self.pic1)
            pic1.set_height(1)
            facebook = ImageMobject(self.facebook)
            facebook.set_height(1)
            power = ImageMobject(self.power)
            power.set_height(1)

            facebook.shift(UP*0.6)
            pic1.next_to(facebook, LEFT)
            power.next_to(facebook, RIGHT)

            invokerText = TextMobject("I N V O K E R")
            invokerText.set_width(3.2)
            invokerText.next_to(facebook, DOWN)

            self.play(FadeInFromLarge(pic1), run_time=1.5)
            self.play(FadeInFromLarge(facebook), run_time=1.5)
            self.play(FadeInFromLarge(power), run_time=1.5)

            self.play(Write(invokerText), run_time=1.5)
            self.wait(1)

