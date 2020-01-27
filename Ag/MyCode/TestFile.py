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
