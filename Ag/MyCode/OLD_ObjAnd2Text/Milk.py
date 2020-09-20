from manimlib.imports import *

def imageObjAnd2Text(imageName,text1,text2):
    pic = ImageMobject(imageName).scale(2)
    picText1 = Text(text1,
                    color="#308032"
        )\
        .set_height(0.23)\
        .next_to(pic,DOWN,buff=SMALL_BUFF)
    picText2 = Text(text2, 
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

def imageObjAnd1Text(imageName,text2):
    pic = ImageMobject(imageName).scale(2)
    picText2 = Text(text2, 
                    # font='Microsoft YaHei',
                    color=BLACK
        )\
        .set_height(0.28)\
        .next_to(pic,DOWN,buff=SMALL_BUFF*1.1)
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


class Milk1(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Milk/1、巴氏奶制造运输流程",
                        "巴氏奶制造运输流程"        
            )
        palyALL1(self,allParts)

class Milk2(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "Milk/2、巴斯德",
                        "Louis Pasteur",
                        "路易·巴斯德"        
            )
        palyALL2(self,allParts)

class Milk3(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Milk/3、不同物质含钙量",
                        "不同物质的含钙量"        
            )
        palyALL1(self,allParts)

class Milk4(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Milk/4、乳糖耐受和乳糖不耐受原理",
                        "乳糖耐受与不耐受原理"        
            )
        palyALL1(self,allParts)

class Milk5(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "Milk/5、乳酸菌",
                        "Lactic Acid Bacteria",
                        "乳酸菌"        
            )
        palyALL2(self,allParts)

class Milk6(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Milk/6、骨质疏松图",
                        "骨质疏松的骨骼"        
            )
        palyALL1(self,allParts)

class Milk7(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Milk/7、世界各国乳糖不耐受比例",
                        "世界各国乳糖不耐受比例"        
            )
        palyALL1(self,allParts)

class Milk8(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Milk/8、钙摄入量建议图",
                        "钙摄入量建议图"        
            )
        palyALL1(self,allParts)

class Milk9(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Milk/9、骨量",
                        "不同时期人的骨量"        
            )
        palyALL1(self,allParts)

class Milk10(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Milk/10、世界各国奶制品消费量",
                        "世界各国奶制品消费量"        
            )
        palyALL1(self,allParts)