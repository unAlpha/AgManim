from manimlib.imports import *

class ep051(Scene):
    def construct(self):
        text1 = Text("整数：1、2、3、4、...", font='阿里巴巴普惠体 B',size=0.5).move_to(1.5*LEFT)
        numberline1=NumberLine(x_min=0,
                                x_max=5,
                                include_tip=True,
                                tick_size=0.1,
                                tick_frequency=0.5,
                                color=WHITE
                      ).move_to(DOWN)
        self.play(ShowCreation(text1),ShowCreation(numberline1),run_time=3)
        self.wait(5)

class ep052(Scene):
    def construct(self):
        text1 = Text("...")
        text2 = Text("...")
        x=-4
        y=0
        num=2
        cl=2
        scl=0.8
        bead1=ImageMobject("bead").move_to(np.array([x,y+2,0]))
        copperCoin1=ImageMobject("copperCoin").move_to(np.array([x,y,0]))
        bead1.scale(scl)
        copperCoin1.scale(scl)
        self.play(FadeIn(bead1),FadeIn(copperCoin1))
        self.wait(2)
        for i in range(num):
            bead=ImageMobject("bead")
            copperCoin=ImageMobject("copperCoin")
            bead.scale(scl)
            copperCoin.scale(scl)
            bead.move_to(np.array([cl*(i+1)+x,y+2,0]))
            copperCoin.move_to(np.array([cl*(i+1)+x,y,0]))
            self.play(FadeInFrom(bead,RIGHT),FadeInFrom(copperCoin,RIGHT),run_time=2)
            if i==(num-1):
                text1.next_to(bead,RIGHT)
                text2.next_to(copperCoin,RIGHT)
                self.play(ShowCreation(text1),ShowCreation(text2))
        self.wait(10)

class ep053(Scene):
    def construct(self):
        text1 = Text("整数：1、2、3、4、...", font='阿里巴巴普惠体 B',size=0.5)
        text2 = Text("偶数：2、4、6、8、...", font='阿里巴巴普惠体 B',size=0.5).move_to(DOWN)
        self.play(ShowCreation(text1),ShowCreation(text2),run_time=2)
        self.wait(8)

class ep054(Scene):
    def construct(self):
        text1 = Text("非负整数：0、1、2、3、...", font='阿里巴巴普惠体 B',size=0.5)
        text2 = Text("正整数：1、2、3、4、...", font='阿里巴巴普惠体 B',size=0.5)\
            .move_to(DOWN).align_to(text1,RIGHT)
        self.play(ShowCreation(text1),ShowCreation(text2),run_time=2)
        self.wait(10)

class ep055(Scene):
    def construct(self):
        text1 = TexMobject("\\frac{1}{1}\\ \\",
                           "\\frac{1}{2},",
                           "\\frac{2}{1}\\ \\",
                           "\\frac{1}{3},",
                           "\\frac{2}{2},",
                           "\\frac{3}{1}\\ \\",
                           "..."
                           )
        text2 = TexMobject("1",
                           "2,",
                           "3",
                           "4,",
                           "5,",
                           "6",
                           "...")
        for i in range(6):
            text2[i].next_to(text1[i],DOWN)
        text2[6].next_to(text1[6],3*DOWN)
        self.play(ShowCreation(text1[0]),run_time=2)
        self.wait(3)
        self.play(ShowCreation(text1[1:3]),run_time=2)
        self.wait(3)
        self.play(ShowCreation(text1[3:6]),run_time=2)
        self.wait(3)
        self.play(ShowCreation(text1[6]),run_time=2)
        self.wait(10)
        self.play(ShowCreation(text2),run_time=2)
        self.wait(10)

class ep056(Scene):
    def construct(self):
        text1 = TextMobject(
            "\\small$$\\frac{1}{1}\\ \\ \\frac{1}{2},\\frac{2}{1}\\ \\ \\frac{1}{3},\\frac{2}{2},\\frac{3}{1}\\ \\ ...$$")
        text2 = TextMobject(
            "\\textbf{$$1 2,3 4,5,6 ...$$}",)
        self.add(text1)
        self.add(text2.move_to(DOWN))
        self.wait(5)

class ep031(Scene):
    def construct(self):
        text = TexMobject("10000000000…00","=","{10","^{63}}")
        text[0].set_color(RED)
        text[1].set_color(YELLOW)
        text[2].set_color(GREEN)
        text[3].set_color(ORANGE)
        brace63=Brace(text[0],DOWN,buff = 3*SMALL_BUFF)
        text_brace63=brace63.get_text("63个0")
        
        self.play(Write(text[0]))
        self.play(GrowFromCenter(brace63),FadeIn(text_brace63.scale(0.8)))
        self.play(Write(text[1:]))
        self.wait(3)

class ep041(Scene):
    def construct(self):
        target_list = []
        for i in range(8):
            for j in range(8):
                if i%2==0:
                    if j%2==0:
                        grid = Square(fill_color=BLACK, fill_opacity=1,stroke_width=0.1)
                    else:
                        grid = Square(fill_color=WHITE, fill_opacity=1,stroke_width=0.1)
                else:
                    if j%2==0:
                        grid = Square(fill_color=WHITE, fill_opacity=1,stroke_width=0.1)
                    else:
                        grid = Square(fill_color=BLACK, fill_opacity=1,stroke_width=0.1)
                grid.scale(0.25)
                grid.move_to(np.array([-2+j*0.5,2-i*0.5,0]))
                target_list.append(grid)
                gridALL=VGroup(*target_list)
        self.play(FadeInFromPoint(gridALL,gridALL.get_center()))
        self.wait()
        text = TexMobject("1",
                          "2",
                          "4",
                          "8",
                          "16",
                          "...").set_color(RED).scale(0.6)
        for k in range(6):
            text[k].move_to(target_list[k].get_center())
            self.play(Write(text[k]))
            self.wait()
        self.wait()

class ep042(Scene):
    def construct(self):
        text = TexMobject("1+2+4+8+...+{2^{63}}", # 0
                          "=",                    # 1
                          "{2^{64}}-1",           # 2
                          "=",                    # 3
                          "18446744073709551615"  # 4
                          )
        brace63=Brace(text[0],UP,buff = 1*SMALL_BUFF)
        text_brace63=brace63.get_text("64格")
        text[1:3].set_color(RED)
        text[1:3].align_to(text[0],LEFT)
        text[1:3].shift(1*DOWN)
        text[3:5].align_to(text[0],LEFT)
        text[3:5].shift(1.8*DOWN)
        text[3:5].set_color_by_gradient(RED,ORANGE,YELLOW)
        self.play(Write(text[0]))
        self.play(GrowFromCenter(brace63),FadeIn(text_brace63.scale(0.8)))
        self.wait(9)
        self.play(Write(text[1:3]))
        self.wait(2)
        self.play(Write(text[3:5]))
        self.wait(3)

class ep043(Scene):
    def construct(self):
        text1 = TextMobject("1斤麦子=10000颗")
        text2 = TextMobject("18446744073709551615颗")
        text2.set_color_by_gradient(RED,ORANGE,YELLOW)
        text3 = TextMobject("=1845万亿斤麦子")
        text3.set_color_by_gradient(RED,ORANGE,YELLOW)
        text2.shift(DOWN)
        text3.align_to(text2,LEFT)
        text3.shift(1.8*DOWN)

        self.play(Write(text1))
        self.wait()
        self.play(FadeInFromDown(text2))
        self.wait()
        self.play(Write(text3))
        self.wait(5)


class ep044(Scene):
    def construct(self):
        text1 = TextMobject("1层: 1步")
        text2 = TextMobject("2层: 3步")
        text3 = TextMobject("3层: 7步")
        text4 = TextMobject("...")
        text5 = TextMobject("64层: ${2^{64}}$-1")
        text6 = TextMobject("=18446744073709551615步")
        
        VGroup(text1,text2,text3,text4,text5,text6).arrange_submobjects(DOWN,aligned_edge = LEFT,buff=0.4)
        text6.shift(RIGHT*1.6)
        text6.set_color_by_gradient(RED,ORANGE,YELLOW)
        self.play(Write(text1))
        self.wait(1)
        self.play(Write(text2))
        self.wait(1)
        self.play(Write(text3))
        self.wait(1)
        self.play(Write(text4))
        self.wait(1)
        self.play(Write(text5))
        self.wait(1)
        self.play(Write(text6))
        self.wait(2)

class ep045(Scene):
    def construct(self):
        text1 = Text("1秒=1步", font='义启魔音体')
        text2 = Text("1天=86400秒", font='阿里巴巴普惠体 B')
        text3 = TextMobject("1年365天=31536000秒")
        text5 = TextMobject("18446744073709551615秒$\\approx$5800亿年")
        text5.set_color_by_gradient(RED,ORANGE,YELLOW)
        text=VGroup(text1,text2,text3,text5).arrange_submobjects(DOWN,aligned_edge = LEFT,buff=0.4)
        text.shift(2*LEFT)
        self.play(ShowCreation(text),run_time=2)
        self.wait(10)