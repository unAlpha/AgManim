from manimlib.imports import *

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
