from manimlib.imports import *

class HealthyLifeYears(Scene):
    def construct(self):
        txt79 = Text("79岁")
        crl = Circle(radius=1.2)
        text1 = Text("发达国家人的寿命:77–90岁",
                    font='宋体',
                    size=0.5
            )
        text2 = Text("发展中国家人的寿命:32–80岁",
                    font='宋体',
                    size=0.5
            )

        tcrlGroup = VGroup(txt79,crl).shift(1*UP)
        VGroup(text1,text2)\
            .arrange(DOWN,aligned_edge = RIGHT,buff=MED_SMALL_BUFF)\
            .next_to(tcrlGroup,2*DOWN)

        # self.add(tcrlGroup,text)
        self.play(FadeInFromLarge(txt79))
        self.play(ShowCreation(crl))
        self.wait()
        self.play(FadeInFromRandomB(text1))
        self.wait()
        self.play(FadeInFromRandomB(text2))
        self.wait()
