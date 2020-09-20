from manimlib.imports import *

def ObjAnd2Text(Obj,text1,text2):
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
                    stroke_opacity=0,
                    fill_color = "#DDDDDD",
                    fill_opacity = 1,
                    height=picAndText.get_height()+0.2,
                    width=picAndText.get_width()+0.2
        )
    return Group(pic.rect,pic,picText1,picText2)

def ObjAnd1Text(Obj,text2):
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
                    color=BLACK
        )\
        .set_height(0.28)\
        .next_to(pic,DOWN,buff=SMALL_BUFF*1.1)
    picAndText = Group(pic,picText2).center()
    pic.rect = RoundedRectangle(
                    corner_radius=0.1,
                    color="#DDDDDD",
                    stroke_opacity=0,
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

def get_coords_from_csv(file_name):
    import csv
    coords = []
    with open(f'{file_name}.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            x,y = row
            coord = [float(x),float(y)]
            coords.append(coord)
    csvFile.close()
    return coords

def get_coords_from_csvdata(file_name):
    import csv
    coords = []
    with open(f'{file_name}.csv', 'r', encoding='UTF-8') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            coords.append(row)
    csvFile.close()
    return coords

def get_points_from_coords(self,coords):
    return [
        # Convert COORDS -> POINTS
        self.coords_to_point(px,py)
        # See manimlib/scene/graph_scene.py
        for px,py in coords
    ]

def get_dots_from_coords(self,coords,radius=0.1):
    points = self.get_points_from_coords(coords)
    dots = VGroup(*[
        Dot(radius=radius).move_to([px,py,pz])
        for px,py,pz in points
        ]
    )
    return dots

class SmoothGraphFromSetPoints(VMobject):
    def __init__(self,set_of_points,**kwargs):
        super().__init__(**kwargs)
        self.set_points_smoothly(set_of_points)

class DiscreteGraphFromSetPoints(VMobject):
    def __init__(self,set_of_points,**kwargs):
        super().__init__(**kwargs)
        self.set_points_as_corners(set_of_points)

class Dujiangyan1(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "Dujiangyan/1亚非大河文明",
                        "四大文明古国及对应的河流"         
            )
        palyALL1(self,allParts)

class Dujiangyan2(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "Dujiangyan/2郑国渠",
                        "郑国渠修建位置"         
            )
        palyALL1(self,allParts)

class Dujiangyan3(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "Dujiangyan/3秦灭巴蜀",
                        "公元前316年 秦灭巴蜀"         
            )
        palyALL1(self,allParts)

class Dujiangyan4(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "Dujiangyan/4都江堰开凿前的地图",
                        "都江堰开凿前的地形图"       
            )
        palyALL1(self,allParts)

class Dujiangyan5(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "Dujiangyan/5二八分沙",
                        "都江堰 二八分沙"       
            )
        palyALL1(self,allParts)

class Dujiangyan6(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "Dujiangyan/6四六分水",
                        "都江堰 四六分水"       
            )
        palyALL1(self,allParts)

class Dujiangyan7(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "Dujiangyan/7都江堰的结构图",
                        "都江堰的结构图"       
            )
        palyALL1(self,allParts)

class Dujiangyan8(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "Dujiangyan/8东汉李冰石像",
                        "1974年出土的李冰石像"       
            )
        palyALL1(self,allParts)

class Dujiangyan9(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "Dujiangyan/9热胀冷缩原理",
                        "采用“热胀冷缩”原理使山石裂开"  
            )
        palyALL1(self,allParts)
