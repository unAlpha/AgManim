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

class IncomeTax01(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "IncomeTax/个人所得税税率",
                        "个人所得税税率"        
            )
        palyALL1(self,allParts)

class IncomeTax02(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "IncomeTax/个税扣除项",
                        "个人所得税扣除项"        
            )
        palyALL1(self,allParts)

class IncomeTax03(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "IncomeTax/个税收入来源",
                        "个人所得税包括项"        
            )
        palyALL1(self,allParts)

class IncomeTax04(Scene):
    def imageObjAnd1Text(self,imageName,text2,lsh=1):
        pic = ImageMobject(imageName).scale(1.2)
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
    def construct(self):
        allParts = self.imageObjAnd1Text(
                        "IncomeTax/应纳税收入",
                        "劳动报酬应纳税收入"        
            )
        palyALL1(self,allParts)

class IncomeTax05(Scene):
    def imageObjAnd1Text(self,imageName,text2,lsh=1):
        pic = ImageMobject(imageName).scale(1.5)
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
    def construct(self):
        allParts = self.imageObjAnd1Text(
                        "IncomeTax/应纳税预扣",
                        "劳动报酬应纳税预扣"        
            )
        palyALL1(self,allParts)

class IncomeTax06(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "IncomeTax/张三每个月的预缴个税",
                        "张三每个月的预缴个税"        
            )
        palyALL1(self,allParts)

class IncomeTax07(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "IncomeTax/综合所得额",
                        "综合所得额包括项"        
            )
        palyALL1(self,allParts)

class IncomeTax08(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "IncomeTax/奖金计税方式选择",
                        "奖金计税方式选择"        
            )
        palyALL1(self,allParts)

class IncomeTax09(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "IncomeTax/申报导入",
                        "申报导入"        
            )
        palyALL1(self,allParts)

class IncomeTax10(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "IncomeTax/填写扣除",
                        "专项扣除填写"        
            )
        palyALL1(self,allParts)


