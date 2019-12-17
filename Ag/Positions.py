from manimlib.imports import *

class CustomPosition2(Scene):
    def construct(self):
        textM = TextMobject("Text")
        textC = TextMobject("Central text")
        textM.move_to(1*UP+1*RIGHT)
        self.play(Write(textM),Write(textC))
        self.wait(1)
        textM.move_to(1*UP+1*RIGHT) 
        self.play(Write(textM))
        self.wait(3)

class RelativePosition1(Scene):
    def construct(self):
        textM = TextMobject("Text")
        textC = TextMobject("Reference text")
        textM.next_to(textC,LEFT,buff=1) 
        self.play(Write(textM),Write(textC))
        self.wait(3)

class RelativePosition2(Scene):
    def construct(self):
        textM = TextMobject("Text")
        textC = TextMobject("Reference text")
        textM.shift(UP*0.1)
        self.play(Write(textM),Write(textC))
        self.wait(3)

class FlipObject(Scene):
    def construct(self):
        textM = TextMobject("Text")
        textM.flip(UP)
        self.play(Write(textM))
        self.wait(2)

class TextInUpperRightCorner(Scene):
    def construct(self):
        text = TextMobject("Text")
        text.to_edge(UP+RIGHT)
        self.play(Write(text))
        self.wait(3)

class CircleIndicateExample(Scene):
    def construct(self):
        mobjects = VGroup(
            Dot(),
            TexMobject("x")
        ).scale(2)
        mobjects.arrange_submobjects(RIGHT,buff=2)

        self.add(mobjects)
        self.wait(0.2)

        for obj in mobjects:
            self.play(CircleIndicate(obj))