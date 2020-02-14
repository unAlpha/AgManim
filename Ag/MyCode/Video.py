from manimlib.imports import *

class imageAnim(Scene):
    def construct(self):
        Feynman = self.imageObjAndText("Surely_Youre_Joking_cover","Feynman")
        Taniyama = self.imageObjAndText("Taniyama","Taniyama")
        ChenJinRun = self.imageObjAndText("ChenJinRun","ChenJinRun")
        Wiles = self.imageObjAndText("Wiles","Wiles")
        self.rotateAndFade(Feynman,Taniyama,ChenJinRun,Wiles)

    def rotateAndFade(self, *mobs):
        Origin = 6.5*DOWN
        angle = PI/4
        num_mobs = len(mobs)
        for i in range(num_mobs):
            if i==0:
                self.play(
                        FadeInFromAngle(mobs[i],angle = angle,about_point = Origin)
                    )
            self.wait()
            if i < num_mobs-1:
                self.play(
                        FadeOutFromAngle(mobs[i],angle = angle,about_point = Origin),
                        FadeInFromAngle(mobs[i+1],angle = angle, about_point = Origin)
                    )
            if i == num_mobs-1:
                self.play(
                        FadeOutFromAngle(mobs[i],angle = angle,about_point = Origin)
                    )

    def imageObjAndText(self,imageName,text):
        pic = ImageMobject(imageName).scale(2)
        pic.rect = SurroundingRectangle(pic,color=WHITE,stroke_width=8,buff=0)
        picText = Text(text, 
                        font='阿里巴巴普惠体 B',
                        size=0.5).next_to(pic,DOWN)
        return Group(pic,pic.rect,picText)
