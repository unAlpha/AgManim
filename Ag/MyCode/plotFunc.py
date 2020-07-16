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
        # "y_labeled_nums": list(np.arange(0, 1, 0.1)),
        "x_num_decimal_places": 0,
        # "y_num_decimal_places": 1,
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
        # List of values of positions
        values_decimal_y=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
        # Transform positions to tex labels
        list_y = [*["%s"%i for i in range(10,100,10)]]
        # List touples of (position,label)
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