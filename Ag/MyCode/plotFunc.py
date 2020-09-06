from manimlib.imports import *

def ObjAnd2Text(Obj,text1,text2):
    if isinstance(Obj,VMobject):
        pic = Rectangle(
            height = Obj.get_height() + 0.618,
            width = Obj.get_width() + 1.2,
            stroke_color = BLACK,
            fill_color = BLACK,
            fill_opacity = 1,
            )
    else:
        pic = ImageMobject(Obj).scale(2)
    picText1 = Text(text1,
                    color="#308032"
        )\
        .set_height(0.23)\
        .next_to(pic,DOWN,buff=SMALL_BUFF)
    picText2 = Text(text2, 
                    color=BLACK
        )\
        .set_height(0.28)\
        .next_to(picText1,DOWN,buff=SMALL_BUFF)
    picAndText = Group(pic,picText1,picText2).center()
    pic.rect = RoundedRectangle(
                    corner_radius=0.1,
                    color="#DDDDDD",
                    fill_color = "#DDDDDD",
                    fill_opacity = 1,
                    height=picAndText.get_height()+0.2,
                    width=picAndText.get_width()+0.2
        )
    return Group(pic.rect,pic,picText1,picText2)

def ObjAnd1Text(Obj,text2):
    if isinstance(Obj,VMobject):
        pic = Rectangle(
            height = Obj.get_height() + 0.618,
            width = Obj.get_width() + 1.2,
            stroke_color = BLACK,
            fill_color = BLACK,
            fill_opacity = 1,
            )
    else:
        pic = ImageMobject(Obj).scale(2)
    picText2 = Text(text2, 
                    # font='Microsoft YaHei',
                    color=BLACK
        )\
        .set_height(0.28)\
        .next_to(pic,DOWN,buff=SMALL_BUFF*1.1)
    picAndText = Group(pic,picText2).center()
    pic.rect = RoundedRectangle(
                    corner_radius=0.1,
                    color="#DDDDDD",
                    fill_color = "#DDDDDD",
                    fill_opacity = 1,
                    height=picAndText.get_height()+0.2,
                    width=picAndText.get_width()+0.2
        )
    return Group(pic.rect,pic,picText2)

def palyALL2(self,allParts):
    self.play(
        FadeInFromLarge(allParts[:2]),
        AnimationGroup(
                    Animation(Mobject(),run_time=0.1),
                    FadeInFromDirections(allParts[2]),
                    FadeInFromDirections(allParts[3]),
                    lag_ratio=0.1
            )
        )
    self.wait(15)
    self.play(FadeOutAndShiftDown(allParts))

def palyALL1(self,allParts):
    self.play(
        FadeInFromLarge(allParts[:2]),
        AnimationGroup(
                    Animation(Mobject(),run_time=0.1),
                    FadeInFromDirections(allParts[2]),
                    lag_ratio=0.1
            )
        )
    self.wait(15)
    self.play(FadeOutAndShiftDown(allParts))

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

class BarChartRectangle(VGroup):
    def __init__(self,values,width, graph_origin_down=2.6, **kwargs):
        VGroup.__init__(self, **kwargs)
        for value in values:
            print(value)
            bar = Rectangle(
                height=abs(value[1]+graph_origin_down),
                width=width,
                fill_opacity=0.5,
            )
            bar.next_to(np.array(value),DOWN,buff=0)
            self.add(bar)

class PlotBarChart(GraphFromData):
    CONFIG = {
        "x_max" : 8,
        "x_min" : 0,
        "y_max" : 30,
        "y_min" : 0,
        "x_tick_frequency" : 2, 
        "y_tick_frequency" : 5, 
        "axes_color" : BLUE, 
        "x_axis_label": "x",
        "y_axis_label": "y",
    }
    def construct(self):
        self.setup_axes()
        x = [1, 2, 3, 4,  5,  6, 7]
        y = [2, 4, 6, 8, 10, 20, 25]

        coords = [[px,py] for px,py in zip(x,y)]
        points = self.get_points_from_coords(coords)

        graph = BarChartRectangle(points,0.5)

        self.play(FadeIn(graph))
        self.wait()

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
        axes = self.setup_axes(reback=True)
        # Get coords
        coords = get_coords_from_csv(r"Ag\MyCode\InsuranceData1")
        points = self.get_points_from_coords(coords)
        # Set graph
        graph = DiscreteGraphFromSetPoints(points,color=ORANGE)
        graph.set_stroke(width=10)

        allVG = VGroup(axes,graph).scale(0.618).shift(LEFT*0.8+UP*0.2)

        allParts = ObjAnd1Text(
                        allVG,
                        "“相互宝”参与人数与时间的关系"         
            )

        self.play(
            FadeInFromLarge(allParts[:2]),
            FadeInFromLarge(axes),
            AnimationGroup(
                        Animation(Mobject(),run_time=0.1),
                        FadeInFromDirections(allParts[2]),
                        lag_ratio=5
                )
            )        
        self.play(ShowCreation(graph,run_time=4))
        self.wait(15)
        self.play(FadeOutAndShiftDown(allParts),FadeOutAndShiftDown(allVG))


    def setup_axes(self,reback=False):
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
        self.x_axis.add(self.x_axis_labels)
        if reback:
            return VGroup(self.x_axis, self.y_axis)

class Plot31(GraphFromData):
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
        axes = self.setup_axes(reback=True)
        # Get coords
        coords = get_coords_from_csv(r"Ag\MyCode\InsuranceData1")
        points = self.get_points_from_coords(coords)
        # Set graph
        graph = DiscreteGraphFromSetPoints(points,color=ORANGE)
        graph.set_stroke(width=10)

        allVG = VGroup(axes,graph).scale(0.7).shift(LEFT*0.8+UP*0.618)
        text = Text("“相互宝”参与人数与时间的关系",size=0.4,color=ORANGE).next_to(allVG,DOWN)

        self.play(
            FadeInFromLarge(text),
            FadeInFromLarge(axes))        
        self.play(ShowCreation(graph,run_time=4))
        self.wait(15)

    def setup_axes(self,reback=False):
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
        self.x_axis.add(self.x_axis_labels)
        if reback:
            return VGroup(self.x_axis, self.y_axis)

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
        "y_axis_label": "\\heiti{分摊金(元/期)}",
    }
    def construct(self):
        axes = self.setup_axes(reback=True)
        # Get coords
        coords = get_coords_from_csv(r"Ag\MyCode\InsuranceData2")
        points = self.get_points_from_coords(coords)
        # Set graph
        graph = DiscreteGraphFromSetPoints(points,color=RED)
        graph.set_stroke(width=10)

        allVG = VGroup(axes,graph).scale(0.618).shift(LEFT*0.8+UP*0.2)

        allParts = ObjAnd1Text(
                        allVG,
                        "“相互宝”人均分摊金额变化规律"         
            )

        self.play(
            FadeInFromLarge(allParts[:2]),
            FadeInFromLarge(axes),
            AnimationGroup(
                        Animation(Mobject(),run_time=0.1),
                        FadeInFromDirections(allParts[2]),
                        lag_ratio=5
                )
            )        
        self.play(ShowCreation(graph,run_time=4))
        self.wait(15)
        self.play(FadeOutAndShiftDown(allParts),FadeOutAndShiftDown(allVG))

    def setup_axes(self,reback=False):
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
        self.x_axis.add(self.x_axis_labels)
        if reback:
            return VGroup(self.x_axis, self.y_axis)

class Plot5(GraphFromData):
    CONFIG = {
        "y_max" : 1800,
        "y_min" : 0,
        "x_max" : 70,
        "x_min" : 0,
        "y_tick_frequency" : 200, 
        "x_tick_frequency" : 10, 
        "axes_color" : BLUE, 
        "x_labeled_nums": range(0,70,10),
        "y_labeled_nums": range(0,1800,200),
        "x_num_decimal_places": 0,
        "x_axis_label": "\\heiti{年龄(岁)}",
        "y_axis_label": "\\heiti{纯保费(元)}",
    }
    def construct(self):
        axes = self.setup_axes(reback=True)
        # Get coords
        coords = get_coords_from_csv(r"Ag\MyCode\InsuranceData3")
        points = self.get_points_from_coords(coords)
        # Set graph
        graph1 = DiscreteGraphFromSetPoints(points[:40],color=RED)
        graph2 = DiscreteGraphFromSetPoints(points[40:],color=RED)
        graph3 = DiscreteGraphFromSetPoints(points[39:41],color=RED)
        graph3_dash = DashedVMobject(graph3,num_dashes=6)
        graph1.set_stroke(width=10)
        graph2.set_stroke(width=10)
        graph3_dash.set_stroke(width=10)

        allVG = VGroup(axes,graph1,graph2,graph3,graph3_dash).scale(0.618).shift(LEFT*0.8)

        allParts = ObjAnd1Text(
                        allVG,
                        "纯保费与年龄的关系图"         
            )
        
        self.play(
            FadeInFromLarge(allParts[:2]),
            FadeInFromLarge(axes),
            AnimationGroup(
                        Animation(Mobject(),run_time=0.1),
                        FadeInFromDirections(allParts[2]),
                        lag_ratio=5
                )
            )
        
        self.play(ShowCreation(graph1,run_time=4))
        self.play(ShowCreation(graph3_dash,run_time=1))
        self.play(ShowCreation(graph2,run_time=4))

        self.wait(15)
        self.play(FadeOutAndShiftDown(allParts),FadeOutAndShiftDown(allVG))
 
class Plot6(Scene):
    def construct(self):
        r=1.618
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
        position1 = [ORIGIN,0.236*UR,0.236*UR+2.2*RIGHT]
        polyline1.set_points_as_corners(position1)
        polyline1.set_color(RED).next_to(arc1,UR,buff=-0.6)
        text1.next_to(polyline1,UP,buff=0.2,aligned_edge=RIGHT)

        polyline2 = VMobject()
        position2 = [ORIGIN,0.236*DR,0.236*DR+2.2*RIGHT]
        polyline2.set_points_as_corners(position2)
        polyline2.set_color(RED).next_to(arc2,DR,buff=-0.6)
        text2.next_to(polyline2,UP,buff=-0.04,aligned_edge=RIGHT)

        Tx1 = Text("80后",size=0.36).next_to(text1,DOWN,buff=0.3,aligned_edge=RIGHT)
        Tx2 = Text("90后",size=0.36).next_to(text2,DOWN,buff=0.3,aligned_edge=RIGHT)

        Txt = Text("成员以80、90后社会中坚为主",font="宋体",size=0.42).next_to(polyline2.get_left(),DOWN,buff=1.2).shift(0.5*LEFT)
        Txtsrr = Underline(Txt,color=RED,stroke_width=1)
        allVG = VGroup(circle1,arc1,arc2,txt1,txt2,polyline1,text1,polyline2,text2,Tx1,Tx2,Txt,Txtsrr).move_to(ORIGIN).scale(0.8)

        group1 = VGroup(arc1,txt1,polyline1,Tx1)
        group2 = VGroup(arc2,txt2,polyline2,Tx2)

        allParts = ObjAnd1Text(
                        allVG,
                        "“相互宝”成员年龄构成"         
            )
        
        self.play(
            FadeInFromLarge(allParts[:2]),
            FadeInFromLarge(circle1),
            AnimationGroup(
                        Animation(Mobject(),run_time=0.1),
                        FadeInFromDirections(allParts[2]),
                        lag_ratio=5
                )
            )
        
        self.play(Write(group1),run_time=2)
        self.wait()
        self.play(Indicate(text1,color=RED))
        self.wait()
        self.play(Write(group2),run_time=2)
        self.wait()
        self.play(Indicate(text2,color=RED))
        self.wait()
        self.play(Write(Txt),ShowCreation(Txtsrr))

        self.wait(15)
        self.play(FadeOutAndShiftDown(allParts),FadeOutAndShiftDown(allVG))

def get_coords_from_csvdata(file_name):
    import csv
    coords = []
    with open(f'{file_name}.csv', 'r', encoding='UTF-8') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            coords.append(row)
    csvFile.close()
    return coords

class Plot7(Scene):
    # CONFIG = {
    #     "camera_config": {"background_color": GRAY},   
    # }
    def construct(self):
        data = get_coords_from_csvdata(r"Ag\MyCode\InsuranceData4")
        dataArray=np.array(data)
        row = dataArray.shape[0]
        column = dataArray.shape[1]
        x, y, dx, dy = -column+1, 3, 2, 0.5
        dataTxt = []
        dataTxtBackground = []
        for i in range(row):
            for j in range(column):
                target_ij = Text(dataArray[i][j])
                if i==0:
                    target_ij.scale(0.5)
                    target_ij.set_color(RED)
                else:
                    target_ij.scale(0.35)
                target_ij.shift(np.array([x+j*dx,y-i*dy,0]))
                dataTxt.append(target_ij)
            if (i+1)%2:
                target_i = Rectangle(
                    width=column*dx,
                    height=dy,
                    color=GRAY,
                    fill_color=GRAY,
                    fill_opacity=0.236,
                    stroke_opacity=0
                    ).move_to(target_ij).shift(np.array([-int(column/2)*dx,0,0]))
                dataTxtBackground.append(target_i)
 
        allGroupHead = VGroup(
            dataTxtBackground[0],
            dataTxtBackground[0].copy(),
            *dataTxt[:column]
            )
        
        allGroup = VGroup(
            dataTxtBackground[0].copy(),
            *dataTxtBackground,
            *dataTxt,
            )

        self.play(
            FadeInFromDirections(allGroup[0]),
            FadeInFromDirections(dataTxtBackground[0]),
            FadeInFromDirections(dataTxt[:column])
            )
        self.play(
                LaggedStartMap(FadeIn,[obj for obj in dataTxt[column:]],lag_ratio=0.2),
                LaggedStartMap(FadeIn,[obj for obj in dataTxtBackground[1:]],lag_ratio=0.1),
                run_time=3
            )

        VGroupHeadForeground=VGroup(
                Rectangle(
                    width=column*dx,
                    height=dy,
                    color=BLACK,
                    fill_color=BLACK,
                    fill_opacity=1,
                    ).align_to(allGroupHead,DOWN),
                *allGroupHead
                )
        
        self.play(
            allGroup.remove(*allGroupHead).shift,(row-12)*dy*UP,
            VGroupHeadForeground.shift,ORIGIN,
            rate_func=linear,
            run_time=5
            )

        self.wait(5)    

class Insurance1(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "Insurance/1、腓尼基希波商帆船",
                        "腓尼基“希波”商帆船"         
            )
        palyALL1(self,allParts)

class Insurance2(Scene):
    def construct(self):
        allParts = ObjAnd2Text(
                        "Insurance/2、伦敦大火",
                        "Great Fire of London",
                        "伦敦博物馆藏图：1666年伦敦大火"         
            )
        palyALL2(self,allParts)

class Insurance3(Scene):
    def construct(self):
        allParts = ObjAnd2Text(
                        "Insurance/3、尼古拉斯巴蓬",
                        "Nicholas Barbon",
                        "尼古拉斯·巴蓬"         
            )
        palyALL2(self,allParts)

class Insurance4(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "Insurance/4、某火灾保险公司的消防标志",
                        "某火灾保险公司的消防标志"         
            )
        palyALL1(self,allParts)

class Insurance5(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "Insurance/5、主要国家保险市场份额变化",
                        "主要国家保险市场份额变化"         
            )
        palyALL1(self,allParts)

class Tmp1(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "pic/都江堰",
                        "都江堰地图显示"         
            )
        palyALL1(self,allParts)
