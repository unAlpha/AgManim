from manimlib.imports import *

class DrawAnAxis(Scene):
    CONFIG = { "plane_kwargs" : { 
        "x_line_frequency" : 0.5,
        "y_line_frequency" : 0.5
        }
    }

    def construct(self):
        my_plane = NumberPlane(**self.plane_kwargs)
        my_plane.add(my_plane.get_axis_labels())

        self.play(Write(my_plane, run_time = 2))


class NaturalNumberCube(Scene):
    def construct(self):
        equal = TextMobject("=", color=RED)
        eq_left1 = TextMobject("$1^3+2^3+3^3+\\dots+n^3$", color = GREEN)
        eq_right1= TextMobject("$(1+2+3+\\dots+n)^2$", color=YELLOW)

        eq_left2 = TextMobject("$\\Sigma_{i=1}^{n} i^{3}$", color=GREEN)
        eq_right2= TextMobject("$(\\Sigma_{i=1}^{n} i)^{2}$", color=YELLOW)
        equation2= VGroup(equal,eq_left2,eq_right2)

        eq_left1.next_to(equal,LEFT)
        eq_right1.next_to(equal,RIGHT)
        eq_left2.next_to(equal,LEFT)
        eq_right2.next_to(equal,RIGHT)

        self.play(FadeIn(equal),FadeIn(eq_left1),FadeIn(eq_right1))
        self.wait(1)
        self.play(ReplacementTransform(eq_left1,eq_left2))
        self.play(ReplacementTransform(eq_right1,eq_right2))
        self.wait(1)
        self.play(ApplyMethod(equation2.scale,2.0))
        self.wait(1)

class SunAndPlanet(ThreeDScene):
    def construct(self):
        rSun = 1.6
        rPlanet = 0.4
        rOrb = 3.5
        sun = Sphere(radius=rSun)
        planet = Sphere(radius=rPlanet)
        orbit = Circle(radius=rOrb)
        planet.shift(UP*rOrb)
        system = VGroup(sun, orbit, planet)
        system.shift(DOWN*2+LEFT*1.2)

        FVector = Vector(np.array([0,rSun-rOrb,0]), color=YELLOW)
        FVector.next_to(planet, DOWN*0.6)
        FFomula = TexMobject("\\vec{F}=G m_1 m_2\\frac{(\\vec{r_1}-\\vec{r_2})}{r^3}", color=RED)
        FFomula.rotate_about_origin(PI/2)
        FFomula.next_to(FVector,LEFT*0.4)

        self.set_camera_orientation(phi=10)
        self.play(ShowCreation(orbit))
        self.play(FadeIn(planet), FadeIn(sun))
        self.wait(1)
        self.play(ShowCreation(FVector))
        self.play(Write(FFomula))
        self.wait(1)


class BasicShapes(Scene):
    def construct(self):
        #make object
        annulus1 = Annulus(inner_radius=.4, outer_radius=1, color=BLUE)
        square1 = Square(color=ORANGE, fill_color=ORANGE, fill_opacity=.5)
        rect1 = Rectangle(height=3.2,width=1.2,color=PINK, fill_color=PINK, fill_opacity=0.5)

        line1 = Line(np.array([0,3.6,0]),np.array([0,2,0]),color=BLUE)
        line2 = Line(np.array([-0.98,2,0]),np.array([-1,-1,0]),color=BLUE)
        line3 = Line(np.array([0.98,2,0]),np.array([1,0.5,0]),color=BLUE)

        #position
        annulus1.shift(UP*2)
        square1.shift(LEFT+DOWN*2)
        rect1.shift(RIGHT+DOWN*(3.2/2-0.5))

        #Showing object
        self.add(line1)
        self.play(GrowFromCenter(annulus1))
        self.wait(0.5)
        self.play(FadeIn(line2),FadeIn(line3))
        self.wait(0.5)
        self.play(FadeInFromDown(square1))
        self.play(FadeInFromDown(rect1))
        self.wait()


class Shoot(Scene):
    def construct(self):
        #make aim_scope
        circle1 = Circle(color=BLUE)
        circle2 = Circle(color=RED, fill_color=RED, fill_opacity=1)
        circle2.scale(0.1)
        line1 = Line(np.array([-1,0,0]),np.array([1,0,0]),color=RED)
        line2 = Line(np.array([0,1,0]),np.array([0,-1,0]),color=RED)
        aim_scope = VGroup(circle1,circle2,line1,line2)

        #make target
        target_list = []
        for i in range(3):
            for j in range(5):
                target_ij = Circle(color=YELLOW, fill_color=YELLOW, fill_opacity=0.4)
                target_ij.scale(0.4)
                target_ij.shift(np.array([-4+j*2,-2+i*2,0]))
                self.play(FadeIn(target_ij),run_time=0.2)
                target_list.append(target_ij)
        self.wait(1)

        #move&shoot animation
        def shoot_ij(i,j):
            target_ij=target_list[j+i*5]
            self.play(ApplyMethod(aim_scope.next_to, target_ij, 0))
            self.play(ApplyMethod(target_ij.set_fill, GREY), ApplyMethod(target_ij.set_color, GREY))
            ij = TexMobject("(%d,%d)" % (i,j),color=GREY)
            ij.next_to(target_ij, DOWN)
            self.play(Write(ij))
            self.wait(1)
            return 0
        
        self.add(aim_scope)
        self.play(ApplyMethod(aim_scope.shift, DOWN*3+LEFT*6.1))
        shoot_ij(0,1)
        shoot_ij(2,0)
        shoot_ij(1,3)
        shoot_ij(0,0)
        shoot_ij(2,4)


class LoveDeathAndRobots(Scene):
    def construct(self):
        #make object
        circle1 = Circle(color=RED, fill_color=RED,fill_opacity=0.5)
        circle2 = Circle(color=RED, fill_color=RED,fill_opacity=0.5)
        square1 = Square(color=RED, fill_color=RED,fill_opacity=0.5)
        loveShape = VGroup(circle1, circle2,square1)

        rect1 = Rectangle(height=0.8, width=4, color=RED, fill_color=RED,fill_opacity=0.5)
        rect2 = Rectangle(height=0.8, width=4, color=RED, fill_color=RED,fill_opacity=0.5)
        death = VGroup(rect1, rect2)

        square2 = Square(color=RED, fill_color=RED,fill_opacity=0.5)
        square2.scale(1.6)
        c1 = Circle(color=RED, fill_color=BLACK,fill_opacity=0.5)
        c2 = Circle(color=RED, fill_color=BLACK,fill_opacity=0.5)
        c1.scale(0.45)
        c2.scale(0.45)
        robots = VGroup(square2, c1, c2)

        line1 = Line(np.array([-6,-2.4,0]), np.array([6,-2.4,0]), color=RED)
        line1.set_height(0.2)

        text1 = TextMobject("LOVE\nDEATH\n+\nROBOTS", color=RED)
        text1.scale(1.8)

        groupShape = VGroup(loveShape, death, robots)
        groupAll = VGroup(loveShape, death, robots, line1, text1)

        #position
        circle1.shift((UP+LEFT)*np.sqrt(2)/2)
        circle2.shift((UP+RIGHT)*np.sqrt(2)/2)
        square1.rotate(np.pi/4)

        rect1.rotate(np.pi/4)
        rect2.rotate(-np.pi/4)

        c1.shift(np.array([-0.72,0.6,0]))
        c2.shift(np.array([0.72,0.6,0]))
        robots.shift(RIGHT*4)

        text1.shift(DOWN*2.5)

        self.play(ShowCreation(circle1),ShowCreation(circle2),ShowCreation(square1))
        self.wait(1)
        self.play(ApplyMethod(loveShape.shift, LEFT*4))
        self.wait(1)

        self.play(ShowCreation(rect1),ShowCreation(rect2))
        self.wait(1)

        self.play(ShowCreation(square2))
        self.play(ShowCreation(c1),ShowCreation(c2))
        self.wait(1)

        self.play(ApplyMethod(groupShape.set_opacity,1))
        self.wait(1)

        self.play(ShowCreation(line1))
        self.wait(1)
        self.play(Transform(line1,text1))
        self.wait(1)
        self.play(ApplyMethod(groupAll.shift, UP*0.5))
        self.wait(1)
        

class TextLuXun(Scene):
    def construct(self):
        quote1 = TextMobject("使用Manim制作数学动画很有意思")
        quote1.set_color(RED)
        quote1.to_edge(UP)
        quote2 = TextMobject("Making animation by manim is funny.")
        quote2.set_color(BLUE)
        author = TextMobject("-鲁迅", color=PINK)

        author.next_to(quote1.get_corner(DOWN+RIGHT),DOWN)

        self.add(quote1)
        self.add(author)
        self.wait(2)
        self.play(Transform(quote1,quote2),ApplyMethod(author.move_to,quote2.get_corner(DOWN+RIGHT)+DOWN))

        self.play(ApplyMethod(author.scale,1.5))
        self.wait(1)
        author.match_color(quote2)
        self.wait(1)
        self.play(FadeOut(quote1),FadeOut(author))
        self.wait()
        

class LabelShape(Scene):
    def construct(self):
        #side_length 边长
        square1 = Square(side_length=5, fill_color=BLUE, fill_opacity=0.5)

        label1 = TextMobject("扭一下身体")
        label1.bg = BackgroundRectangle(label1, fill_opacity=1)
        #VGroup的参数顺序就是前后的叠层顺序
        label1_group = VGroup(label1.bg, label1)
        label1_group.rotate(TAU/8)

        label2 = TextMobject("加个边框", color=BLACK)
        label2.bg = SurroundingRectangle(label2, color=BLUE, fill_color=RED, fill_opacity=1)
        label2_group = VGroup(label2.bg, label2)
        label2_group.next_to(label1_group,DOWN)

        label3 = TextMobject("变成彩虹")
        label3.set_color_by_gradient(RED, ORANGE, YELLOW, BLUE, PURPLE)
        label3.to_edge(DOWN)

        self.add(square1)
        self.play(FadeIn(label1_group))
        self.play(FadeIn(label2_group))
        self.play(FadeIn(label3))
        self.wait(1)


class LatexTmp(Scene):
    def construct(self):
        title = TextMobject("This is some \\LaTeX")
        basel = TexMobject(
            "\\sum_{n=1}^\\infty "
            "\\frac{1}{n^2} = \\frac{\\pi^2}{6}"
        )
        #使basel在title下面
        VGroup(title, basel).arrange(DOWN)
        self.play(
            Write(title),
            FadeInFrom(basel, UP)
        )
        self.wait()