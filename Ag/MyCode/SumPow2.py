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
