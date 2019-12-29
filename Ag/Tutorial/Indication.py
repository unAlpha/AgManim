
from manimlib.imports import *

class FlashExample(Scene):
    def construct(self):
        mobjects = VGroup(
            Dot(),
            TexMobject("x")
        ).scale(2)
        mobjects.arrange_submobjects(RIGHT,buff=2)

        mobject_or_coord = [
            *mobjects,                    # Mobjects: Dot and "x"
            mobjects.get_right()+RIGHT*2  # Coord
        ]

        colors=[GRAY,RED,BLUE]

        self.add(mobjects)

        for obj,color in zip(mobject_or_coord,colors):
            self.play(Flash(obj,color=color,flash_radius=0.5))

        self.wait(0.3)

class IndicateExample(Scene):
    def construct(self):
        #                     0    1   2
        formula = TexMobject("f(","x",")")
        dot = Dot()

        VGroup(formula,dot)\
                           .scale(3)\
                           .arrange_submobjects(DOWN,buff=3)

        self.add(formula,dot)

        for mob in [formula[1],dot]:
            self.play(Indicate(mob))

        self.wait(0.3)


class FocusOnExample(Scene):
    def construct(self):
        mobjects = VGroup(
            Dot(),
            TexMobject("x")
        )
        mobjects.arrange_submobjects(RIGHT,buff=2)

        mobject_or_coord = [
            *mobjects,                    # Mobjects: Dot and "x"
            mobjects.get_right()+RIGHT*2  # Coord
        ]

        colors=[GRAY,RED,BLUE]

        self.add(mobjects)

        for obj,color in zip(mobject_or_coord,colors):
            self.play(FocusOn(obj,color=color))

        self.wait(0.3)


class ShrinkToCenterExample(Scene):
    def construct(self):
        mobjects = VGroup(
                Square(),
                RegularPolygon(fill_opacity=1),
                TextMobject("Text").scale(2)
            )
        mobjects.scale(1.5)
        mobjects.arrange_submobjects(RIGHT,buff=2)

        self.play(
            *[ShrinkToCenter(mob) for mob in mobjects]
        )

        self.wait()