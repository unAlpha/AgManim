from manimlib.imports import *

class ten63(Scene):
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

class ChessBoard(Scene):
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

class pow2(Scene):
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

class pow3(Scene):
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


class pow4(Scene):
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

class pow5(Scene):
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