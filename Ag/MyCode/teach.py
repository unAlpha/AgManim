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
        allParts = imageObjAnd1Text(
                        "teach/飞机投弹A",
                        "以飞机为参照的投弹轨迹",
            )
        palyALL1(self,allParts)

class PrinceRupertsDrop02(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "teach/飞机投弹B",
                        "以地面为参照的投弹轨迹",
            )
        palyALL1(self,allParts)


class PrinceRupertsDrop03(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "teach/伽利略·伽利莱",
                        "Galileo Galilei",
                        "伽利略·伽利莱",     
            )
        palyALL2(self,allParts)

class PrinceRupertsDrop04(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "teach/克劳狄乌斯·托勒密",
                        "Claudius Ptolemaeus",
                        "克劳狄乌斯·托勒密",     
            )
        palyALL2(self,allParts)

class PrinceRupertsDrop05(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "teach/尼古拉·哥白尼",
                        "Nicolaus Copernicus",
                        "尼古拉·哥白尼",     
            )
        palyALL2(self,allParts)

class PrinceRupertsDrop06(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "teach/约翰内斯·开普勒",
                        "Johannes Kepler",
                        "约翰内斯·开普勒",     
            )
        palyALL2(self,allParts)

class PrinceRupertsDrop07(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "teach/球坐标系",
                        "Spherical Coordinate System",
                        "球坐标系",     
            )
        palyALL2(self,allParts)

class PrinceRupertsDrop08(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "teach/柱坐标系",
                        "Cylindrical Coordinate system",
                        "柱坐标系",     
            )
        palyALL2(self,allParts)

class DeferentandEpicycle(Scene):
    def construct(self):
        self.t_offset=0
        orbit=Circle(radius=2.5,color=GREEN,stroke_width=8.32)
        orbitMin=Circle(radius=1,color=RED)
        planet=Dot(radius=0.2)
        earth = ImageMobject("teach/earth").scale(0.832)
        cross = Cross(orbit).scale(0.03).set_color(GRAY)
        earth.move_to(DOWN*0.5)
        text1=Text("均轮",color=GREEN)
        text1.to_corner(UR).shift(1.5*LEFT)
        text2=Text("本轮",color=RED)
        text2.next_to(text1,DOWN)
        orbitMin.move_to(orbit.point_from_proportion(0))
        planet.move_to(orbitMin.point_from_proportion(0))

        def update_planet(mob,dt):
            rate=dt*0.1
            # 0.8为一圈的百分比
            if self.t_offset>2:
                rate = 0
            mob.move_to(orbitMin.point_from_proportion(((self.t_offset + rate))%1))
            self.t_offset += rate

        planet.add_updater(update_planet)
        self.add(cross)
        self.play(FadeInFromLarge(earth))
        self.play(Write(orbit),ShowCreation(orbitMin))
        self.play(Write(text1),Write(text2))
        self.add(planet)
        self.play(Rotate(orbitMin,PI*10/3,about_point=ORIGIN,rate_func=linear,run_time=20))
        self.wait()
