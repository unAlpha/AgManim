from manimlib.imports import *

def debugTeX(self, texm):
    for i,j in enumerate(texm):
        tex_id = Integer(i).scale(0.3).set_color(RED)
        tex_id.move_to(j)
        self.add(tex_id)

def debugPoints(self, obj):
    for i,points in enumerate(obj.get_points()):
        point_id = Integer(i).scale(0.5).set_color(PURPLE_A)
        point_id.move_to(points)
        self.add(point_id)
