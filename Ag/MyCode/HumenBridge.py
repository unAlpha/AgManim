from manimlib.imports import *

def imageObjAnd2Text(imageName,text1,text2):
    pic = ImageMobject(imageName).scale(2)
    picText1 = Text(text1,
                    font='Microsoft YaHei',
                    color="#308032"
        )\
        .set_height(0.23)
    if picText1.get_width() > pic.get_width():
        picText1.set_width(pic.get_width()*0.96)
    picText1.next_to(pic,DOWN,buff=SMALL_BUFF)
    picText2 = Text(text2, 
                    font='Microsoft YaHei',
                    color=BLACK
        )\
        .set_height(0.28)
    if picText2.get_width() > pic.get_width():
        picText2.set_width(pic.get_width()*0.96)
    picText2.next_to(picText1,DOWN,buff=SMALL_BUFF*1.1)
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

def imageObjAnd1Text(imageName,text2,lsh=1):
    pic = ImageMobject(imageName).scale(2)
    picText2 = Text(text2, 
                    font='Microsoft YaHei',
                    color=BLACK,
                    lsh=1.2
        )\
        .set_height(0.28*lsh)
    if picText2.get_width() > pic.get_width():
        picText2.set_width(pic.get_width()*0.96)
    picText2.next_to(pic,DOWN,buff=SMALL_BUFF*1.1)
    picAndText = Group(pic,picText2).center()
    pic.rect = RoundedRectangle(
                    corner_radius=0.1,
                    color="#DDDDDD",
                    fill_color = "#DDDDDD",
                    fill_opacity = 1,
                    height=picAndText.get_height()+0.2,
                    width=picAndText.get_width()+0.2
        )
    return Group(pic.rect,pic,picText2)

def palyALL2(self,allParts):
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

def palyALL1(self,allParts):
    self.play(
        FadeInFromLarge(allParts[:2]),
        AnimationGroup(
                    Animation(Mobject(),run_time=0.1),
                    FadeInFromDirections(allParts[2]),
                    lag_ratio=0.1
            )
        )
    self.wait(15)
    self.play(FadeOutAndShiftDown(allParts))


class HumenBridge01(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "HumenBridge/1冯卡门",
                        "Theodore von Kármán",
                        "西奥多·冯·卡门",     
            )
        palyALL2(self,allParts)

class HumenBridge02(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "HumenBridge/2普朗特",
                        "Ludwig Prandtl",
                        "路德维希·普朗特",
                        
            )
        palyALL2(self,allParts)

class HumenBridge03(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "HumenBridge/3哈依门兹",
                        "Karl Hiemenz",
                        "卡尔·海门兹",
                        
            )
        palyALL2(self,allParts)

class HumenBridge05(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "HumenBridge/5圣克里斯多福",
                        "聖克里斯多福背耶稣过河",
            )
        palyALL1(self,allParts)

class HumenBridge06(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "HumenBridge/6卫星拍摄的大气卡门涡街",
                        "大气中的卡门涡街现象",
            )
        palyALL1(self,allParts)

class HumenBridge09(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "HumenBridge/9科塔马大桥原貌",
                        "塔科马大桥原貌",
            )
        palyALL1(self,allParts)

class HumenBridge11(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "HumenBridge/11水马",
                        "虎门大桥两侧水马",
            )
        palyALL1(self,allParts)