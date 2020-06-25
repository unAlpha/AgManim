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


class PrinceRupertsDrop01(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "PrinceRupertsDrop/prince-ruperts-drop",
                        "Prince Rupert's Drop",
                        "鲁珀特之泪",     
            )
        palyALL2(self,allParts)

class PrinceRupertsDrop02(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "PrinceRupertsDrop/glass",
                        "家用车内使用头枕的自救方法",
            )
        palyALL1(self,allParts)