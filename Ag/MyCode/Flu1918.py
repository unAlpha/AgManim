from manimlib.imports import *

def imageObjAnd2Text(imageName,text1,text2):
    pic = ImageMobject(imageName).scale(2)
    picText1 = Text(text1,
                    color="#308032"
        )\
        .set_height(0.23)
    if picText1.get_width() > pic.get_width():
        picText1.set_width(pic.get_width()*0.96)
    picText1.next_to(pic,DOWN,buff=SMALL_BUFF)
    picText2 = Text(text2, 
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
                    # font='Microsoft YaHei',
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

class Flu1(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Flu1918/1918费城大游行",
                        "1918年费城大游行"        
            )
        palyALL1(self,allParts)

class Flu2(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Flu1918/1918年流感期间西雅图电车乘务员拒绝没戴口罩的乘客",
                        """
                        1918年流感期间的西雅图
                        电车乘务员拒绝没戴口罩的乘客
                        """
                        ,2
            )
        self.play(
            FadeInFromLarge(allParts[:2]),
            AnimationGroup(
                        Animation(Mobject(),run_time=1),
                        FadeInFromRandomB(allParts[2]),
                        lag_ratio=0.5
                )
            )
        self.wait(15)
        self.play(FadeOutAndShiftDown(allParts))

class Flu3(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "Flu1918/1918年流行病的流感死亡率年龄分布与正常流行病之间的差异",
                        "美国每个年龄组的100,000人死亡",
                        "1918年流感与正常流行病之间的死亡率差异"
            )
        palyALL2(self,allParts)

class Flu4(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Flu1918/1951年赫尔汀和队友",
                        "1951年赫尔汀和其队友"        
            )
        palyALL1(self,allParts)


class Flu5(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Flu1918/巴黎和会中的领导人",
                        "巴黎和会中的领导人"        
            )
        palyALL1(self,allParts)

class Flu6(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Flu1918/戴口罩的西雅图警察",
                        "戴口罩的西雅图警察"        
            )
        palyALL1(self,allParts)

class Flu7(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "Flu1918/德国皇帝威廉二世",
                        "Wilhelm II",
                        "德国皇帝威廉二世"
            )
        palyALL2(self,allParts)

class Flu8(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Flu1918/护士正在处理尸体",
                        "护士正在处理尸体"        
            )
        palyALL1(self,allParts)

class Flu9(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "Flu1918/甲型流感病毒",
                        "Influenza A virus",
                        "甲型流感病毒"
            )
        palyALL2(self,allParts)

class Flu10(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Flu1918/堪萨斯州赖利堡福斯顿军营中的患病士兵",
                        "堪萨斯州赖利堡芬斯顿军营中的患病士兵"        
            )
        palyALL1(self,allParts)

class Flu11(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Flu1918/流感病毒的感染路径",
                        "流感病毒的感染路径"        
            )
        palyALL1(self,allParts)

class Flu12(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Flu1918/流感病毒中片段化的RNA",
                        "流感病毒中片段化的RNA"        
            )
        palyALL1(self,allParts)

class Flu13(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "Flu1918/美国红十字会医护倾向于在1918年奥克兰市政厅内设立的临时病房中对患者进行流感治疗",
                        "在1918年奥克兰市政厅内设立的临时病房",
                        "美国红十字会设立临时病房"
            )
        palyALL2(self,allParts)

class Flu14(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Flu1918/美国人均预期寿命",
                        "美国人均预期寿命"        
            )
        palyALL1(self,allParts)

class Flu15(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "Flu1918/美国总统威尔逊",
                        "Thomas Woodrow Wilson",
                        "美国总统威尔逊"
            )
        palyALL2(self,allParts)

class Flu16(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Flu1918/齐默尔曼电报",
                        "齐默尔曼电报"
            )
        palyALL1(self,allParts)

class Flu17(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Flu1918/三波流感中英国病死率",
                        "三波流感中 英国病死率"
            )
        palyALL1(self,allParts)

class Flu18(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Flu1918/陶本伯格和赫尔汀",
                        "陶本伯格和赫尔汀"
            )
        palyALL1(self,allParts)

class Flu19(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "Flu1918/西班牙国王阿方索十三世",
                        "Alfonso XIII",
                        "西班牙国王 阿方索十三世"
            )
        palyALL2(self,allParts)

class Flu20(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "Flu1918/英国首相大卫·劳合·乔治",
                        "David Lloyd George",
                        "英国首相 大卫·劳合·乔治"           
            )
        palyALL2(self,allParts)

class Flu21(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Flu1918/重建的西班牙流感病毒",
                        "重建的西班牙流感病毒"         
            )
        palyALL1(self,allParts)

class Flu22(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "Flu1918/乔治五世",
                        "George V",
                        "英国国王 乔治五世" 
            )
        palyALL2(self,allParts)