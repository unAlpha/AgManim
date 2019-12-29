from manimlib.imports import *

class DataRead(GraphScene):
    def construct(self):
        self.setup_axes()
        coords = self.return_coords()
        dots = VGroup(*[Dot().move_to(self.coords_to_point(coord[0],coord[1]))\
            for coord in coords])
        self.add(dots)
        Line()

    def return_coords(self):
        coords = ((1,2),(2,4))
        return coords