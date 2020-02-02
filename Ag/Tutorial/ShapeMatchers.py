from manimlib.imports import *

class DashedRectangleScene(Scene):
    def construct(self):
        vp = DashedRectangle()
        self.play(ShowCreation(vp))
        self.wait()

class SurroundingDashedRectangleScene(Scene):
    def construct(self):
        tex = TextMobject("彭小宝")
        vp = SurroundingDashedRectangle(tex,num_dashes=36)
        self.add(tex)
        self.play(ShowCreation(vp))
        self.wait()

class FreehandDrawScene(Scene):
    def construct(self):
        line = Line()
        vp = FreehandDraw(line,partitions=50)
        self.add(line)
        self.play(ShowCreation(vp))
        self.wait()

class FreehandRectangleScene(Scene):
    def construct(self):
        tex = TextMobject("我可爱的彭小宝",color=YELLOW)
        vp = FreehandRectangle(tex,
                margin=0.2,
                partitions=50,
                color=RED,
                fill_color=BLUE,
                fill_opacity=1.0
                )
        self.play(FadeInFromLarge(vp),FadeInFromRandom(tex[0]))
        self.wait()

class ZigZagScene(Scene):
    def construct(self):
        tex = TextMobject("彭小宝")
        vp = ZigZag(tex,margin=0.1,partitions=10,color=RED)
        self.add(tex)
        self.play(ShowCreation(vp))
        self.wait()

class MeasureDistanceScene(Scene):
    def construct(self):
        line = Line()
        vp = MeasureDistance(line)
        vp.add_tips()
        vp.add_text("1m",buff=1)
        self.add(line)
        self.play(ShowCreation(vp))
        self.wait()

class RectanglePatternScene(Scene):
    def construct(self):
        line = Square()
        vp = RectanglePattern(2)
        self.add(line)
        self.play(ShowCreation(vp))
        self.wait()