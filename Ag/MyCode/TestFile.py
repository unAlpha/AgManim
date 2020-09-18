from manimlib.imports import *
import fractions

class TestVMobject(Scene):
    def construct(self):
        ployObj1 = VMobject()
        ployObj2 = VMobject()
        ployObj3 = VMobject()
        ployObj4 = VMobject()
        ployObj1.set_points([DOWN,LEFT,RIGHT,DOWN])
        ployObj2.set_points_as_corners([DOWN,LEFT,RIGHT,DOWN])
        ployObj3.set_anchors_and_handles(DOWN,LEFT,LEFT,RIGHT)
        ployObj4.set_points_as_corners(ployObj3.points).to_edge(UP)

        ployObj5=Arrow()

        # print(ployObj1.points)
        # print("-------------------------")
        # print(ployObj2.points)
        # print("-------------------------")
        # print(ployObj3.points)
        # print("-------------------------")
        # print(ployObj4.points)
        print("-------------------------------")
        print(ployObj5.family_members_with_points(),"ployObj5")
        print(ployObj5.submobjects,"ployObj5")

        self.add(
            # ployObj1,
            # ployObj2,
            # ployObj3,
            # ployObj4,
            ployObj5
        )

class funcReplaceTest(Scene):
    def construct(self):
        line = Line(UL,DR).to_edge(UP)
        triangle = Circle()
        triangle.replace(line, dim_to_match=0, stretch = True)
        self.add(line,triangle)
        self.wait()

class VGroupTransfrom(Scene):
    def construct(self):
        txt_list = [Text(str(txtn)) for txtn in range(99,102)]
        txt_vgroup = VGroup(*txt_list).arrange(DOWN, buff= MED_LARGE_BUFF)
        
        def vgroup_transform_to_part(vgroup):
            vgroup[1].scale(2)
            vgroup.arrange(DOWN, buff=MED_LARGE_BUFF*1.2)
            return vgroup

        self.add(txt_vgroup)
        # # 方法1 不太可行
        # self.play(       
        #     txt_vgroup.arrange, DOWN, {"buff" : LARGE_BUFF},
        #     txt_vgroup[1].scale, 2,
        # )
        # 方法2 可行的
        self.play(
            ApplyFunction(vgroup_transform_to_part,txt_vgroup)
        )

        self.wait()

class testTransform(Scene):
    def construct(self):
        dot = Dot()
        self.add(dot)
        self.play(
            dot.shift,UP,
            Transform(self.myLine(ORIGIN),self.myLine(UP))
        )
        self.wait()

    def myLine(self,direction):
        ployObj = VMobject()
        return ployObj.set_points_as_corners([DOWN,LEFT,direction])

class MyThreeDScene(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
                y_min = -3.6,
                y_max = 3.6,
                x_axis_config= {
                    "include_numbers" : True,
                    "exclude_zero_from_default_numbers":False,
                    },
                y_axis_config= {
                    "include_numbers" : True,
                    "label_direction" : DOWN
                    },
                z_axis_config= {
                    "include_numbers" : True,
                    }
            )

        cube=Cube()

        axes.add_label_xyzStr()
        sqr = Square(side_length=2.5)
        sqr.rotate(PI/2,X_AXIS,about_point=ORIGIN).set_color(BLUE)
        axes.x_axis.numbers.set_color(RED)
        axes.z_axis.rotate(PI,about_point=ORIGIN)        
        
        self.play(
                *list(map(ShowCreation,[axes.x_axis,axes.y_axis]))
            )
        
        self.move_camera(phi=60*DEGREES,theta=-45*DEGREES,run_time=3)
        self.play(ShowCreation(axes.z_axis))
        self.wait()
        self.play(ShowCreation(sqr))
        
        self.play(FadeIn(cube))
        self.wait()

class Equation(Scene):
    def construct(self):
        equation1 = TexMobject("a", "^2", "+", "b", "^2", "=", "c", "^2")
        equation2 = TexMobject("aa", "^2", "+", "bb", "^2", "=", "cc", "^2")
        equation3 = TexMobject("A", "^2", "+", "bB", "^2", "=", "CcCCC", "^2")
        # list对象
        equation = VGroup(equation1,equation2,equation3).arrange(DOWN)
        equation1.next_to(equation3, DOWN, MED_LARGE_BUFF)
        # equation1.shift_onto_screen(buff=5)
        # equation1.center()
        self.add(equation)
        self.play(equation1.shift_onto_screen,{"buff":5})
        self.wait()

class FuncGraphSin(Scene):
    CONFIG={
        "amp": 2.3,
        "sine_graph_config":{
            "x_min": -TAU/2,
            "x_max": TAU/2,
            "color": RED,
            },
    }
    def construct(self):
        sinGraph = self.get_sin_graph(0)
        sinGraph.scale(0.5)
        self.add(sinGraph)
        self.wait()

    def get_sin_graph(self, dx):
        sin_graph = FunctionGraph(
                lambda x: self.amp * np.sin(x - dx),
                **self.sine_graph_config
                )
        return sin_graph

class SumTyping(Scene):
    def construct(self):
        # text1 = Text("D 这是一个测试")
        # Add animation Typing (unfinished)\
        # https://github.com/xy-23/manim/commit/f4d45d13017e3c061fce4a0fd907e4247626ccda
        # self.play(Typing(text1),run_time=1)

        text1 = Text("第一段文字")
        always_shift(text1, rate=0.5)
        self.add(text1)
        self.wait(2)

class vectors(GraphScene):
    CONFIG ={
        "x_min" : -1,
        "x_max" : 10,
        "y_min" : -1,
        "y_max" : 10,
        "x_axis_label" : "实数",
        "y_axis_label" : "虚数",
    }
    def construct(self):
        self.setup_axes()
        
        self.x_axis.add_numbers(*[i for i in range(1,10,2)])
        self.y_axis.add_numbers(*[i for i in range(-0,10,2)])
        # 1 创建对象
        vector1 = self.vector(1,1,5,5,True)
        # 2 变化的量
        vlu = ValueTracker(5)
        # 3 add_updater
        vector1.add_updater(lambda obj: obj.become(self.vector(1,1,5,vlu.get_value(),True)))

        dashV = self.dashVector(1,1,6,2)

        # 4 show
        self.play(ShowCreation(vector1))
        # 5 add
        self.add(vector1)
        # 6 change
        self.play(vlu.increment_value,1)
        # 7 change again
        self.play(vlu.increment_value,-2)
        self.play(ShowCreation(dashV))
        self.wait()
    # 0 定义对象
    def vector(self,x1=0,y1=0,x2=1,y2=1,texNeed=False):
        arr = Arrow(self.coords_to_point(x1,y1),self.coords_to_point(x2,y2),buff=0)
        tex = TexMobject("(%.1f,%.1f)"%(x2,y2))
        tex.next_to(arr.end,UP+RIGHT,buff=SMALL_BUFF)
        if texNeed:
            return VGroup(arr,tex)
        else:
            return arr

    def dashVector(self,x1=0,y1=0,x2=1,y2=1,texNeed=False):
        arr = DashedLine(
            self.coords_to_point(x1,y1),self.coords_to_point(x2,y2),
            buff=0,
            dash_length=5*DEFAULT_DASH_LENGTH,
            stroke_width=6
            )
        arr.add_tip()
        tex = TexMobject("(%.1f,%.1f)"%(x2,y2))
        tex.next_to(arr.end,UP+RIGHT,buff=SMALL_BUFF)
        if texNeed:
            return VGroup(arr,tex)
        else:
            return arr

class ep1011(Scene):
    def construct(self):
        def fsin(dx=1):
            return FunctionGraph(lambda x: np.sin(x-dx),x_min=-TAU/2-1.5,x_max=TAU/2+1).set_color(RED)
        def fcos(dx=1):
            return FunctionGraph(lambda x: np.cos(x-dx),x_min=-TAU/2-1.5,x_max=TAU/2+1).set_color(YELLOW)

        gsin = fsin()
        gcos = fcos()
        axes=Axes(x_min=-5,x_max=5.5,y_min=-2, y_max=2)

        text1 = Text("功率=电压x电流",size=0.8).shift(UP)
        text2 = Text("电压",size=0.5).move_to(2.5*UP+4*RIGHT).set_color(RED)
        line1 = Line(start=ORIGIN, end=RIGHT).next_to(text2,LEFT).set_color(RED)
        text3 = Text("电流",size=0.5).next_to(text2,DOWN).set_color(YELLOW)
        line2 = Line(start=ORIGIN, end=RIGHT).next_to(text3,LEFT).set_color(YELLOW)

        self.play(Write(text1))
        self.wait()
        self.play(
            text1.to_corner,UP+LEFT
        )
        self.wait()
        # 摆掉dt的限制
        def update_curveSin(func, alpha):
            dx = interpolate(1, 20, alpha)
            funcdx = fsin(dx)
            func.become(funcdx)

        def update_curveCos(func, alpha):
            dx = interpolate(1, 20, alpha)
            funcdx = fcos(dx)
            func.become(funcdx)

        self.play(
            ShowCreation(axes),
            ShowCreation(gsin),
            ShowCreation(gcos),
            ShowCreation(VGroup(text2,line1)),
            ShowCreation(VGroup(text3,line2))
            )
        self.wait(2)
        self.play(
            UpdateFromAlphaFunc(gsin,update_curveSin),
            UpdateFromAlphaFunc(gcos,update_curveCos),
            rate_func=linear,
            run_time=20
            )
        self.wait(5)

class ValueTrackerVector(GraphScene):
    CONFIG ={
        "x_min" : -1,
        "x_max" : 10,
        "y_min" : -1,
        "y_max" : 10,
        "x_axis_label" : "实数",
        "y_axis_label" : "虚数",
    }
    def construct(self):
        self.setup_axes()
        # 初始坐标
        x0=0
        y0=0
        x1=5
        y1=5
        vector1 = self.vector(x0,y0,x1,y1,True)
        vlu_x = ValueTracker(x1)
        vlu_y = ValueTracker(y1)
        vector1.add_updater(lambda obj: obj.become(self.vector(x0,y0,vlu_x.get_value(),vlu_y.get_value(),True)))
        elbow = self.polyline(ORIGIN,x1*RIGHT,x1*RIGHT+y1*UP)
        dot=Dot()
        dot.move_to(elbow.get_start())
        
        self.add(dot)
        self.play(
            MoveAlongPath(dot,elbow),
            run_time=5
        )
        self.play(ShowCreation(vector1),FadeOut(dot))
        self.add(vector1)
        self.play(
            vlu_x.increment_value,2,
            vlu_y.increment_value,1
            )
        self.play(vlu_y.increment_value,-1)
        self.play(vlu_x.increment_value,-2)
        self.wait()

        self.wait()

    def polyline(self,*points):
        polyline1 = VMobject()
        pointslist = [self.coords_to_point(point[0],point[1]) for point in points]
        polyline1.set_points_as_corners(pointslist)
        return polyline1

    def vector(self,x1=0,y1=0,x2=1,y2=1,texNeed=False):
        arr = Arrow(self.coords_to_point(x1,y1),self.coords_to_point(x2,y2),buff=0)
        if texNeed:
            tex = TexMobject("(%.1f,%.1f)"%(x2,y2))
            tex.next_to(arr.end,UP+RIGHT,buff=SMALL_BUFF)
            return VGroup(arr,tex)
        else:
            return arr

    def setup_axes(self):
        GraphScene.setup_axes(self)

        values_y = [(n,str(n)+"i") for n in range(0,10,2) if n!=0]
        self.y_axis_label_mob.set_color(RED)
        self.x_axis_label_mob.set_color(YELLOW)
        self.x_axis.add_numbers(*[i for i in range(0,10,2)])
        self.x_axis.numbers[0].shift(0.2*LEFT)
        self.y_axis_labels = VGroup()

        for y_val, y_tex in values_y:
            tex = TexMobject(y_tex) # Convert string to tex
            tex.scale(0.7) 
            # coords_to_point 获取指定值的点坐标
            tex.next_to(self.coords_to_point(0 ,y_val), LEFT)
            self.y_axis_labels.add(tex)  

        self.play(
            Write(self.y_axis_labels),
            Write(self.x_axis.numbers)
        )
        self.wait()

class ElbowVector(GraphScene):
    CONFIG ={
        "x_min" : -1,
        "x_max" : 10,
        "y_min" : -1,
        "y_max" : 10,
        "x_axis_label" : "实数",
        "y_axis_label" : "虚数",
    }
    def construct(self):
        self.setup_axes()
        # 初始坐标
        x0=0
        y0=0
        x1=0
        y1=0
        vector1 = self.vector(x0,y0,x1,y1,True)
        elbow = self.polyline(ORIGIN,5*RIGHT,5*RIGHT+5*UP)
        dot=Dot()
        dot.move_to(elbow.get_start())
        vector1.add_updater(lambda obj: obj.become(self.vector(
                    x0,y0,
                    self.point_to_coords(dot.get_center())[0],
                    self.point_to_coords(dot.get_center())[1],
                    True
                    )
                )
            )
        self.add(vector1)
        self.add(dot)
        self.play(
            MoveAlongPath(dot,elbow),
            run_time=2
        )
        self.wait()
        self.wait()

    def polyline(self,*points):
        polyline1 = VMobject()
        pointslist = [self.coords_to_point(point[0],point[1]) for point in points]
        polyline1.set_points_as_corners(pointslist)
        return polyline1

    def vector(self,x1=0,y1=0,x2=1,y2=1,texNeed=False):
        arr = Arrow(self.coords_to_point(x1,y1),self.coords_to_point(x2,y2),buff=0)
        if texNeed:
            tex = TexMobject("(%.1f,%.1f)"%(x2,abs(y2)))
            tex.next_to(arr.end,UP+RIGHT,buff=SMALL_BUFF)
            return VGroup(arr,tex)
        else:
            return arr

    def setup_axes(self):
        GraphScene.setup_axes(self)

        values_y = [(n,str(n)+"i") for n in range(0,10,2) if n!=0]
        self.y_axis_label_mob.set_color(RED)
        self.x_axis_label_mob.set_color(YELLOW)
        self.x_axis.add_numbers(*[i for i in range(0,10,2)])
        self.x_axis.numbers[0].shift(0.2*LEFT)
        self.y_axis_labels = VGroup()

        for y_val, y_tex in values_y:
            tex = TexMobject(y_tex) # Convert string to tex
            tex.scale(0.7) 
            # coords_to_point 获取指定值的点坐标
            tex.next_to(self.coords_to_point(0 ,y_val), LEFT)
            self.y_axis_labels.add(tex)  

        self.play(
            Write(self.y_axis_labels),
            Write(self.x_axis.numbers)
        )
        self.wait()

class ArcCoords(GraphScene):
    CONFIG ={
        "x_min" : -1,
        "x_max" : 10,
        "y_min" : -1,
        "y_max" : 10,
        "x_axis_label" : "实数",
        "y_axis_label" : "虚数",
    }
    def construct(self):
        self.setup_axes()
        # 初始坐标
        x0=0
        y0=0
        vector1 = self.vector(x0,y0,5,0,True)
        arc = Arc(radius=5)
        arcCoords = VMobject()
        arcCoords.set_points([self.coords_to_point(point[0],point[1]) for point in arc.points])
        dot = Dot()
        dot.move_to(arcCoords.get_start())
        vector1.add_updater(lambda obj: obj.become(self.vector(
                    x0,y0,
                    self.point_to_coords(dot.get_center())[0],
                    self.point_to_coords(dot.get_center())[1],
                    True
                    )
                )
            )
        self.add(vector1)
        self.add(dot)
        self.play(
            MoveAlongPath(dot,arcCoords),
            run_time=2
        )
        self.wait()
        self.wait()

    def polyline(self,*points):
        polyline1 = VMobject()
        pointslist = [self.coords_to_point(point[0],point[1]) for point in points]
        polyline1.set_points_as_corners(pointslist)
        return polyline1

    def vector(self,x1=0,y1=0,x2=1,y2=1,texNeed=False):
        arr = Arrow(self.coords_to_point(x1,y1),self.coords_to_point(x2,y2),buff=0)
        if texNeed:
            tex = TexMobject("(%.1f,%.1f)"%(x2,y2))
            tex.next_to(arr.end,UP+RIGHT,buff=SMALL_BUFF)
            return VGroup(arr,tex)
        else:
            return arr

    def setup_axes(self):
        GraphScene.setup_axes(self)

        values_y = [(n,str(n)+"i") for n in range(0,10,2) if n!=0]
        self.y_axis_label_mob.set_color(RED)
        self.x_axis_label_mob.set_color(YELLOW)
        self.x_axis.add_numbers(*[i for i in range(0,10,2)])
        self.x_axis.numbers[0].shift(0.2*LEFT)
        self.y_axis_labels = VGroup()

        for y_val, y_tex in values_y:
            tex = TexMobject(y_tex) # Convert string to tex
            tex.scale(0.7) 
            # coords_to_point 获取指定值的点坐标
            tex.next_to(self.coords_to_point(0 ,y_val), LEFT)
            self.y_axis_labels.add(tex)  

        self.play(
            Write(self.y_axis_labels),
            Write(self.x_axis.numbers)
        )
        self.wait()

class TexTest(Scene):
    def construct(self):
        rect = Rectangle(
            height = 3.5, width = 6.5,
            stroke_width = 0,
            fill_color = BLUE,
            fill_opacity = 0.8
        )
        rect.to_corner(UP+LEFT, buff = 0)
        top_line = TexMobject("(2+i)", "(2+i)")
        top_line.next_to(rect.get_top(), DOWN)
        second_line = TexMobject(
            "2^2 + 2i + 2i + i^2"
            )
        second_line.next_to(top_line, DOWN, MED_LARGE_BUFF)
        index_alignment_lists = [
            [(0, 1, 0), (1, 1, 1)],
            [(0, 2, 2), (0, 1, 3), (1, 3, 4)],
            [(0, 2, 5), (1, 1, 6), (0, 3, 7)],
            [(0, 2, 8), (0, 3, 9), (1, 3, 10)],
        ]
        self.add(rect,top_line)
        for index_alignment in index_alignment_lists:
            self.play(*[
                ReplacementTransform(
                    top_line[i][j].copy(), second_line[0][k],
                )
                for i, j, k in index_alignment
            ])
        self.wait(2)

class TexTest2(Scene):
    def construct(self):
        top_line = TexMobject("(2+i)", "(2+i)")
        second_line = TexMobject("2^2 + 2i + 2i + i^2")
        i=1
        j=3
        print(len(second_line[0]))
        self.add(top_line[i][j])
        self.wait(2)

class testNumberPlane(Scene):
    def construct(self):
        center_point = 2.6*DOWN + 2*LEFT
        plane = NumberPlane(
            center_point = center_point,
            x_min=-FRAME_X_RADIUS*2,
            x_max=FRAME_X_RADIUS*2,
            y_min=-FRAME_Y_RADIUS*2,
            y_max=FRAME_Y_RADIUS*2,
            axis_config = {
                "stroke_color": WHITE,
                "stroke_width": 5,
                },
            background_line_style = {
                "stroke_color": GRAY,
                "stroke_width": 2,
                "stroke_opacity": 0.5,
                }
            )
        plane.add_coordinates() # 显示坐标

        cir = Circle(radius=1).move_to(center_point)
        v1 = plane.get_vector([3,3])
        v2 = plane.get_vector([1,2])
        v3 = plane.get_complete_vector([1,2,3,3])
        self.play(ShowCreation(plane))
        self.add(v1,v2,v3,cir)
        self.wait()

class testComplexPlane(Scene):
    def construct(self):
        plane = ComplexPlane(
            center_point = 2.6*DOWN + 2*LEFT,
            x_min=-FRAME_X_RADIUS*2,
            x_max=FRAME_X_RADIUS*2,
            y_min=-FRAME_Y_RADIUS*2,
            y_max=FRAME_Y_RADIUS*2,
            axis_config = {
                "stroke_color": WHITE,
                "stroke_width": 5,
                },
            background_line_style = {
                "stroke_color": GRAY,
                "stroke_width": 2,
                "stroke_opacity": 1,
                }
            )
        plane.add_coordinates() # 显示坐标

        v1 = plane.get_vector([3,3])
        v2 = plane.get_vector([1,2])
        v3 = plane.get_complete_vector([1,2,3,3]).set_color(RED)

        self.play(ShowCreation(plane))
        self.add(v1,v2,v3)
        self.wait()

class BackgroundColorScene(Scene):
    CONFIG={
        "camera_config":{"background_color":DARK_GREY}
    }
    def construct(self):
        mob1 = TextMobject("Only a life lived for others is a life worthwhile").to_edge(TOP)
        mob2 = TextMobject("Subtle is the Lord， but malicious He is not")
        self.play(FadeInFromRandomB(mob1[0]))
        self.play(FadeInFromRandomA(mob2[0]))
        self.wait()

class MoveToTargetScene(Scene):
    def construct(self):
        dirc = 2*UP+RIGHT
        dot = Dot(dirc)
        line = Line(ORIGIN,dirc)
        dot.generate_target()
        dot.target.move_to(ORIGIN)
        line.generate_target()
        line.target.scale(0, about_point = ORIGIN)

        tex = TexMobject("r=1",color=YELLOW).next_to(line,DOWN)
        tex.add_background_rectangle().fade()

        self.add(tex)
        self.add(dot.copy().fade())
        self.add(line.copy().set_stroke(GREY, 1))
        self.play(*list(map(MoveToTarget, [dot, line])))
        self.wait()

# SVGMobject中获得点
class ShpaeTest1(Scene):
    def construct(self):
        path1 = self.get_path().shift(3*LEFT)
        self.play(ShowCreation(path1))
        self.wait()

        line = Line(ORIGIN,RIGHT)
        lineGroup = VGroup(
            line,
            line.copy(),
            line.copy(),
            line.copy(),
            line.copy(),
            line.copy(),
            line.copy(),
            line.copy()
            ).arrange_in_grid(3,2).shift(3*RIGHT)
        self.add(lineGroup)
        self.wait()

    def get_shape(self):
        shape = SVGMobject("camera")
        return shape

    def get_path(self):
        shape = self.get_shape()
        # 获得SVG对象
        # 在Mobject类中定义
        path = shape.family_members_with_points()[0]
        # path.set_height(5)
        path.set_fill(opacity=0)
        path.set_stroke(WHITE, 3)
        return path

class ComplexPlaneScene(Scene):
    def construct(self):
        self.background_plane = ComplexPlane(
            center_point = ORIGIN,
            x_min=-FRAME_X_RADIUS*2,
            x_max=FRAME_X_RADIUS*2,
            y_min=-FRAME_Y_RADIUS*2,
            y_max=FRAME_Y_RADIUS*2,
            axis_config = {
                "stroke_color": WHITE,
                "stroke_width": 5,
                },
            background_line_style = {
                "stroke_color": GRAY,
                "stroke_width": 2,
                "stroke_opacity": 1,
                }
            )
        self.background_plane.add_coordinates() # 显示坐标

        clr = Circle()
        neg_one_point = self.background_plane.number_to_point(-1)
        self.neg_one_dot = Dot(neg_one_point, color = BLUE)

        self.add(self.background_plane,clr)
        self.show_all_rational_slopes()   
    
    def show_all_rational_slopes(self):

        lines = VGroup()
        labels = VGroup()
        for u in range(2, 7):
            for v in range(1, u):
                if fractions.gcd(u, v) != 1:
                    continue
                z_squared = complex(u, v)**2
                unit_z_squared = z_squared/abs(z_squared)
                point = self.background_plane.number_to_point(unit_z_squared)
                dot = Dot(point, color = YELLOW)
                line = Line(
                    self.background_plane.number_to_point(-1),
                    point,
                    color = self.neg_one_dot.get_color()
                )
                line.add(dot)

                label = TexMobject(
                    "\\text{Slope = }",
                    str(v), "/", str(u)
                )
                label.add_background_rectangle()
                label.next_to(
                    self.background_plane.coords_to_point(1, 1.5),
                    RIGHT
                )

                lines.add(line)
                labels.add(label)
        line = lines[0]
        label = labels[0]

        self.play(
            ShowCreation(line),
            FadeIn(label)
        )
        self.wait()
        for new_line, new_label in list(zip(lines, labels))[1:]:
            self.play(
                Transform(line, new_line),
                Transform(label, new_label)
            )
            self.wait()
        self.play(*list(map(FadeOut, [line, label])))

class Cycloid(ParametricFunction):
    CONFIG = {
        "point_a": 3*LEFT+2*UP,
        "radius": 2,
        "end_theta": np.pi,
        "density": 5*DEFAULT_POINT_DENSITY_1D,
        "color": YELLOW
    }

    def __init__(self, **kwargs):
        digest_config(self, kwargs)
        ParametricFunction.__init__(self, self.pos_func, **kwargs)

    def pos_func(self, t):
        T = t*self.end_theta
        return self.point_a + self.radius * np.array([
            T - np.sin(T),
            np.cos(T) - 1,
            0
        ])

class RollAlongVector(Animation):
    CONFIG = {
        "rotation_vector": OUT,
    }

    def __init__(self, mobject, vector, **kwargs):
        # 获得对象的半径
        radius = mobject.get_width()/2
        # 求得向量的长度
        radians = get_norm(vector)/radius
        last_alpha = 0
        # 把本地参数给self
        digest_config(self, kwargs, locals())
        Animation.__init__(self, mobject, **kwargs)
    
    # animating 时会调用
    def interpolate_mobject(self, alpha):
        d_alpha = alpha - self.last_alpha
        self.last_alpha = alpha
        self.mobject.rotate_in_place(
            d_alpha*self.radians,
            self.rotation_vector
        )
        self.mobject.shift(d_alpha*self.vector)

class RollAlongVectorTest1(Scene):
    def construct(self):
        circle = Circle(radius=1)
        circle.add(Line(ORIGIN,RIGHT))
        circle.move_to(UP)
        vector = Line(ORIGIN,2*LEFT)
        self.play(
            RollAlongVector(
                circle,
                vector.points[-1]-vector.points[0]
            ),
            ShowCreation(vector)
        )

class RollAlongVectorTest2(Scene):
    def construct(self):
        circle = Square()
        circle.add(Line(ORIGIN,RIGHT))
        # circle.move_to(UP)
        vector = Line(ORIGIN,2*LEFT)
        self.play(
            RollAlongVector(
                circle,
                vector.points[-1]-vector.points[0]
            ),
            ShowCreation(vector)
        )

class CycloidScene(Scene):
    CONFIG = {
        "point_a": 6*LEFT+3*UP,
        "radius": 2,
        "end_theta": 2*np.pi
    }

    def construct(self):
        # 1、生成摆线
        self.generate_cycloid()
        # 2、生成圆和半径
        self.generate_circle()
        # 3、生成上顶线
        self.generate_ceiling()

    # 4、演示圆和顶线生成动画
    def grow_parts(self):
        self.play(*[
            ShowCreation(mob)
            for mob in (self.circle, self.ceiling)
        ])

    def generate_cycloid(self):
        self.cycloid = Cycloid(
            point_a=self.point_a,
            radius=self.radius,
            end_theta=self.end_theta
        )

    def generate_circle(self, **kwargs):
        self.circle = Circle(radius=self.radius, **kwargs)
        self.circle.shift(self.point_a - self.circle.get_top())
        radial_line = Line(
            self.circle.get_center(), self.point_a
        )
        self.circle.add(radial_line)

    def generate_ceiling(self):
        self.ceiling = Line(FRAME_X_RADIUS*LEFT, FRAME_X_RADIUS*RIGHT)
        self.ceiling.shift(self.cycloid.get_top()[1]*UP)
    # 5、动画
    def draw_cycloid(self, run_time=3, *anims, **kwargs):
        # 相当于给kwargs添加run_time
        kwargs["run_time"] = run_time
        self.play(
            RollAlongVector(
                self.circle,
                self.cycloid.points[-1]-self.cycloid.points[0],
                **kwargs
            ),
            ShowCreation(self.cycloid, **kwargs),
            *anims
        )

    def roll_back(self, run_time=3, *anims, **kwargs):
        kwargs["run_time"] = run_time
        self.play(
            RollAlongVector(
                self.circle,
                self.cycloid.points[0]-self.cycloid.points[- 1],
                rotation_vector=IN,
                **kwargs
            ),
            ShowCreation(
                self.cycloid,
                # 倒放
                rate_func=lambda t: smooth(1-t),
                **kwargs
            ),
            *anims
        )
        self.generate_cycloid()

class DrawCycloid(CycloidScene):
    def construct(self):
        CycloidScene.construct(self)
        self.grow_parts()
        self.draw_cycloid()
        self.wait()
        self.roll_back()