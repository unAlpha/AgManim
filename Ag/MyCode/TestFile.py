from manimlib.imports import *

class Sum1(Scene):
    def construct(self):
        equation1 = TexMobject("a", "^2", "+", "b", "^2", "=", "c", "^2")
        equation2 = TexMobject("aa", "^2", "+", "bb", "^2", "=", "cc", "^2")
        equation3 = TexMobject("A", "^2", "+", "bB", "^2", "=", "CcCCC", "^2")
        # list对象
        equation = VGroup(equation1,equation2,equation3).arrange(DOWN)
        equation1.next_to(equation3, DOWN, MED_LARGE_BUFF)
        equation1.shift_onto_screen(buff=5)
        # equation1.center()
        self.add(equation)

class SumPOW(Scene):
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
        sinGraph.scale(0.2)
        self.add(sinGraph)

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

        text1 = Text("D 这是一个测试")
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

        dashV = self.dashVector(1,1,8,1)

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
        tex = TexMobject("(%.1f,%.1f)"%(x2,y2))
        tex.next_to(arr.end,UP+RIGHT,buff=SMALL_BUFF)
        if texNeed:
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
        tex = TexMobject("(%.1f,%.1f)"%(x2,abs(y2)))
        tex.next_to(arr.end,UP+RIGHT,buff=SMALL_BUFF)
        if texNeed:
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
        tex = TexMobject("(%.1f,%.1f)"%(x2,y2))
        tex.next_to(arr.end,UP+RIGHT,buff=SMALL_BUFF)
        if texNeed:
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
            fill_color = BLACK,
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
        plane = NumberPlane(
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
        self.play(ShowCreation(plane))
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
        self.play(ShowCreation(plane))
        self.wait()