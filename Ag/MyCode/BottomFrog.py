from manimlib.imports import *

def imageObjAndText(imageName,text1,text2):
    pic = ImageMobject(imageName).scale(2)
    picText1 = Text(text1,
                    font='Microsoft YaHei',
                    color="#308032"
        )\
        .set_height(0.23)\
        .next_to(pic,DOWN,buff=SMALL_BUFF)
    picText2 = Text(text2, 
                    font='Microsoft YaHei',
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

class BottomFrog1(Scene):
    def construct(self):
        allParts = imageObjAndText(
                        "BottomFrog/1、门镜",
                        "Peephole",
                        "门镜"        
            )
        palyALL(self,allParts)

class BottomFrog2(Scene):
    def construct(self):
        allParts = imageObjAndText(
                        "BottomFrog/2、门镜图",
                        "View through a peephole",
                        "门镜图像"        
            )
        palyALL(self,allParts)

class BottomFrog3(Scene):
    def construct(self):
        allParts = imageObjAndText(
                        "BottomFrog/3、鱼眼图A",
                        "Fisheye picture A",
                        "鱼眼图A"        
            )
        palyALL(self,allParts)

class BottomFrog4(Scene):
    def construct(self):
        allParts = imageObjAndText(
                        "BottomFrog/4、鱼眼图B",
                        "Fisheye picture B",
                        "鱼眼图B"        
            )
        palyALL(self,allParts)

class BottomFrog5(Scene):
    def construct(self):
        allParts = imageObjAndText(
                        "BottomFrog/5、克劳狄乌斯·托勒密",
                        "Claudius Ptolemaeus",
                        "克劳狄乌斯·托勒密"        
            )
        palyALL(self,allParts)

class BottomFrog6(Scene):
    def construct(self):
        allParts = imageObjAndText(
                        "BottomFrog/6、威理博·斯涅尔",
                        "Willebrord Snellius",
                        "威理博·斯涅耳"        
            )
        palyALL(self,allParts)

class BottomFrog7(Scene):
    def construct(self):
        allParts = imageObjAndText(
                        "BottomFrog/7、克里斯蒂安·惠更斯",
                        "Christiaan Huygens",
                        "克里斯蒂安·惠更斯"        
            )
        palyALL(self,allParts)

class BottomFrog8(Scene):
    def construct(self):
        allParts = imageObjAndText(
                        "BottomFrog/8、笛卡尔",
                        "René Descartes",
                        "勒内·笛卡尔"        
            )
        palyALL(self,allParts)