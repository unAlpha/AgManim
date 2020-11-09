from manimlib.imports import *

class DeferentandEpicycle(Scene):
    def construct(self):
        self.t_offset=0
        orbit=Circle(radius=2.5,color=GREEN,stroke_width=8.32)
        orbitMin=Circle(radius=1,color=RED)
        planet=Dot(radius=0.2)
        earth = ImageMobject("teach/earth").scale(0.832)
        cross = Cross(orbit).scale(0.03).set_color(GRAY)
        earth.move_to(DOWN*0.5)
        text1=Text("均轮", color=GREEN)
        text1.to_corner(UR).shift(1.5*LEFT)
        text2=Text("本轮", color=RED)
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

class Coin1A(Scene):
    def construct(self):
        coinR1 = 1.2
        coin2 = Circle(radius = coinR1,stroke_width=3.82,color=RED)
        coin = Group(coin2,Text("1元",size=1))
        line1 = Line(-RIGHT*coinR1*PI,RIGHT*coinR1*PI)
        coin.move_to(line1.point_from_proportion(0))
        
        lines = []
        for i in range(1):
            for j in range(31):
                target_ij = Line(ORIGIN,UR,stroke_width=2)
                target_ij.scale(0.4)
                target_ij.shift(np.array([-5.1+j*0.3,-2+i*2,0]))
                lines.append(target_ij)

        line2 = Line(-RIGHT*coinR1*4,RIGHT*coinR1*4).move_to(coinR1*DOWN)

        self.t_offset=0
        def update_track(mob,dt):
            rate=dt*0.2
            if self.t_offset>=1:
                rate = 0
            mob.move_to(line1.point_from_proportion(self.t_offset + rate))
            mob.rotate(-rate*PI,about_point = line1.point_from_proportion(self.t_offset + rate))
            self.t_offset += rate

        coin.add_updater(update_track)
        self.add(coin,line2,*lines)
        self.wait(8)

class Coin1B(Scene):
    def construct(self):
        coinR1 = 1.2
        coin2 = Circle(radius = coinR1,stroke_width=3.82,color=RED)
        coin = VGroup(coin2,Text("F",size=1.618))
        line1 = Line(-RIGHT*coinR1*PI/2,RIGHT*coinR1*PI/2)
        coin.move_to(line1.point_from_proportion(0))
        
        lines = []
        for i in range(1):
            for j in range(31):
                target_ij = Line(ORIGIN,UR,stroke_width=2)
                target_ij.scale(0.4)
                target_ij.shift(np.array([-5.1+j*0.3,-2+i*2,0]))
                lines.append(target_ij)

        line2 = Line(-RIGHT*coinR1*4,RIGHT*coinR1*4).move_to(coinR1*DOWN)
        coin.save_state()
        def update_rotate_move(mob,alpha):
            coin.restore()
            coin.move_to(line1.point_from_proportion(alpha))
            coin.rotate(-PI*alpha)

        self.play(ShowCreation(line2),Write(coin))
        self.add(*lines)
        self.wait()
        self.play(
                UpdateFromAlphaFunc(coin,update_rotate_move),
                run_time=4)
        self.wait()

class Coin2A(Scene):
    def construct(self):
        coin1 = Circle(radius = 1.2,stroke_width=4.5,color=WHITE)
        coin2 = VGroup(Circle(radius = 1.2,stroke_width=3.82),Text("F",size=1.618))
        path = Circle(radius = 2.4).rotate(PI)
        coin2.next_to(coin1,UP*0.01)
        coin2.save_state()
        def update_rotate_move(mob,alpha):
            coin2.restore()
            # alpha是把这个物体从0-1进行拆分
            coin2.move_to(path.point_from_proportion(-alpha/2+0.75))
            coin2.rotate(-TAU*alpha)
        self.play(ShowCreation(coin1),Write(coin2))
        self.wait()
        self.play(
                # Blue square
                UpdateFromAlphaFunc(coin2,update_rotate_move),
                run_time=4
            )
        self.wait()

class RotateWithPath(Scene):
    def construct(self):
        square1, coin2 = VGroup(
                Square(color=RED), Square(color=BLUE)
            ).scale(0.5).set_x(-5)

        path = Line(LEFT*5,RIGHT*5,stroke_opatity=0.5)
        path.points[1:3] += UP*2

        coin2.save_state()
        def update_rotate_move(mob,alpha):
            coin2.restore()
            coin2.move_to(path.point_from_proportion(alpha))
            coin2.rotate(3*PI*alpha)

        self.add(square1,coin2,path)
        self.play(
                # Red square
                # 目标复用，只会有一个效果
                MoveAlongPath(square1,path),
                Rotate(square1,2*PI/3,about_point=square1.get_center()),
                # Blue square
                UpdateFromAlphaFunc(coin2,update_rotate_move),
                run_time=4
            )
        self.wait()

