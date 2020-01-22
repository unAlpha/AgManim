from manimlib.imports import *

class ep071(Scene):
    def construct(self):
        text1 = Text("5 质数", font='义启魔音体')
        text2 = Text("8=2x4 合数", font='义启魔音体')
        VGroup(text1,text2).arrange_submobjects(DOWN,aligned_edge = RIGHT,buff=0.4)
        self.play(Write(text1),run_time=2)
        self.wait()
        self.play(Write(text2),run_time=2)
        self.wait(5)

class ep072(Scene):
    def construct(self):
        text1 = Text("哥德巴赫猜想", font='义启魔音体')
        text2 = Text("孪生素数猜想", font='义启魔音体')
        text3 = Text("费马猜想", font='义启魔音体')
        VGroup(text1,text2,text3).arrange_submobjects(DOWN,buff=0.4)
        self.add(text1)
        self.play(Indicate(text1,scale_factor=1.5))
        self.wait()
        self.add(text2)
        self.play(Indicate(text2,scale_factor=1.5))
        self.wait()
        self.add(text3)
        self.play(Indicate(text3,scale_factor=1.5))
        self.wait()
        self.wait(5)

class ep073(Scene):
    def construct(self):
        text1 = TexMobject("y(N)=N^2-N+41").set_color_by_gradient(YELLOW,RED).scale(2)

        self.play(Write(text1))
        self.wait(2)
        # self.play(ReplacementTransform(text1,text1.copy().scale(0.5).to_edge(UP)))
        self.play(
                text1.to_edge, UP,
                text1.scale, 0.5,
                text1.set_color, RED,
                run_time=2,
            )
        self.wait(2)

        text2 = TexMobject(
                            "y(1)=%s" %(self.yN(1)),
                            "y(2)=%s" %(self.yN(2)),
                            "y(3)=%s" %(self.yN(3)),
                            "y(4)=%s" %(self.yN(4)),
                            "...\\ \\ ...",
                            "y(40)=%s" %(self.yN(40)),
                            "y(41)=%s" %(self.yN(41))
                            )

        VGroup(text1,*text2).arrange_submobjects(DOWN,aligned_edge = LEFT,buff=0.4)

        ttmp = []
        for i in range(len(text2)-1):
            if i!=4:
                text = Text("质数", font='义启魔音体',size=0.5)
                if i<4:
                    text.next_to(text2[i],RIGHT,buff=1.75)
                else:
                    text.next_to(text2[i],RIGHT,buff=1)
            ttmp.append(text)

        text4 = Text("合数", font='义启魔音体',size=0.5,color=RED)
        text4.next_to(text2[-1],RIGHT,buff=1)
        text3 = VGroup(*ttmp)

        text2[0:4].shift(0.22*RIGHT)
        text2[4].shift(0.96*RIGHT)
        text2[5:7].shift(0.036*LEFT)

        for i in range(len(text2)-1):
            self.add(text2[i],text3[i])
            self.wait(0.5)

        self.wait()
        self.play(Write(text2[-1]))
        self.wait()
        self.add(text4)
        self.play(Indicate(text4,scale_factor=1.5))
        self.wait()
        self.wait(5)
        
    def yN(self,n):
        return n**2-n+41

class ep061(Scene):
    def construct(self):
        text1 = TexMobject("0.25=\\frac{1}{4}",
                           "0.333...=\\frac{1}{3}",
                           "0.454545...=\\frac{45}{99}")\
                               .arrange_submobjects(DOWN,aligned_edge = LEFT,buff=0.4)
        text2 = Text("有限小数",size=0.5)
        text2.next_to(text1[0],LEFT)
        text3 = Text("无限循环小数",size=0.5)
        text3.next_to(text1[1],LEFT)
        self.play(Write(text2))
        self.wait(1)
        self.play(Write(text3))
        self.wait(5)
        for i in range(len(text1)):
            self.play(Write(text1[i]))
            self.wait(2)
        brace1 = Brace(text1,RIGHT).set_color(YELLOW)
        btext1 = brace1.get_text("\\textbf{分数}").set_color(YELLOW)
        self.play(GrowFromCenter(brace1),FadeIn(btext1))
        self.wait(2)
        brace2 = Brace(VGroup(text1,text2,text3),DOWN).set_color(RED)
        btext2 = brace2.get_text("\\textbf{有理数}").set_color(RED)
        self.play(GrowFromCenter(brace2),FadeIn(btext2))
        self.wait(5)


class ep062(Scene):
    def construct(self):
        text1 = TexMobject("\\sqrt{2}=1.4142135623731...",
                           "\\pi=3.1415926535897...",
                           "... ...")\
                               .arrange_submobjects(DOWN,aligned_edge = RIGHT,buff=0.4)
        text1[2].shift(0.25*DOWN)
        for i in range(len(text1)):
            self.play(Write(text1[i]))
            self.wait(5)
        brace1 = Brace(text1,RIGHT)
        btext1 = brace1.get_text("\\textbf{无理数}")

        text2 = TexMobject("\\textbf{有理数}")
        text2.next_to(btext1,5*DOWN)

        brace2 = Brace(VGroup(btext1,text2),RIGHT)
        btext2 = brace2.get_text("\\textbf{实数}")

        VGroup(btext1,text2,brace2,btext2).set_color_by_gradient(YELLOW,RED)

        self.play(GrowFromCenter(brace1),FadeIn(btext1))
        self.wait(2)
        self.play(Write(text2))
        self.wait(2)
        self.play(GrowFromCenter(brace2),FadeIn(btext2))
        self.wait(5)

class ep063(Scene):
    def construct(self):
        numberline1=NumberLine(x_min=0,
                               x_max=6,
                               # 箭头
                               include_tip=True,
                               tick_size=0.2,
                               tick_frequency=1,
                               color=WHITE).move_to(ORIGIN)
        text_0=TextMobject("0")\
               .next_to(numberline1.get_tick(0),DOWN)
        text_1=TextMobject("1")\
               .next_to(numberline1.get_tick(1),DOWN)
        text_2=TextMobject("2")\
               .next_to(numberline1.get_tick(2),DOWN)
        text_3=TextMobject("3")\
               .next_to(numberline1.get_tick(3),DOWN)
        text_4=TextMobject("4")\
               .next_to(numberline1.get_tick(4),DOWN)
        text_5=TextMobject("5")\
               .next_to(numberline1.get_tick(5),DOWN)

        text_pi=TexMobject("\\pi")\
               .next_to(numberline1.get_tick(3.14),UP).shift(0.11*UP).set_color(RED)
        arrpi= Arrow(text_pi.get_bottom(),numberline1.get_tick(3.14)).set_color(RED)
        
        text_sqrt2=TexMobject("\\sqrt{2}")\
               .next_to(numberline1.get_tick(1.414),UP).scale(0.618).set_color(RED)
        arrsqrt2 = Arrow(text_sqrt2.get_bottom(),numberline1.get_tick(1.414)).set_color(RED)

        self.play(ShowCreation(numberline1),run_time=3)
        text=VGroup(text_0,text_1,text_2,text_3,text_4,text_5,text_sqrt2,arrsqrt2,text_pi,arrpi)
        self.add(text[0:6])
        for i in range(6,10):
            self.play(ShowCreation(text[i]))
        self.wait(5)

class ep064(Scene):
    def construct(self):
        text1 = Text("假设成立",size=0.5)
        text2 = Text("逻辑推理",size=0.5)
        text3 = Text("矛盾",size=0.5)
        text4 = Text("不成立",size=0.5)

        VGroup(text1,text3).arrange_submobjects(RIGHT ,buff=4)
        self.play(Write(text1))
        self.wait(2)
        arr1 = Arrow(text1.get_right(),text3.get_left(),color=YELLOW)
        text2.next_to(arr1,0.5*UP)
        self.play(Write(text2),ShowCreation(arr1),ShowCreation(text3))
        self.wait(2)

        arr2 = CurvedArrow(text3.get_bottom(),text1.get_bottom(),angle=-TAU/4,stroke_width=6,color=RED).shift(0.2*DOWN)
        text4.next_to(arr2,DOWN)
        self.play(ShowCreation(arr2),Write(text4))
        self.wait(2)

class ep065(Scene):
    def construct(self):
        text1 = Text("自然数",size=0.5)
        text2 = Text("实数",size=0.5)

        text1t = VGroup(text1,*TexMobject("1","2","3","4","5","6","7","..."))\
            .arrange_submobjects(DOWN,buff=0.41).scale(0.8)

        str1 = ["0.38602563078...",
                "0.55350762050...",
                "0.99356753207...",
                "0.25763200456...",
                "0.00005320562...",
                "0.99035638567...",
                "0.55522730456...",
                "...\\ ...",
                "0.52740712189..."]

        target_list = []
        for i in range(len(str1)):
            text=TexMobject(*list(str1[i]))
            target_list.append(text)
        text2t=VGroup(text2,*target_list).arrange_submobjects(DOWN,buff=0.4).scale(0.8)
        text2t[-1].shift(0.2*DOWN)
        
        text1t.next_to(text2t,3*LEFT).align_to(text2t,TOP)
        self.play(Write(text2))
        self.wait()
        for j in range(1,len(str1)):
            self.add(text2t[j])
            self.wait(0.2)
        self.wait(2)
        self.play(Write(text1t),run_time=2)
        self.wait(8)

        textX = Text("X =",size=0.42).set_color(RED).next_to(text2t[-1],LEFT)
        self.add(textX)
        self.play(Indicate(textX,scale_factor=1.5))
        self.wait(5)
        for i in range(len(str1)-2):
            self.play(Transform(text2t[1+i][2+i],text2t[1+i][2+i].set_color(RED)),Indicate(text2t[1+i][2+i],scale_factor=1.5))
            self.wait(3)
        self.wait(10)
        self.play(Write(text2t[-1].set_color_by_gradient(RED,ORANGE,YELLOW)))
        self.wait(10)


class ep066(Scene):
    def construct(self):
        text1 = Text("线段上的点的个数")
        text2 = Text("=",size=0.8)
        text3 = Text("实数的个数")
        text4 = Text(">",size=0.8)
        text5 = Text("自然数的个数")
        VgText = VGroup(text1,text2,text3,text4,text5).arrange_submobjects(RIGHT,buff=0.4).scale(0.8)
        self.play(Write(VgText[2:]))
        self.wait()
        self.play(Indicate(text4,scale_factor=1.5))
        self.wait(3)
        self.play(Write(VgText[:2]))
        self.wait()
        self.play(Indicate(text2,scale_factor=1.5))
        self.wait(3)
        VgText2 = VGroup(text1,text4,text5).copy().arrange_submobjects(RIGHT,buff=0.4)
        VgText2.align_to(VgText,RIGHT)
        self.play(Transform(VgText,VgText2))
        self.wait(5)

    
class ep0671(GraphScene):
    CONFIG ={
        "x_min" : -5,
        "x_max" : 5,
        "y_max" : 5,
        "y_axis_height": 5,
        "x_axis_label": None,
        "y_axis_label": None,
        "graph_origin": 1.2*DOWN,
        "xyStrokeOpacity": 0
    }
    def construct(self):
        self.setup_axes(animate=False)
        graghFuncXX = self.get_graph(lambda x: x**2,
                                    x_min = -2, 
                                    x_max = 2)
        self.play(ShowCreation(graghFuncXX),run_time=1)
        text1 = Text("抛物线",size=0.5).next_to(graghFuncXX,2*DOWN)
        self.play(Write(text1))
        self.wait(10)

class ep0672(GraphScene):
    CONFIG ={
        "x_min" : 0,
        "x_max" : 10,
        "y_max" : 5,
        "y_axis_height": 5,
        "x_axis_label": None,
        "y_axis_label": None,
        "graph_origin": LEFT*TAU/2,
        "xyStrokeOpacity": 0
    }
    def construct(self):
        self.setup_axes(animate=False)
        graghFuncXX = self.get_graph(lambda x: np.sin(x),
                                    x_min = 0, 
                                    x_max = TAU)
        self.play(ShowCreation(graghFuncXX),run_time=1)
        text1 = Text("正弦线",size=0.5).next_to(graghFuncXX,2*DOWN)
        self.play(Write(text1))
        self.wait(10)

class ep0673(GraphScene):
    def construct(self):
        curve1=ParametricFunction(lambda x : np.array([2*np.cos(x),1*np.sin(x),0]),\
            color=BLUE,t_min=-TAU,t_max=TAU)
        self.play(ShowCreation(curve1),run_time=1)
        text1 = Text("椭圆",size=0.5).next_to(curve1,2*DOWN)
        self.play(Write(text1))
        self.wait(10)

class ep0674(GraphScene):
    CONFIG = {
        "y_max" : 10,
        "y_min" : -10,
        "x_max" : 5,
        "x_min" : -5,
        "graph_origin" : ORIGIN,
        "x_axis_label": None,
        "y_axis_label": None,
        "xyStrokeOpacity": 0
    }
    def construct(self):
        self.setup_axes()
        tan_function = lambda x: np.tan(x)
        tan_graph = VGroup()
        approx_factor = 0.934
        for n in range(-1,2):
            graph = self.get_graph(tan_function, 
                                    color = BLUE,
                                    x_min = (-PI/2)*approx_factor+n*PI,
                                    x_max = (PI/2)*approx_factor+n*PI
                                    )
            tan_graph.add(graph)
        self.play(ShowCreation(tan_graph))
        text1 = Text("正切线",size=0.5).next_to(tan_graph,2*DOWN)
        self.play(Write(text1))
        self.wait(10)


class ep0675(GraphScene):
    def construct(self):
        tan_graph = VGroup()
        approx_factor = 0.8
        for n in range(-1,2):
            curve1=ParametricFunction(lambda x : np.array([1/np.cos(x),0.5*np.tan(x),0]),\
                color=BLUE,t_min=(-PI/2)*approx_factor+n*PI,t_max=(PI/2)*approx_factor+n*PI)
            tan_graph.add(curve1)
        self.play(ShowCreation(tan_graph.shift(UP)),run_time=1)
        text1 = Text("双曲线",size=0.5).next_to(tan_graph,2*DOWN)
        self.play(Write(text1))
        self.wait(10)

        
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
        # 更好的方法使用Group排列
        # group1 = Group(bead1,copperCoin1).arrange_submobjects(DOWN,aligned_edge = LEFT,buff=0.4)
        # self.add(group1)
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