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

class keju01(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "keju/1、分封制金字塔",
                        "分封制金字塔", 
            )
        palyALL1(self,allParts)

class keju02(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "keju/2、隋文帝",
                        "隋文帝", 
            )
        palyALL1(self,allParts)

class keju03(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "keju/3、隋炀帝",
                        "隋炀帝", 
            )
        palyALL1(self,allParts)

class keju04(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "keju/4、范仲淹",
                        "范仲淹", 
            )
        palyALL1(self,allParts)

class keju05(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "keju/5、王安石",
                        "王安石", 
            )
        palyALL1(self,allParts)

class keju06(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "keju/6、司马光",
                        "司马光", 
            )
        palyALL1(self,allParts)

class keju07(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "keju/7、欧阳修",
                        "欧阳修", 
            )
        palyALL1(self,allParts)

class keju08(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "keju/8、朱元璋",
                        "朱元璋", 
            )
        palyALL1(self,allParts)

class keju09(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "keju/9、北京贡院",
                        "北京贡院", 
            )
        palyALL1(self,allParts)

class keju10(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "keju/10、慈禧太后",
                        "慈禧太后", 
            )
        palyALL1(self,allParts)

class keju11(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "keju/11、光绪帝",
                        "光绪帝", 
            )
        palyALL1(self,allParts)

class keju12(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "keju/12、康有为",
                        "康有为", 
            )
        palyALL1(self,allParts)

class keju13(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "keju/13、梁启超",
                        "梁启超", 
            )
        palyALL1(self,allParts)

class Txt1(Scene):
    def construct(self):
        txt = (
            "富家不用买良田，书中自有千钟粟。",
            "安居不用架高堂，书中自有黄金屋。",
            "出门无车毋须恨，书中有马多如簇。",
            "娶妻无媒毋须恨，书中有女颜如玉。",
            "男儿欲遂平生志，五经勤向窗前读。"
            )
        
        txtT = []
        for i in range(5):
            txtTmp = Text(txt[i])
            txtT.append(txtTmp)
        TxtGroup=VGroup(*txtT).arrange_submobjects(DOWN,buff=0.4)

        self.play(LaggedStartMap(Write,[obj for obj in TxtGroup],lag_ratio=1.5),run_time=10)
        self.wait()

class Txt2(Scene):
    def construct(self):
        txt = ("""
                    八股文是指文章的八个部分，文体有
            固定格式：由破题、承题、起讲、入题、
            起股、中股、后股、束股八部分组成，题
            目一律出自四书五经中的原文。""")
        txtTmp = Text(txt,lsh=1)
 
        self.play(Write(txtTmp))
        self.wait()

class Txt3(Scene):
    def construct(self):
        txt = (
            "离离原上草，一岁一枯荣。",
            "野火烧不尽，春风吹又生。",
            "远芳侵古道，晴翠接荒城。",
            "又送王孙去，萋萋满别情。",
            )
        
        txtT = []
        for i in range(4):
            txtTmp = Text(txt[i])
            txtT.append(txtTmp)
        TxtGroup=VGroup(*txtT).arrange_submobjects(DOWN,buff=0.4)

        self.play(LaggedStartMap(Write,[obj for obj in TxtGroup],lag_ratio=1.5),run_time=10)
        self.wait()
