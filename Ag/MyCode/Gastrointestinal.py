from manimlib.imports import *

def ObjAnd2Text(Obj,text1,text2,sizeHeight=0.28):
    if isinstance(Obj,VMobject):
        pic = Rectangle(
            height = Obj.get_height() + 0.618,
            width = Obj.get_width() + 1.2,
            stroke_color = BLACK,
            fill_color = BLACK,
            fill_opacity = 1,
            )
    else:
        pic = ImageMobject(Obj).scale(2)
    picText1 = Text(text1,
                    color="#308032",         
        )\
        .set_height(sizeHeight-0.05)\
        .next_to(pic,DOWN,buff=SMALL_BUFF)
    picText2 = Text(text2, 
                    color=BLACK,
                    lsh=0.9,
        )\
        .set_height(sizeHeight)\
        .next_to(picText1,DOWN,buff=SMALL_BUFF)
    picAndText = Group(pic,picText1,picText2).center()
    pic.rect = RoundedRectangle(
                    corner_radius=0.1,
                    color="#DDDDDD",
                    stroke_opacity = 0,
                    fill_color = "#DDDDDD",
                    fill_opacity = 1,
                    height=picAndText.get_height()+0.24,
                    width=picAndText.get_width()+0.24
        )
    return Group(pic.rect,pic,picText1,picText2)

def ObjAnd1Text(Obj,text2,sizeHeight=0.28):
    if isinstance(Obj,VMobject):
        pic = Rectangle(
            height = Obj.get_height() + 0.618,
            width = Obj.get_width() + 1.2,
            stroke_color = BLACK,
            fill_color = BLACK,
            fill_opacity = 1,
            )
    else:
        pic = ImageMobject(Obj).scale(2)
    picText2 = Text(text2, 
                    # font='Microsoft YaHei',
                    color=BLACK,
                    lsh=0.9,
        )\
        .set_height(sizeHeight)\
        .next_to(pic,DOWN,buff=SMALL_BUFF*1.1)
    picAndText = Group(pic,picText2).center()
    pic.rect = RoundedRectangle(
                    corner_radius=0.1,
                    color="#DDDDDD",
                    stroke_opacity = 0,
                    fill_color = "#DDDDDD",
                    fill_opacity = 1,
                    height=picAndText.get_height()+0.24,
                    width=picAndText.get_width()+0.24
        )
    return Group(pic.rect,pic,picText2)

def palyALL2(self,allParts):
    self.play(
        FadeInFromLarge(allParts[:2]),
        AnimationGroup(
                    Animation(Mobject(),run_time=0.1),
                    FadeInFrom(allParts[2]),
                    FadeInFrom(allParts[3]),
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
                    FadeInFrom(allParts[2]),
                    lag_ratio=0.1
            )
        )
    self.wait(15)
    self.play(FadeOutAndShiftDown(allParts))


class Gastr1(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "Gastrointestinal/1黑豹剧照",
                        "黑豹剧照"         
            )
        palyALL1(self,allParts)

class Gastr2(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "Gastrointestinal/2发病率",
                        """
                        2015年中国城市和农村地区
                        恶性肿瘤年龄别发病情况
                        """,
                        0.5
            )
        palyALL1(self,allParts)


class Gastr3(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "Gastrointestinal/3死亡率",
                        """
                        2015年中国恶性肿瘤年龄别
                        死亡情况估计
                        """,
                        0.5
            )
        palyALL1(self,allParts)

class Gastr4(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "Gastrointestinal/4上消化道肿瘤发病风险的单因素分析",
                        "上消化道肿瘤发病风险的单因素分析",
            )
        palyALL1(self,allParts)

class Gastr51(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "Gastrointestinal/5.1胃癌演变过程",
                        "胃癌的演变过程",
            )
        palyALL1(self,allParts)

class Gastr52(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "Gastrointestinal/5.2肠癌演变过程",
                        "肠癌的演变过程",
            )
        palyALL1(self,allParts)

class Gastr6(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "Gastrointestinal/6食管癌不同临床分期的五年生存率",
                        "食管癌不同临床分期的五年生存率",
            )
        palyALL1(self,allParts)

class Gastr7(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "Gastrointestinal/7胃癌不同临床分期的五年生存率",
                        "胃癌不同临床分期的五年生存率",
            )
        palyALL1(self,allParts)

class Gastr8(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "Gastrointestinal/8中国韩国日本胃癌早癌检出率对比",
                        "中国、韩国、日本胃癌早癌检出率对比",
            )
        palyALL1(self,allParts)

class Gastr9(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "Gastrointestinal/9医生给自己做胃镜图",
                        "医生给自己做胃镜图",
            )
        palyALL1(self,allParts)

class Gastr10(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "Gastrointestinal/10电子胃镜仪及其使用",
                        "电子胃镜仪及其使用",
            )
        palyALL1(self,allParts)

class Gastr11(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "Gastrointestinal/11胶囊内镜图",
                        "胶囊内镜",
            )
        palyALL1(self,allParts)

class Gastr12(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "Gastrointestinal/12日本胃癌开展率持续提升（每10万人）",
                        "日本胃镜开展率持续提升（每10万人）",
            )
        palyALL1(self,allParts)

class Gastr13(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "Gastrointestinal/13日本胃癌死亡率（每10万人，年均矫正）",
                        "日本胃癌死亡率（每10万人，年均矫正）",
            )
        palyALL1(self,allParts)

class Gastr14(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "Gastrointestinal/14中国与其他国家肠镜开展率对比（每10万人）",
                        "中国与其他国家肠镜开展率对比（每10万人）",
            )
        palyALL1(self,allParts)

class Gastr15(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "Gastrointestinal/15中国与其他国家胃镜开展率对比（每10万人）",
                        "中国与其他国家胃镜开展率对比（每10万人）",
            )
        palyALL1(self,allParts)


script = [
"""（1）胃癌高发地区人群；""",
"""（2）幽门螺杆菌感染者；""",
"""（3）既往患有慢性萎缩性胃炎、胃溃疡、胃息肉、
          手术后残胃、肥厚性胃炎、恶性贫血等胃癌前疾病；""",
"""（4）胃癌患者的一级亲属；""",
"""（5）存在胃癌的其它高危因素，比如：
          高盐、腌制饮食、吸烟、重度饮酒等。"""
]

class Gastr16(Scene):
    def construct(self):
        textList = []
        for txt in script:
            text = Text(txt,size=0.3,lsh=0.4)
            textList.append(text)
        allVG = VGroup(*textList).arrange(DOWN, aligned_edge = LEFT, buff = MED_SMALL_BUFF).shift(0.2*UP)
        allVG.set_color_by_gradient(RED, YELLOW)

        allParts = ObjAnd1Text(
                        allVG,
                        "推荐做胃镜的高危人群"         
            )
        
        self.play(
            FadeInFromLarge(allParts[:2]),
            FadeInFrom(allParts[2])
            )

        self.play(FadeInFromDirections(allVG[0]))
        self.wait(2)
        self.play(FadeInFromDirections(allVG[1]))
        self.wait(2)
        self.play(FadeInFromDirections(allVG[2]))
        self.wait(2)
        self.play(FadeInFromDirections(allVG[3]))
        self.wait(2)
        self.play(FadeInFromDirections(allVG[4]))
        self.wait(5)

        self.play(FadeOutAndShiftDown(allParts),FadeOutAndShiftDown(allVG))


class Gastr18(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "Gastrointestinal/18医生给自己做胃镜图",
                        "医生给自己做肠镜图",
            )
        palyALL1(self,allParts)


class Gastr20(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "Gastrointestinal/20电子胃镜仪导管末端功能",
                        "电子胃镜仪导管末端功能",
            )
        palyALL1(self,allParts)
