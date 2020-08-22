from manimlib.imports import *

class Plot1(GraphScene):
    CONFIG = {
        "y_max" : 1,
        "y_min" : 0,
        "x_max" : 120,
        "x_min" : 0,
        "y_tick_frequency" : 0.1, 
        "x_tick_frequency" : 10, 
        "axes_color" : BLUE, 
        "x_labeled_nums": range(0,120,10),
        "y_labeled_nums": list(np.arange(0, 1, 0.1)),
        "x_num_decimal_places": 0,
        "y_num_decimal_places": 1,
        "x_axis_label": "$N(year)$",
        "y_axis_label": "$P(probability)$",
    }
    def construct(self):
        self.setup_axes(animate=True)
        graph = self.get_graph(lambda x : 1-0.99**x,  
                                    color = GREEN,
                                    x_min = 0, 
                                    x_max = 100
                                    )

        p=Dot().move_to(self.coords_to_point(self.x_min, self.y_min))
        self.add(p)

        graph.set_stroke(width=10)

        graph_label = self.get_graph_label(graph, label="1-0.99^N", direction=UP+LEFT,buff=0)

        self.play(
        	ShowCreation(graph),
            ShowCreation(graph_label),
            run_time = 2
        )
        self.wait()

class Plot2(GraphScene):
    CONFIG = {
        "y_max" : 1,
        "y_min" : 0,
        "x_max" : 120,
        "x_min" : 0,
        "y_tick_frequency" : 0.1, 
        "x_tick_frequency" : 10, 
        "axes_color" : BLUE, 
        "x_labeled_nums": range(0,120,10),
        "x_num_decimal_places": 0,
        "x_axis_label": "$N(year)$",
        "y_axis_label": "$P(probability)$",
    }
    def construct(self):
        self.setup_axes()
        graph = self.get_graph(lambda x : 1-0.99**x,  
                                    color = RED,
                                    x_min = 0, 
                                    x_max = 100
                                    )

        p=Dot().move_to(self.coords_to_point(self.x_min, self.y_min))
        self.add(p)
        graph.set_stroke(width=10)
        graph_label = self.get_graph_label(graph, label="1-0.99^N", direction=UP+LEFT,buff=0)
        self.play(
        	ShowCreation(graph),
            Write(graph_label),
            run_time = 3.6
        )
        self.wait()

    def setup_axes(self):
        GraphScene.setup_axes(self)
        values_decimal_y=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
        list_y = [*["%s"%i for i in range(10,100,10)]]
        values_y = [
            (i,j)
            for i,j in zip(values_decimal_y,list_y)
        ]
        self.y_axis_labels = VGroup()
        for y_val, y_tex in values_y:
            tex = TexMobject(str(y_tex)+"\\%")
            tex.scale(0.75)
            tex.next_to(self.coords_to_point(0, y_val), LEFT)
            self.y_axis_labels.add(tex)
        self.add(self.y_axis_labels)

class GraphFromData(GraphScene):
    # Covert the data coords to the graph points
    def get_points_from_coords(self,coords):
        return [
            # Convert COORDS -> POINTS
            self.coords_to_point(px,py)
            # See manimlib/scene/graph_scene.py
            for px,py in coords
        ]

    # Return the dots of a set of points
    def get_dots_from_coords(self,coords,radius=0.1):
        points = self.get_points_from_coords(coords)
        dots = VGroup(*[
            Dot(radius=radius).move_to([px,py,pz])
            for px,py,pz in points
            ]
        )
        return dots

def get_coords_from_csv(file_name):
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

class SmoothGraphFromSetPoints(VMobject):
    def __init__(self,set_of_points,**kwargs):
        super().__init__(**kwargs)
        self.set_points_smoothly(set_of_points)

class DiscreteGraphFromSetPoints(VMobject):
    def __init__(self,set_of_points,**kwargs):
        super().__init__(**kwargs)
        self.set_points_as_corners(set_of_points)

class Plot3(GraphFromData):
    CONFIG = {
        "y_max" : 14000,
        "y_min" : 0,
        "x_max" : 50,
        "x_min" : 1,
        "y_tick_frequency" : 1000, 
        "x_tick_frequency" : 2, 
        "axes_color" : BLUE, 
        "y_labeled_nums": range(0,14000,2000),
        "x_num_decimal_places": 0,
        "x_axis_label": "\\heiti{时间(年/月)}",
        "y_axis_label": "\\heiti{参与分摊人数(万人)}",
    }
    def construct(self):
        self.setup_axes()
        # Get coords
        coords = get_coords_from_csv(r"Ag\MyCode\InsuranceData1")
        points = self.get_points_from_coords(coords)
        # Set graph
        graph = DiscreteGraphFromSetPoints(points,color=ORANGE)
        graph.set_stroke(width=10)
        self.play(ShowCreation(graph,run_time=4))
        self.wait(3)
    def setup_axes(self):
        GraphScene.setup_axes(self)
        values_decimal_x=[*[i for i in range(6,46,2)]]
        list_x = [
            "2019/01",
            "2019/02",
            "2019/03",
            "2019/04",
            "2019/05",
            "2019/06",
            "2019/07",
            "2019/08",
            "2019/09",
            "2019/10",
            "2019/11",
            "2019/12",
            "2020/01",
            "2020/02",
            "2020/03",
            "2020/04",
            "2020/05",
            "2020/06",
            "2020/07",
            "2020/08",
            ]
        values_x = [
            (i,j)
            for i,j in zip(values_decimal_x,list_x)
        ]
        self.x_axis_labels = VGroup()
        for x_val, x_tex in values_x:
            tex = TextMobject(x_tex)
            tex.scale(0.5)
            tex.next_to(self.coords_to_point(x_val, 0), 1.8*DOWN)
            tex.rotate(PI/4)
            self.x_axis_labels.add(tex)
        self.add(self.x_axis_labels)

class Plot4(GraphFromData):
    CONFIG = {
        "y_max" : 5,
        "y_min" : 0,
        "x_max" : 50,
        "x_min" : 1,
        "y_tick_frequency" : 1000, 
        "x_tick_frequency" : 2, 
        "axes_color" : BLUE, 
        "y_labeled_nums": range(0,6,1),
        "x_num_decimal_places": 0,
        "x_axis_label": "\\heiti{时间(年/月)}",
        "y_axis_label": "\\heiti{分摊金(元)}",
    }
    def construct(self):
        self.setup_axes()
        # Get coords
        coords = get_coords_from_csv(r"Ag\MyCode\InsuranceData2")
        points = self.get_points_from_coords(coords)
        # Set graph
        graph = DiscreteGraphFromSetPoints(points,color=RED)
        graph.set_stroke(width=10)
        self.play(ShowCreation(graph,run_time=4))
        self.wait(3)
    def setup_axes(self):
        GraphScene.setup_axes(self)
        values_decimal_x=[*[i for i in range(6,46,2)]]
        list_x = [
            "2019/01",
            "2019/02",
            "2019/03",
            "2019/04",
            "2019/05",
            "2019/06",
            "2019/07",
            "2019/08",
            "2019/09",
            "2019/10",
            "2019/11",
            "2019/12",
            "2020/01",
            "2020/02",
            "2020/03",
            "2020/04",
            "2020/05",
            "2020/06",
            "2020/07",
            "2020/08",
            ]
        values_x = [
            (i,j)
            for i,j in zip(values_decimal_x,list_x)
        ]
        self.x_axis_labels = VGroup()
        for x_val, x_tex in values_x:
            tex = TextMobject(x_tex)
            tex.scale(0.5)
            tex.next_to(self.coords_to_point(x_val, 0), 1.8*DOWN)
            tex.rotate(PI/4)
            self.x_axis_labels.add(tex)
        self.add(self.x_axis_labels)

class Plot5(GraphFromData):
    CONFIG = {
        "y_max" : 1600,
        "y_min" : 0,
        "x_max" : 70,
        "x_min" : 0,
        "y_tick_frequency" : 200, 
        "x_tick_frequency" : 10, 
        "axes_color" : BLUE, 
        "x_labeled_nums": range(0,70,10),
        "y_labeled_nums": range(0,1600,200),
        "x_num_decimal_places": 0,
        "x_axis_label": "\\heiti{年龄(岁)}",
        "y_axis_label": "\\heiti{纯保费(元)}",
    }
    def construct(self):
        self.setup_axes()
        # Get coords
        coords = get_coords_from_csv(r"Ag\MyCode\InsuranceData3")
        points = self.get_points_from_coords(coords)
        # Set graph
        graph1 = DiscreteGraphFromSetPoints(points[:40],color=RED)
        graph2 = DiscreteGraphFromSetPoints(points[40:],color=RED)
        graph3 = DiscreteGraphFromSetPoints(points[39:41],color=RED)
        graph3_dash = DashedVMobject(graph3,num_dashes=8)
        graph1.set_stroke(width=10)
        graph2.set_stroke(width=10)
        graph3_dash.set_stroke(width=10)
        self.play(ShowCreation(graph1,run_time=4))
        self.play(ShowCreation(graph3_dash,run_time=1))
        self.play(ShowCreation(graph2,run_time=4))
        self.wait(3)

class Plot6(Scene):
    def construct(self):
        r=2
        circle1 = Circle(
                        radius=r,
                        stroke_color=GRAY,
                        fill_color=GRAY,
                        fill_opacity=1)
        arc1 = Sector(
                        inner_radius=0,
                        outer_radius=r,
                        angle=29.6*TAU/100,
                        start_angle=0,
                        stroke_color=ORANGE,
                        fill_color=ORANGE,
                        fill_opacity=1)
        arc2 = Sector(
                        inner_radius=0,
                        outer_radius=r,
                        angle=28.4*TAU/100,
                        start_angle=-28.4*TAU/100,
                        stroke_color=YELLOW,
                        fill_color=YELLOW,
                        fill_opacity=1)

        txt1 = Text("80's",color=BLACK,size=0.382)
        text1 = Text("29.6%",color=RED,size=0.618)
        txt2 = Text("90's",color=BLACK,size=0.382)
        text2 = Text("28.4%",color=RED,size=0.618)

        txt1.move_to(arc1)
        txt2.move_to(arc2)

        polyline1 = VMobject()
        position1 = [ORIGIN,0.236*UR,0.236*UR+2*RIGHT]
        polyline1.set_points_as_corners(position1)
        polyline1.set_color(RED).next_to(arc1,UR,buff=-0.6)
        text1.next_to(polyline1,UP,buff=0.2,aligned_edge=RIGHT)

        polyline2 = VMobject()
        position2 = [ORIGIN,0.236*DR,0.236*DR+2*RIGHT]
        polyline2.set_points_as_corners(position2)
        polyline2.set_color(RED).next_to(arc2,DR,buff=-0.6)
        text2.next_to(polyline2,UP,buff=-0.04,aligned_edge=RIGHT)

        Tx1 = Text("80后",size=0.36).next_to(text1,DOWN,buff=0.3,aligned_edge=RIGHT)
        Tx2 = Text("90后",size=0.36).next_to(text2,DOWN,buff=0.3,aligned_edge=RIGHT)

        Txt = Text("成员以80、90后社会中坚为主",font="宋体",size=0.42).next_to(polyline2.get_left(),DOWN,buff=1.2).shift(0.5*LEFT)
        Txtsrr=Underline(Txt,color=RED,stroke_width=1)
        group= VGroup(circle1,arc1,arc2,txt1,txt2,polyline1,text1,polyline2,text2,Tx1,Tx2,Txt,Txtsrr).move_to(ORIGIN)

        self.add(group)
        self.wait()
