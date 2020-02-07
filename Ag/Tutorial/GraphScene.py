from manimlib.imports import *

class Graphing(GraphScene):
    CONFIG = {
        "x_min": -5,
        "x_max": 5,
        "y_min": -4,
        "y_max": 4,
        "graph_origin": ORIGIN,
        "function_color": WHITE,
        "axes_color": BLUE
    }

    def construct(self):
        #Make graph
        self.setup_axes(animate=True)
        func_graph=self.get_graph(self.func_to_graph,self.function_color)
        graph_lab = self.get_graph_label(func_graph, label = "x^{2}")

        func_graph_2=self.get_graph(self.func_to_graph_2,self.function_color)
        graph_lab_2 = self.get_graph_label(func_graph_2, label = "x^{3}")

        vert_line = self.get_vertical_line_to_graph(1,func_graph,color=YELLOW)

        x = self.coords_to_point(1, self.func_to_graph(1))
        y = self.coords_to_point(0, self.func_to_graph(1))
        horz_line = Line(x,y, color=YELLOW)

        point = Dot(self.coords_to_point(1,self.func_to_graph(1)))

        #Display graph
        self.play(ShowCreation(func_graph), Write(graph_lab))
        self.wait(1)
        self.play(ShowCreation(vert_line))
        self.play(ShowCreation(horz_line))
        self.add(point)
        self.wait(1)
        self.play(Transform(func_graph, func_graph_2), Transform(graph_lab, graph_lab_2))
        self.wait(2)


    def func_to_graph(self, x):
        return (x**2)

    def func_to_graph_2(self, x):
        return(x**3)


class ep0673(GraphScene):
    def construct(self):
        curve1=ParametricFunction(lambda x : np.array([2*np.cos(x),1*np.sin(x),0]),\
            color=BLUE,t_min=-TAU,t_max=TAU)
        self.play(ShowCreation(curve1),run_time=1)
        text1 = Text("椭圆",size=0.5).next_to(curve1,2*DOWN)
        self.play(Write(text1))
        self.wait(10)

class MultipleDeriv(Scene):
    def construct(self):
        title = TexMobject(r"\text{What does } \frac{d^nf}{dx^n} \text{ mean?}",
                           tex_to_color_map={r"\frac{d^nf}{dx^n}": YELLOW}
                           )
        title.scale(2)

        title2 = TexMobject(r"\text{What does } \frac{d^nf}{dx^n} \text{ mean?}",
                            tex_to_color_map={r"\frac{d^nf}{dx^n}": YELLOW}
                            )
        title2.shift(3 * UP)

        eq = TexMobject(
            r"\frac{d^nf}{dx^n}=", r"\left (\frac{d}{dx} ... \frac{d}{dx}\right )", r"f")
        eq.scale(1.5)

        b = Brace(eq[1])
        t = b.get_text("n times").scale(1.5)

        eq1 = VGroup(eq, b, t)

        f1 = ParametricFunction(
            lambda t: np.array([t, t**2, 0]),
            t_min=0,
            t_max=math.sqrt(2),
            color=RED,
            stroke_width=1.25*DEFAULT_STROKE_WIDTH
        )
        a1 = Axes(
            x_min=0,
            x_max=2,
            y_min=0,
            y_max=2,
            number_line_config={
                "include_tip": False,
            }
        )

        func1 = VGroup(a1, f1)
        func1.scale(1.5)
        func1.shift(4.5 * LEFT + 1 * DOWN)

        f2 = ParametricFunction(
            lambda t: np.array([t, 2*t, 0]),
            t_min=0,
            t_max=1,
            color=BLUE,
            stroke_width=1.25*DEFAULT_STROKE_WIDTH
        )
        a2 = Axes(
            x_min=0,
            x_max=2,
            y_min=0,
            y_max=2,
            number_line_config={
                "include_tip": False,
            }
        )

        func2 = VGroup(a2, f2)
        func2.scale(1.5)
        func2.shift(3 * RIGHT + 1 * DOWN)

        a = Arrow(1 * LEFT, 1 * RIGHT, color=GREEN)
        a.scale(1.5)

        t = TexMobject(r"\frac{d}{dx}")
        t.shift(1 * UP)

        arr = VGroup(a, t)

        self.play(Write(title))
        self.wait()

        self.play(Transform(title, title2))
        self.wait()

        self.play(Write(eq1))
        self.wait()

        self.play(Uncreate(eq1))
        self.play(Write(func1))
        self.wait()

        self.play(Write(arr))
        self.play(TransformFromCopy(func1, func2))
        self.wait()


class ExampleApproximation(GraphScene):
    CONFIG = {
        "function" : lambda x : np.cos(x), 
        "function_color" : BLUE,
        "taylor" : [lambda x: 1, lambda x: 1-x**2/2, lambda x: 1-x**2/math.factorial(2)+x**4/math.factorial(4), lambda x: 1-x**2/2+x**4/math.factorial(4)-x**6/math.factorial(6),
        lambda x: 1-x**2/math.factorial(2)+x**4/math.factorial(4)-x**6/math.factorial(6)+x**8/math.factorial(8), lambda x: 1-x**2/math.factorial(2)+x**4/math.factorial(4)-x**6/math.factorial(6)+x**8/math.factorial(8) - x**10/math.factorial(10)],
        "center_point" : 0,
        "approximation_color" : GREEN,
        "x_min" : -10,
        "x_max" : 10,
        "y_min" : -1,
        "y_max" : 1,
        "graph_origin" : ORIGIN ,
        "x_labeled_nums" :range(-10,12,2),

    }
    def construct(self):
        self.setup_axes(animate=True)
        func_graph = self.get_graph(
            self.function,
            self.function_color,
        )
        approx_graphs = [
            self.get_graph(
                f,
                self.approximation_color
            )
            for f in self.taylor
        ]

        term_num = [
            TexMobject("n = " + str(n),aligned_edge=TOP)
            for n in range(0,8)]
        #[t.to_edge(BOTTOM,buff=SMALL_BUFF) for t in term_num]

        #term = TexMobject("")
        #term.to_edge(BOTTOM,buff=SMALL_BUFF)
        term = VectorizedPoint(3*DOWN)

        approx_graph = VectorizedPoint(
            self.input_to_graph_point(self.center_point, func_graph)
        )

        self.play(
            ShowCreation(func_graph),
        )
        for n,graph in enumerate(approx_graphs):
            self.play(
                Transform(approx_graph, graph, run_time = 2),
                Transform(term,term_num[n])
            )
            self.wait()


class CSV(GraphScene):
    def construct(self):
        self.setup_axes()
        coords = self.return_coords_from_csv(r"Ag\Tutorial\data")
        dots = VGroup(*[Dot().move_to(self.coords_to_point(coord[0],coord[1])) for coord in coords])
        self.add(dots)

    def return_coords_from_csv(self,file_name):
        import csv
        coords = []
        with open(f'{file_name}.csv', 'r') as csvFile:
            reader = csv.reader(csvFile)
            for row in reader:
                x,y = row
                coord = [float(x),float(y)]
                coords.append(coord)
        csvFile.close()
        return coords


class RiemannRectangles(GraphScene):
    CONFIG = {
        "y_max": 8,
        "y_axis_height": 5,
    }
    def construct(self):
        self.setup_axes()
        def func(x):
            return 0.1 * (x + 3-5) * (x - 3-5) * (x-5) + 5

        graph=self.get_graph(func,x_min=0.3,x_max=9.2)
        riemann_rectangles=self.get_riemann_rectangles(
                                    graph,
                                    x_min=2,
                                    x_max=8,
                                    dx=0.5
                                    )
        self.add(graph,riemann_rectangles)

class RiemannRectanglesAnimation(GraphScene):
    CONFIG = {
        "y_max": 8,
        "y_axis_height": 5,
        "init_dx":0.5,
    }
    def construct(self):
        self.setup_axes()

        def func(x):
            return 0.1 * (x + 3-5) * (x - 3-5) * (x-5) + 5
        graph=self.get_graph(func,x_min=0.3,x_max=9.2)

        kwargs = {
            "x_min" : 2,
            "x_max" : 8,
            "fill_opacity" : 0.75,
            "stroke_width" : 0.25,
        }
        flat_rectangles = self.get_riemann_rectangles(
                                self.get_graph(lambda x : 0),
                                dx=self.init_dx,
                                start_color=invert_color(PURPLE),
                                end_color=invert_color(ORANGE),
                                **kwargs
        )
        riemann_rectangles_list = self.get_riemann_rectangles_list(
                                graph,
                                6,
                                max_dx=self.init_dx,
                                power_base=2,
                                start_color=PURPLE,
                                end_color=ORANGE,
                                 **kwargs
        )
        self.add(graph)
        # Show Riemann rectangles
        self.play(ReplacementTransform(flat_rectangles,riemann_rectangles_list[0]))
        self.wait()
        for r in range(1,len(riemann_rectangles_list)):
            self.transform_between_riemann_rects(
                    riemann_rectangles_list[r-1],
                    riemann_rectangles_list[r],
                    replace_mobject_with_target_in_scene = True,
                )
        self.wait()


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

class PlotDemo(GraphScene):
    CONFIG ={
        "x_min" : 0,
        "x_max" : 10,
        "x_tick_frequency" : 1,
        "y_min" : 0,
        "y_max" : 1000,
        "y_tick_frequency" : 200,
        "graph_origin": 3 * DOWN + 4 * LEFT,
    }
    def construct(self):
        self.setup_axes(animate=False)

        self.x_axis.add_numbers(*[0,1,2,3])
        self.y_axis.add_numbers(*[200,400,600])

        graghFuncXX = self.get_graph(lambda x: x**3,
                                    x_min = 1, 
                                    x_max = 9)
        self.play(ShowCreation(graghFuncXX),run_time=2)

class PlotGraph(GraphScene):
    CONFIG = {
        "y_max" : 60,
        "y_min" : 20,
        "x_max" : 8,
        "x_min" : 4,
        "y_tick_frequency" : 5, 
        "x_tick_frequency" : 1, 
        "axes_color" : BLUE,
        "y_labeled_nums": range(30,70,10),
        "x_labeled_nums": list(np.arange(4, 9, 1)),
        "x_label_decimal":1,
        "graph_origin": 3 * DOWN + 6 * LEFT,
        "x_label_direction":DOWN,
        "y_label_direction":RIGHT,
        "y_axis_label": "$f(x)$",
        "x_axis_width":12,
    }

    def construct(self):
        self.setup_axes(animate=False) #animate=True to add animation

        self.x_axis.shift(LEFT*abs(self.y_axis[0].points[0]-self.x_axis[0].points[0]))
        self.y_axis.shift(DOWN*abs(self.y_axis[0].points[0]-self.x_axis[0].points[0]))
        
        self.y_axis_label_mob.next_to(self.y_axis[0].get_end(),UP)
        self.x_axis_label_mob.next_to(self.x_axis[0].get_end(),RIGHT)

        p=Dot().move_to(self.coords_to_point(self.x_min, self.y_min))

        self.add(p)
        graph = self.get_graph(lambda x : x**2, 
                                    color = GREEN,
                                    x_min = 4.5, 
                                    x_max = 7.5
                                    )

        self.play(
            ShowCreation(graph),
            run_time = 2
        )
        self.wait()


def Range(in_val,end_val,step=1):
    return list(np.arange(in_val,end_val+step,step))

class Plot1(GraphScene):
    CONFIG = {
        "y_max" : 50,
        "y_min" : 0,
        "x_max" : 8,
        "x_min" : 0,
        "y_tick_frequency" : 5, 
        "x_tick_frequency" : 0.5, 
        "axes_color" : BLUE, 
        "y_labeled_nums": range(0,60,10),
        "x_labeled_nums": list(np.arange(0, 8, 1)),
    }
    def construct(self):
        self.setup_axes(animate=True)
        graph = self.get_graph(lambda x : x**2,  
                                    color = GREEN,
                                    x_min = 2, 
                                    x_max = 7
                                    )
        self.play(
        	ShowCreation(graph),
            run_time = 2
        )
        self.wait()

class Plot1v2(GraphScene):
    CONFIG = {
        "y_max" : 50,
        "y_min" : 0,
        "x_max" : 7,
        "x_min" : 0,
        "y_tick_frequency" : 5,
        "x_tick_frequency" : 1,
        "axes_color" : BLUE, 
        "graph_origin" : np.array((0,0,0))
    }
    def construct(self):
        self.setup_axes(animate=True)
        graph = self.get_graph(lambda x : x**2, 
                                    color = GREEN,
                                    x_min = 2, 
                                    x_max = 4
                                    )
        self.play(
            ShowCreation(graph),
            run_time = 2
        )
        self.wait()

class Plot2(GraphScene):
    CONFIG = {
        "y_max" : 50,
        "y_min" : 0,
        "x_max" : 7,
        "x_min" : 0,
        "y_tick_frequency" : 5,
        "axes_color" : BLUE,
        "x_axis_label" : "$t$",
        "y_axis_label" : "$f(t)$",
    }
    def construct(self):
        self.setup_axes()
        graph = self.get_graph(lambda x : x**2, color = GREEN)
        self.play(
        	ShowCreation(graph),
            run_time = 2
        )
        self.wait()

    def setup_axes(self):
        # Add this line
        GraphScene.setup_axes(self) 
        # Parametters of labels
        #   For x
        init_label_x = 2
        end_label_x = 7
        step_x = 1
        #   For y
        init_label_y = 20
        end_label_y = 50
        step_y = 5
        # Position of labels
        #   For x
        self.x_axis.label_direction = DOWN #DOWN is default
        #   For y
        self.y_axis.label_direction = LEFT
        # Add labels to graph
        #   For x
        self.x_axis.add_numbers(*range(
                                        init_label_x,
                                        end_label_x+step_x,
                                        step_x
                                    ))
        #   For y
        self.y_axis.add_numbers(*range(
                                        init_label_y,
                                        end_label_y+step_y,
                                        step_y
                                    ))
        #   Add Animation
        self.play(
            ShowCreation(self.x_axis),
            ShowCreation(self.y_axis)
        )

class Plot3(GraphScene):
    CONFIG = {
        "y_max" : 50,
        "y_min" : 0,
        "x_max" : 7,
        "x_min" : 0,
        "y_tick_frequency" : 10,
        "axes_color" : BLUE,
    }
    def construct(self):
        self.setup_axes()
        graph = self.get_graph(lambda x : x**2, color = GREEN)

        self.play(
            ShowCreation(graph),
            run_time = 2
        )
        self.wait()

    def setup_axes(self):
        GraphScene.setup_axes(self)
        # Custom parametters
        self.x_axis.add_numbers(*[0,2,5,4])
        # Y parametters
        init_label_y = 0
        end_label_y = 50
        step_y = 5
        self.y_axis.label_direction = LEFT
        self.y_axis.add_numbers(*range(
                                        init_label_y,
                                        end_label_y+step_y,
                                        step_y
                                    ))
        self.play(Write(self.x_axis),Write(self.y_axis))

class Plot4(GraphScene):
    CONFIG = {
        "y_max" : 50,
        "y_min" : 0,
        "x_max" : 7,
        "x_min" : 0,
        "y_tick_frequency" : 10,
        "axes_color" : BLUE,
    }
    def construct(self):
        self.setup_axes()
        graph = self.get_graph(lambda x : x**2, color = GREEN)

        self.play(
            ShowCreation(graph),
            run_time = 2
        )
        self.wait()

    def setup_axes(self):
        GraphScene.setup_axes(self)
        self.x_axis.label_direction = UP
        self.x_axis.add_numbers(*[3.5,5,4]) # 3.5 is rounded to 4
        self.y_axis.label_direction = LEFT
        self.y_axis.add_numbers(*range(0, 50+5, 5))
        self.play(Write(self.x_axis),Write(self.y_axis))

class Plot5(GraphScene):
    CONFIG = {
        "y_max" : 50,
        "y_min" : 0,
        "x_max" : 7,
        "x_min" : 0,
        "y_tick_frequency" : 10,
        "x_tick_frequency" : 0.5,
        "axes_color" : BLUE,
    }
    def construct(self):
        self.setup_axes()
        graph = self.get_graph(lambda x : x**2, color = GREEN)

        self.play(
            ShowCreation(graph),
            run_time = 2
        )
        self.wait()

    def setup_axes(self):
        GraphScene.setup_axes(self)
        self.x_axis.label_direction = UP
        values_x = [
            (3.5,"3.5"), # (position 3.5, label "3.5")
            (4.5,"\\frac{9}{2}") # (position 4.5, label "9/2")
        ]
        self.x_axis_labels = VGroup() # Create a group named x_axis_labels
        #   pos.   tex.
        for x_val, x_tex in values_x:
            tex = TexMobject(x_tex) # Convert string to tex
            tex.scale(0.7) 
            # coords_to_point 获取指定值的点坐标
            tex.next_to(self.coords_to_point(x_val, 0), DOWN) #Put tex on the position
            self.x_axis_labels.add(tex) #Add tex in graph
        self.play(
            Write(self.x_axis_labels),
            Write(self.x_axis),
            Write(self.y_axis)
        )

class Plot6(GraphScene):
    CONFIG = {
        "y_max" : 50,
        "y_min" : 0,
        "x_max" : 7,
        "x_min" : 0,
        "y_tick_frequency" : 10,
        "x_tick_frequency" : 0.5,
        "axes_color" : BLUE,
    }
    def construct(self):
        self.setup_axes()
        graph = self.get_graph(lambda x : x**2, color = GREEN)

        self.play(
            ShowCreation(graph),
            run_time = 2
        )
        self.wait()

    def setup_axes(self):
        GraphScene.setup_axes(self)
        self.x_axis.label_direction = UP
        # List of values of positions
        values_decimal_x=[0,0.5,1,1.5,3.35]
        # Transform positions to tex labels
        list_x = [*["%s"%i for i in values_decimal_x]]
        # List touples of (position,label)
        values_x = [
            (i,j)
            for i,j in zip(values_decimal_x,list_x)
        ]
        self.x_axis_labels = VGroup()
        for x_val, x_tex in values_x:
            tex = TexMobject(x_tex)
            tex.scale(0.7)
            tex.next_to(self.coords_to_point(x_val, 0), DOWN)
            self.x_axis_labels.add(tex)
        self.play(
            Write(self.x_axis_labels),
            Write(self.x_axis),
            Write(self.y_axis)
        )

class Plot7(GraphScene):
    CONFIG = {
        "y_max" : 50,
        "y_min" : 0,
        "x_max" : 7,
        "x_min" : 0,
        "y_tick_frequency" : 10,
        "x_tick_frequency" : 0.5,
        "axes_color" : BLUE,
    }
    def construct(self):
        self.setup_axes()
        graph = self.get_graph(lambda x : x**2, color = GREEN)

        self.play(
            ShowCreation(graph),
            run_time = 2
        )
        self.wait()

    def setup_axes(self):
        GraphScene.setup_axes(self)
        self.x_axis.label_direction = UP
        # Additional parametters
        init_val_x = 0
        step_x = 0.5
        end_val_x = 7
        # Position of labels
        values_decimal_x=Range(init_val_x,end_val_x,step_x)
        # List of labels
        list_x=[*["%.1f"%i for i in values_decimal_x]]
        # List touples of (posición,etiqueta)
        values_x = [
            (i,j)
            for i,j in zip(values_decimal_x,list_x)
        ]
        self.x_axis_labels = VGroup()
        for x_val, x_tex in values_x:
            tex = TexMobject(x_tex)
            tex.scale(0.7)
            tex.next_to(self.coords_to_point(x_val, 0), DOWN)
            self.x_axis_labels.add(tex)
        self.play(
            Write(self.x_axis_labels),
            Write(self.x_axis),
            Write(self.y_axis)
        )

class PlotSinCos(GraphScene):
    CONFIG = {
        "y_max" : 1.5,
        "y_min" : -1.5,
        "x_max" : 3*PI/2,
        "x_min" : -3*PI/2,
        "y_tick_frequency" : 0.5,
        "x_tick_frequency" : PI/2,
        "graph_origin" : ORIGIN,
        "y_axis_label": None, # Don't write y axis label
        "x_axis_label": None,
    }
    def construct(self):
        self.setup_axes()
        plotSin = self.get_graph(lambda x : np.sin(x), 
                                    color = GREEN,
                                    x_min=-4,
                                    x_max=4,
                                )
        plotCos = self.get_graph(lambda x : np.cos(x), 
                                    color = GRAY,
                                    x_min=-PI,
                                    x_max=0,
                                )
        plotSin.set_stroke(width=3) # width of line
        plotCos.set_stroke(width=2)
        # Animation
        for plot in (plotSin,plotCos):
            self.play(
                    ShowCreation(plot),
                    run_time = 2
                )
        self.wait()

    def setup_axes(self):
        GraphScene.setup_axes(self)
        # width of edges
        self.x_axis.set_stroke(width=2)
        self.y_axis.set_stroke(width=2)
        # color of edges
        self.x_axis.set_color(RED)
        self.y_axis.set_color(YELLOW)
        # Add x,y labels
        func = TexMobject("\\sin\\theta")
        var = TexMobject("\\theta")
        func.set_color(BLUE)
        var.set_color(PURPLE)
        func.next_to(self.y_axis,UP)
        var.next_to(self.x_axis,RIGHT+UP)
        # Y labels
        self.y_axis.label_direction = LEFT*1.5
        self.y_axis.add_numbers(*[-1,1])
        #Parametters of x labels
        init_val_x = -3*PI/2
        step_x = PI/2
        end_val_x = 3*PI/2
        # List of the positions of x labels
        values_decimal_x=Range(init_val_x,end_val_x,step_x) 
        # List of tex objects
        list_x=TexMobject("-\\frac{3\\pi}{2}", #   -3pi/2
                            "-\\pi", #              -pi 
                            "-\\frac{\\pi}{2}", #   -pi/2
                            "0", #                   0 (space)
                            "\\frac{\\pi}{2}", #     pi/2
                            "\\pi",#                 pi
                            "\\frac{3\\pi}{2}", #     3pi/2
                          )
        # .set_opacity()是函数，需要在()中写入参数
        list_x[3].set_opacity(0)
        #List touples (position,label)
        values_x = [(i,j)
            for i,j in zip(values_decimal_x,list_x)
        ]
        self.x_axis_labels = VGroup()
        for x_val, x_tex in values_x:
            x_tex.scale(0.7)
            if x_val == -PI or x_val == PI: #if x is equals -pi or pi
                x_tex.next_to(self.coords_to_point(x_val, 0), 2*DOWN) #Put 2*Down
            else: # In another case
                x_tex.next_to(self.coords_to_point(x_val, 0), DOWN)
            self.x_axis_labels.add(x_tex)

        self.play(
            *[Write(objeto)
            for objeto in [
                    self.y_axis,
                    self.x_axis,
                    self.x_axis_labels,
                    func,var
                ]
            ],
            run_time=2
        )