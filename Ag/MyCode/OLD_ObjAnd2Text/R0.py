from manimlib.imports import *

def imageObjAndText(imageName,text1,text2):
    pic = ImageMobject(imageName).scale(2)
    picText1 = Text(text1,
                    font='阿里巴巴普惠体 B',
                    color="#308032"
        )\
        .set_height(0.23)\
        .next_to(pic,DOWN,buff=SMALL_BUFF)
    picText2 = Text(text2, 
                    font='阿里巴巴普惠体 B',
                    color=BLACK
        )\
        .set_height(0.28)\
        .next_to(picText1,DOWN,buff=SMALL_BUFF)
    picAndText = Group(pic,picText1,picText2).center()
    pic.rect = RoundedRectangle(
                    corner_radius=0.1,
                    color="#DDDDDD",
                    fill_color = "#DDDDDD",
                    fill_opacity = 1,
                    height=picAndText.get_height()+0.2,
                    width=picAndText.get_width()+0.2
        )
    return Group(pic.rect,pic,picText1,picText2)

def palyALL(self,allParts):
    self.play(
        FadeInFromLarge(allParts[:2]),
        AnimationGroup(
                    Animation(Mobject(),run_time=0.1),
                    FadeInFromDirections(allParts[2]),
                    FadeInFromDirections(allParts[3]),
                    lag_ratio=0.1
            )
        )
    self.wait(15)
    self.play(FadeOutAndShiftDown(allParts))

class R01(Scene):
    def construct(self):
        allParts = imageObjAndText(
                        "R0/1、鲍里斯·约翰逊",
                        "Boris Johnson",
                        "鲍里斯·约翰逊"        
            )
        palyALL(self,allParts)

class R02(Scene):
    def construct(self):
        allParts = imageObjAndText(
                        "R0/2、帕特里克·瓦兰斯",
                        "Patrick Vallance",
                        "帕特里克·瓦兰斯"       
            )
        palyALL(self,allParts)

class R03(Scene):
    def construct(self):
        allParts = imageObjAndText(
                        "R0/3、陈薇院士",
                        "中国工程院院士",
                        "陈薇"       
            )
        palyALL(self,allParts)

class R04(Scene):
    def construct(self):
        allParts = imageObjAndText(
                        "R0/4、麻疹",
                        "Measles",
                        "麻疹"       
            )
        palyALL(self,allParts)

class R05(Scene):
    def construct(self):
        allParts = imageObjAndText(
                        "R0/5、部分疾病的R0值",
                        "The R0 of some diseases",
                        "部分疾病的R0值"       
            )
        palyALL(self,allParts)