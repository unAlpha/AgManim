from manimlib.imports import *

class ep1101(GraphScene):
    CONFIG ={
        "x_min" : -4,
        "x_max" : 6,
        "y_min" : -1,
        "y_max" : 6,
        "x_axis_label" : "实轴",
        "y_axis_label" : "虚轴",
        "graph_origin": 2.6 * DOWN + 2 * LEFT
    }
    def construct(self):
        self.setup_axes()
        # 初始坐标
        x0=0
        y0=0
        vector1 = self.vector(x0,y0,4,2,True)
        vector2 = self.vector(x0,y0,1,3,True)

        # 动画1
        elbow = self.polyline(ORIGIN,4*RIGHT,4*RIGHT+2*UP)
        dot = Dot()
        dot.move_to(elbow.get_start())
        self.add(dot)
        self.play(
            MoveAlongPath(dot,elbow),  
            run_time=2
            )
        self.play(Write(vector1[1]))
        self.wait(2)
        self.play(ShowCreation(vector1[0]))
        self.wait(2)
        self.play(ShowCreation(vector2))
        self.wait(2)

        text1 = Text("复平面",size=0.86)
        text1.to_corner(UP+RIGHT)
        self.play(FadeInFromLarge(text1))
        self.wait()

        dashVector1 = self.dashVector(4,2,5,5,True)
        dashVector2 = self.dashVector(1,3,5,5,True)
        vector3 = self.vector(0,0,5,5,True).set_color(BLUE)

        self.remove(dot)
        self.play(
            ShowCreation(dashVector1[0]),
            ShowCreation(dashVector2[0]),
            vector1[1].shift,DOWN*0.36+RIGHT*0.16,
            vector2[1].shift,UP*0.2+LEFT*0.86,     
        )
        self.wait()
        self.play(ShowCreation(vector3),run_time=2)
        self.wait(2)

        self.remove(
            dashVector1[0],
            dashVector2[0],
            vector3
            )
        self.wait()

        # 动画2
        vector4 = self.vector(1,3,4,2,0).set_color(PINK)
        tex2 = TexMobject("3-i").set_color(PINK)
        tex2.next_to(vector4.get_center(),UP,buff=MED_SMALL_BUFF)
        tex2.rotate(vector4[0].get_angle())
        self.play(ShowCreation(vector4))
        self.play(Write(tex2))
        self.wait(3)

        self.remove(
            tex2,
            vector4,
            vector1[0],
            vector1[1],
            vector2[0],
            vector2[1]
            )

        # 动画3
        vector5 = self.vector(0,0,3,0,0)
        vector55 = self.vector(0,0,3,0,0).set_color(BLUE)
        arc = Arc(radius=3)
        arcCoords = VMobject()
        arcCoords.set_points([self.coords_to_point(point[0],point[1]) for point in arc.points])
        dot2 = Dot(radius=1e-3)
        dot2.move_to(arcCoords.get_start())
        vector5.add_updater(lambda obj: obj.become(self.vector(
                    x0,y0,
                    self.point_to_coords(dot2.get_center())[0],
                    self.point_to_coords(dot2.get_center())[1],0)))
        tex3 = TexMobject("a=3").set_color(BLUE)\
            .next_to(self.x_axis.get_tick(3),UP,buff=MED_SMALL_BUFF)
        tex4 = TexMobject("b=3i")\
            .next_to(self.y_axis.get_tick(3),RIGHT,buff=MED_SMALL_BUFF)
        
        self.play(ShowCreation(vector55))
        self.play(Write(tex3))
        self.wait()
        self.add(vector5)
        self.play(
            MoveAlongPath(dot2,arcCoords),
            run_time=2
        )
        self.play(Write(tex4))
        self.wait(3)

        self.remove(dot2,tex3,tex4,vector5,vector55)

        # 动画4
        x1 = 4
        y1 = 2
        x2 = -2
        y2 = 4
        r1 = math.sqrt(x1**2+y1**2)
        r2 = math.sqrt(x2**2+y2**2)
        star_angle = math.asin(y1/r1)
        angle = PI-math.asin(y2/r2)-star_angle

        vector6 = self.vector(0,0,x1,y1,0)
        vector66 = self.vector(0,0,x1,y1,0).set_color(BLUE)
        arc1 = Arc(star_angle,angle,radius=r1)
        arcCoords1 = VMobject()
        arcCoords1.set_points([self.coords_to_point(point[0],point[1]) for point in arc1.points])
        dot3 = Dot(radius=1e-3)
        dot3.move_to(arcCoords1.get_start())
        vector6.add_updater(lambda obj: obj.become(self.vector(
                    x0,y0,
                    self.point_to_coords(dot3.get_center())[0],
                    self.point_to_coords(dot3.get_center())[1],
                    0
                    )
                )
            )

        tex5 = TexMobject("a=%s+%si"%(x1,y1)).set_color(BLUE)\
            .next_to(self.coords_to_point(4,2),UP,buff=MED_SMALL_BUFF)
        tex6 = TexMobject("b=%s+%si"%(x2,y2))\
            .next_to(self.coords_to_point(-2,4),UP,buff=MED_SMALL_BUFF)
        
        self.play(ShowCreation(vector66))
        self.play(Write(tex5))
        self.wait()
        self.add(vector6)
        self.play(
            MoveAlongPath(dot3,arcCoords1),
            run_time=2
        )
        self.play(Write(tex6))
        self.wait(3)
 
    def polyline(self,*points):
        polyline1 = VMobject()
        pointslist = [self.coords_to_point(point[0],point[1]) for point in points]
        polyline1.set_points_as_corners(pointslist)
        return polyline1

    def vector(self,x1=0,y1=0,x2=1,y2=1,texNeed=False):
        arr = Arrow(self.coords_to_point(x1,y1),self.coords_to_point(x2,y2),buff=0)
        if texNeed:
            if round(abs(y2),1)==0.0:
                tex = TexMobject("%.0f"%x2)
            else:
                tex = TexMobject("%.0f+%.0fi"%(x2,abs(y2)))
            tex.next_to(arr.end,UP+RIGHT,buff=SMALL_BUFF)
            return VGroup(arr,tex)
        else:
            return arr

    def dashVector(self,x1=0,y1=0,x2=1,y2=1,texNeed=False):
        arr = DashedLine(
            self.coords_to_point(x1,y1),self.coords_to_point(x2,y2),
            buff=0,
            dash_length=5*DEFAULT_DASH_LENGTH,
            stroke_width=6
            )
        if texNeed:
            tex = TexMobject("(%.0f,%.0f)"%(x2,y2))
            tex.next_to(arr.end,UP+RIGHT,buff=SMALL_BUFF)
            return VGroup(arr,tex)
        else:
            return arr

    def setup_axes(self):
        GraphScene.setup_axes(self)

        values_y = [(n,str(n)+"i") for n in range(self.y_min+1,self.y_max,1) if n!=0]
        self.y_axis_label_mob.set_color(RED)
        self.x_axis_label_mob.set_color(YELLOW)
        self.x_axis.add_numbers(*[i for i in range(self.x_min+1,self.x_max,1)])
        # self.x_axis.numbers[0].shift(0.2*LEFT)
        self.y_axis_labels = VGroup()

        for y_val, y_tex in values_y:
            tex = TexMobject(y_tex) # Convert string to tex
            tex.scale(0.7) 
            # coords_to_point 获取指定值的点坐标
            tex.next_to(self.coords_to_point(0 ,y_val), LEFT)
            self.y_axis_labels.add(tex)  

        self.play(
            Write(self.y_axis_labels),
            Write(self.x_axis.numbers)
        )
        self.wait()

class vectors(GraphScene):
    CONFIG ={
        "x_min" : -1,
        "x_max" : 10,
        "y_min" : -1,
        "y_max" : 10,
        "x_axis_label" : "实数",
        "y_axis_label" : "虚数",
    }
    def construct(self):
        self.setup_axes()
        
        self.x_axis.add_numbers(*[i for i in range(1,10,2)])
        self.y_axis.add_numbers(*[i for i in range(-0,10,2)])
        # 1 创建对象
        vector1 = self.vector(1,1,5,5,True)
        # 2 变化的量
        vlu = ValueTracker(5)
        # 3 add_updater
        vector1.add_updater(lambda obj: obj.become(self.vector(1,1,5,vlu.get_value(),True)))

        dashV = self.dashVector(1,1,8,1)

        # 4 show
        self.play(ShowSubmobjectsOneByOne(vector1))
        # 5 add
        self.add(vector1)
        # 6 change
        self.play(vlu.increment_value,1)
        # 7 change again
        self.play(vlu.increment_value,-2)
        self.play(ShowCreation(dashV))
        self.wait()
    # 0 定义对象
    def vector(self,x1=0,y1=0,x2=1,y2=1,texNeed=False):
        arr = Arrow(self.coords_to_point(x1,y1),self.coords_to_point(x2,y2),buff=0)
        tex = TexMobject("(%.1f,%.1f)"%(x2,y2))
        tex.next_to(arr.end,UP+RIGHT,buff=SMALL_BUFF)
        if texNeed:
            return VGroup(arr,tex)
        else:
            return arr

    def dashVector(self,x1=0,y1=0,x2=1,y2=1,texNeed=False):
        arr = DashedLine(
            self.coords_to_point(x1,y1),self.coords_to_point(x2,y2),
            buff=0,
            dash_length=5*DEFAULT_DASH_LENGTH,
            stroke_width=6
            )
        arr.add_tip()
        tex = TexMobject("(%.1f,%.1f)"%(x2,y2))
        tex.next_to(arr.end,UP+RIGHT,buff=SMALL_BUFF)
        if texNeed:
            return VGroup(arr,tex)
        else:
            return arr

class ep1011(Scene):
    def construct(self):
        def fsin(dx=1):
            return FunctionGraph(lambda x: np.sin(x-dx),x_min=-TAU/2-1.5,x_max=TAU/2+1).set_color(RED)
        def fcos(dx=1):
            return FunctionGraph(lambda x: np.cos(x-dx),x_min=-TAU/2-1.5,x_max=TAU/2+1).set_color(YELLOW)

        gsin = fsin()
        gcos = fcos()
        axes=Axes(x_min=-5,x_max=5.5,y_min=-2, y_max=2)

        text1 = Text("功率=电压x电流",size=0.8).shift(UP)
        text2 = Text("电压",size=0.5).move_to(2.5*UP+4*RIGHT).set_color(RED)
        line1 = Line(start=ORIGIN, end=RIGHT).next_to(text2,LEFT).set_color(RED)
        text3 = Text("电流",size=0.5).next_to(text2,DOWN).set_color(YELLOW)
        line2 = Line(start=ORIGIN, end=RIGHT).next_to(text3,LEFT).set_color(YELLOW)

        self.play(Write(text1))
        self.wait()
        self.play(
            text1.to_corner,UP+LEFT
        )
        self.wait()
        # 摆掉dt的限制
        def update_curveSin(func, alpha):
            dx = interpolate(1, 20, alpha)
            funcdx = fsin(dx)
            func.become(funcdx)

        def update_curveCos(func, alpha):
            dx = interpolate(1, 20, alpha)
            funcdx = fcos(dx)
            func.become(funcdx)

        self.play(
            ShowCreation(axes),
            ShowCreation(gsin),
            ShowCreation(gcos),
            ShowCreation(VGroup(text2,line1)),
            ShowCreation(VGroup(text3,line2))
            )
        self.wait(2)
        self.play(
            UpdateFromAlphaFunc(gsin,update_curveSin),
            UpdateFromAlphaFunc(gcos,update_curveCos),
            rate_func=linear,
            run_time=20
            )
        self.wait(5)

class ep1010(Scene):
    def construct(self):
        tex1 = TexMobject("\\sqrt{-1}=i").set_color_by_gradient(YELLOW,RED)
        tex2 = TexMobject("i^2=(\\sqrt{-1})^2=-1")
        tex3 = TexMobject("i^3=i^2 \\times i=-i")
        tex4 = TexMobject("i^4=i^2 \\times i^2 =(-1)^2=1")
        tex5 = TexMobject("\\sqrt{-9}=\\sqrt{9}\\times \\sqrt{-1}=3i")
        tex6 = TexMobject("\\sqrt{-4}=\\sqrt{4}\\times \\sqrt{-1}=2i")
        tex7 = TexMobject("(","5+\\sqrt{15}i",")","\\times","(","5-\\sqrt{15}i",")","=40")
        allVG= VGroup(tex1,tex2,tex3,tex4,tex5,tex6,tex7).arrange(DOWN,aligned_edge = LEFT,buff=MED_SMALL_BUFF)
        rect1 = SurroundingRectangle(tex7[1])
        rect2 = SurroundingRectangle(tex7[5])
        rect1t = TextMobject("\\textbf{复数}").set_color(YELLOW).next_to(rect1,DOWN)
        rect2t = TextMobject("\\textbf{复数}").set_color(YELLOW).next_to(rect2,DOWN)
        self.play(LaggedStartMap(Write,[obj for obj in allVG],lag_ratio=2),run_time=12)
        self.wait()
        self.play(ShowCreation(rect1),ShowCreation(rect2),Write(rect1t),Write(rect2t))
        self.wait()

class ep109(GraphScene):
    CONFIG ={
        "x_min" : -10,
        "x_max" : 10,
        "x_tick_frequency" : 1,
        "y_min" : -5,
        "y_max" : 5,
        "y_tick_frequency" : 1,
        "graph_origin": ORIGIN,
        "x_axis_label" : "实数",
        "y_axis_label" : "虚数",
    }
    def construct(self):
        self.setup_axes()
        mirror = ImageMobject("mirror").set_height(self.y_axis.get_height()-MED_LARGE_BUFF).shift(LEFT*0.038)
        mirror.rotate(-PI/4)
        text3 = Text("魔镜",size=0.5).shift(UP+RIGHT)
        self.wait()
        self.play(FadeInFromLarge(mirror),Write(text3))
        self.wait()


    def setup_axes(self):
        GraphScene.setup_axes(self)
        values_y = [
            (1,"i"),
            (2,"2i"),
            (3,"3i"),
            (4,"4i"),
            (-1,"-i"),
            (-2,"-2i"),
            (-3,"-3i"),
            (-4,"-4i"),
        ]
        self.y_axis_label_mob.set_color(RED)
        self.x_axis_label_mob.set_color(YELLOW)
        self.x_axis.add_numbers(*[i for i in range(-10,12,2)])
        self.y_axis_labels = VGroup()
        for y_val, y_tex in values_y:
            tex = TexMobject(y_tex) # Convert string to tex
            tex.scale(0.7) 
            # coords_to_point 获取指定值的点坐标
            tex.next_to(self.coords_to_point(0 ,y_val), LEFT)
            self.y_axis_labels.add(tex)
        self.play(
            Write(self.y_axis_labels),
            Write(self.x_axis.numbers)
        )
        self.wait()

class ep108(GraphScene):
    CONFIG ={
        "x_min" : -10,
        "x_max" : 10,
        "x_tick_frequency" : 1,
        "y_min" : -50,
        "y_max" : 50,
        "y_tick_frequency" : 10,
        "graph_origin": ORIGIN,
    }
    def construct(self):
        self.setup_axes(animate=True)
        self.x_axis.add_numbers(*[i for i in range(-10,12,2)])

        text1 = TextMobject("正数").shift(2*(UP+1.5*RIGHT)).set_color(YELLOW)
        text2 = TextMobject("负数").shift(2*(UP+1.5*LEFT)).set_color(RED)

        self.play(Write(self.x_axis.numbers),Write(text1),Write(text2))
        mirror = ImageMobject("mirror").set_height(self.y_axis.get_height()-LARGE_BUFF).shift(LEFT*0.038)

        text3 = Text("镜子",size=0.5).shift(UP)
        self.wait()
        self.play(FadeInFromLarge(mirror),Write(text3))
        self.wait(2)
        
class ep107(Scene):
    def construct(self):
        tex1 = TexMobject("(\\sqrt{-15})^2=-15").set_color_by_gradient(YELLOW,RED)
        tex2 = TexMobject("a=5+\\sqrt{-15},\\ \\","b=5-\\sqrt{-15}")
        tex4 = TexMobject("a \\times b")
        tex5 = TexMobject("=(5+\\sqrt{-15})\\times(5-\\sqrt{-15})")
        tex6 = TexMobject("=5^2-(\\sqrt{-15})^2")
        tex7 = TexMobject("=25-(-15)")
        tex8 = TexMobject("=40")

        eqr = VGroup(tex5,tex6,tex7,tex8).arrange(DOWN,aligned_edge = LEFT)
        tex4.next_to(tex5,LEFT)
        eqrVg = VGroup(eqr,tex4)
        VGroup(tex1,tex2,eqrVg).arrange(DOWN,buff=MED_LARGE_BUFF)
        self.play(Write(tex1))
        self.wait()
        self.play(Write(tex2))
        self.wait()
        self.play(Write(tex4))
        self.wait()
        self.play(Write(tex5))
        self.wait()
        self.play(Write(tex6))
        self.wait()
        self.play(Write(tex7))
        self.wait()
        self.play(Write(tex8))
        self.wait()

class ep106(Scene):
    def construct(self):
        Cardano = self.imageObjAndText("Cardano","卡尔丹") 
        self.play(FadeInFromLarge(Cardano))
        self.wait()

        tex = TexMobject("a+b=10\\ \\","a \\times b=40\\ \\","a=","?",",b=","?")
        tex.set_color_by_tex("?",RED)
        numVG=VGroup()
        for i in range(5):
            tex1 = self.numberCircle("%s"%(i+1))
            texab = TexMobject("a=%s,\\ \\ "%(i+1),"b=%s,\\ \\ "%(9-i),"a \\times b = ","%s"%((i+1)*(9-i)))
            numVG.add(VGroup(tex1,texab).arrange(RIGHT,buff=MED_LARGE_BUFF))
        allVG = VGroup(tex,numVG.scale(0.68).arrange(DOWN,aligned_edge = LEFT))\
            .arrange(DOWN,aligned_edge = LEFT,buff=MED_LARGE_BUFF)
        allVG.next_to(Cardano,RIGHT,buff=MED_LARGE_BUFF)

        arr = Arrow(numVG.get_corner(UP+RIGHT),numVG.get_corner(DOWN+RIGHT),buff=SMALL_BUFF).shift(0.5*RIGHT)\
            .set_color(RED)
        text1 = Text("""
                    a+b 一定
                    a, b 接近
                    axb 越大
                    """,
                    font='阿里巴巴普惠体 B',
                    size=0.5,
                    lsh=0.6
                    ).next_to(arr,1.5*RIGHT).set_color(YELLOW)
        rect = SurroundingRectangle(numVG[-1][-1][-1])
        text2 = Text("无解...",size=0.8,gradient=(YELLOW_D,RED)).next_to(rect,2*DOWN)
        self.play(Write(tex[0:2]))
        self.wait()
        self.play(FadeInFromDown(tex[2:]))
        self.wait()
        self.play(LaggedStartMap(Write,[obj for obj in numVG],lag_ratio=2),run_time=8)
        self.wait()
        self.play(ShowCreation(arr))
        self.play(Write(text1),run_time=2)
        self.wait()
        self.play(ShowCreation(rect))
        self.wait()
        self.add(text2)
        self.play(Indicate(text2))
        self.wait(2)

    def imageObjAndText(self,imageName,text):
        pic = ImageMobject(imageName).shift(4*LEFT).scale(2)
        pic.rect = SurroundingRectangle(pic,color=WHITE,stroke_width=8,buff=0)
        picText = Text(text, 
                        font='阿里巴巴普惠体 B',
                        size=0.5).next_to(pic,DOWN)
        return Group(pic,pic.rect,picText)
    def numberCircle(self,number):
        tex = TexMobject(number)
        texW = tex.get_width()
        texH = tex.get_height()
        clr = Circle(
                    radius=max(texW,texH)-SMALL_BUFF,
                    stroke_width=DEFAULT_STROKE_WIDTH/2,
                    color=WHITE
        )
        clr.move_to(tex)
        return VGroup(tex,clr).scale(0.8)

class ep105(Scene):
    def construct(self):
        tex1 = TexMobject("2 \\times 2=4")
        tex2 = TexMobject("(-2) \\times (-2)=4")
        text1 = TextMobject("\\textbf{任何一个数的平方都是非负的}")
        VG1 = VGroup(tex1,tex2,text1).arrange(DOWN)

        square1 = Square().set_fill(RED,opacity = 0.5)
        tex3 = TexMobject("\\sqrt{-4}=?")
        tex4 = TexMobject("S=-4")
        VG2 = VGroup(square1,tex3).arrange(RIGHT,buff=LARGE_BUFF)

        VGroup(VG1,VG2).arrange(DOWN,buff=LARGE_BUFF)
        tex4.move_to(square1)
        brace1 =Brace(square1,DOWN)
        brace1txt = brace1.get_text("a=?")

        cross1 = Cross(VGroup(square1,brace1,brace1txt))
        cross2 = Cross(tex3)
        
        self.play(Write(tex1))
        self.wait()
        self.play(Write(tex2))
        self.wait(2)
        self.play(Write(text1))
        self.wait()
        self.play(*map(ShowCreation,[square1,tex4,brace1,brace1txt]))
        self.play(Write(tex3))
        self.wait()
        self.play(ShowCreation(VGroup(cross1,cross2)))
        self.wait(2)
      
class ep104(Scene):
    def construct(self):
        square1 = Square().set_fill(RED,opacity = 0.5)
        brace1 =Brace(square1,DOWN)
        brace1txt = brace1.get_text("a")
        saa = TexMobject("S=a^2")
        ssq = TexMobject("\\sqrt{S}=a")

        allVG = VGroup(square1,brace1,brace1txt,saa).arrange(DOWN)
        ssq.next_to(allVG,DOWN,buff=MED_LARGE_BUFF)
        self.play(ShowCreation(allVG),run_time=3)
        self.wait()
        self.play(Write(ssq),ShowCreation(SurroundingRectangle(ssq)))
        self.wait()

class ep103(Scene):
    def construct(self):
        nums = [2, 10, 11, 12]
        formulaVG = VGroup()
        for num in nums:
            Fnum = TexMobject("%s"%num,"^2=","%s"%(num**2), "\\Rightarrow","\\sqrt{%s} = %s"%(num**2,num))
            formulaVG.add(Fnum)
        formulaVG.arrange(DOWN)

        sq2 = TexMobject("\\sqrt{2}=1.414 \\dots").next_to(formulaVG,DOWN,buff=MED_LARGE_BUFF)\
            .set_color(RED)

        s2qtext = TextMobject("\\textbf{平方根}").next_to(formulaVG[0][0],UP+LEFT,buff=MED_LARGE_BUFF)\
            .set_color(YELLOW)
        sq2text = TextMobject("\\textbf{完全平方数}").next_to(formulaVG[0][2],UP,buff=LARGE_BUFF*0.7)\
            .set_color(YELLOW)
        s2qArr = Arrow(formulaVG[0][0].get_corner(UP+LEFT),s2qtext.get_corner(DOWN+RIGHT),buff=SMALL_BUFF)\
            .set_color(YELLOW)
        sq2Arr = Arrow(formulaVG[0][2].get_corner(UP),sq2text.get_corner(DOWN),buff=SMALL_BUFF)\
            .set_color(YELLOW)
        
        formulaVG[0][0].set_color(YELLOW)
        formulaVG[0][2].set_color(YELLOW)


        self.play(Write(formulaVG[0][2]),ShowCreation(sq2Arr),FadeIn(sq2text))
        self.wait()
        self.play(Write(formulaVG[0][0:2]),ShowCreation(s2qArr),FadeIn(s2qtext))
        self.wait()
        self.play(FadeInFromPoint(formulaVG[0][3:],formulaVG[0][3:].get_corner(LEFT)))
        self.wait()
        self.play(FadeInFrom(formulaVG[1],LEFT))
        self.wait()
        self.play(FadeInFrom(formulaVG[2],LEFT))
        self.wait()
        self.play(FadeInFrom(formulaVG[3],LEFT))
        self.wait()
        self.play(Write(sq2))
        self.wait()

class ep102(Scene):
    def construct(self):
        NaturalNum = TexMobject("1, 2, 3, 4, \\dots")
        NaturalNumTxt = TextMobject("\\textbf{自然数}")
        VGNaturalNum = VGroup(NaturalNum,NaturalNumTxt).arrange(RIGHT,buff=MED_LARGE_BUFF)
        addition = TexMobject(
                                "3+5=8",
                                "5+8=13",
                                "\\dots"
        ).arrange_submobjects(DOWN,aligned_edge = LEFT,buff=MED_SMALL_BUFF)
        addition[-1].shift(DOWN*0.125)
        subtraction =TexMobject("5-","8","=","?",
                                tex_to_color_map={
                                            "?" : RED
            }
        )
        VGroup(VGNaturalNum, addition, subtraction).arrange(DOWN,aligned_edge = LEFT,buff=MED_LARGE_BUFF)
        braceAdd = Brace(addition,RIGHT,buff=MED_LARGE_BUFF)
        braceAddt = TextMobject("\\textbf{加法封闭}")
        braceAdd.put_at_tip(braceAddt)
        subtxt = TextMobject("\\textbf{减法不封闭}",color=RED).next_to(subtraction,RIGHT,buff=LARGE_BUFF)

        self.play(Write(NaturalNum))
        self.wait()
        self.add(NaturalNumTxt)
        self.play(Indicate(NaturalNumTxt))
        self.wait()
        self.play(LaggedStartMap(Write,addition),GrowFromCenter(braceAdd),FadeIn(braceAddt),run_time=3)
        self.wait()

        self.play(Write(subtraction))
        self.wait()
        self.add(subtxt)
        self.play(Indicate(subtxt))
        self.wait(2)

        self.play(
            *map(FadeOut,(NaturalNum,NaturalNumTxt,addition,braceAdd,braceAddt,subtxt)),
            subtraction.move_to,NaturalNum
        )
        self.wait()

        goat = SVGMobject("goat").scale(0.4)
        goat_group = VGroup(*[
                goat.copy().shift(-x*UP + y*RIGHT)
                for x in range(2)
                for y in range(4)
            ])
        
        goat_group.next_to(subtraction,DOWN,buff=MED_LARGE_BUFF).align_to(subtraction,LEFT)
        goat_gray = goat_group[5:].copy().set_color(DARK_GREY)
        goat_red = goat_group[5:].set_color(RED)
        subtractionEND = TexMobject("-3").next_to(subtraction[-2]).set_color(RED)
        self.play(FadeInFromDown(goat_group[0:5]))
        self.wait()
        self.play(ShowCreation(SurroundingRectangle(subtraction[1])),FadeInFromDown(goat_gray))
        self.wait()
        self.play(FadeInFromDown(goat_red))
        self.wait()
        self.play(Transform(subtraction[-1],subtractionEND))
        self.wait(5)
                
class ep101(Scene):
    def construct(self):
        imaginaryTxt = Text("虚数",font='阿里巴巴普惠体 B')
        self.add(imaginaryTxt)
        self.play(Indicate(imaginaryTxt))
        self.wait()

class ep095(Scene):
    def construct(self):
        pic1 = self.imageObjAndText("ChenJinRun","陈景润")

        text1 = TexMobject("“1+2”")

        text2 = Text("""
                “任何一个大偶数都可以写成1个
                质数及不超过2个质数的乘积之和。”
            """,
            font='阿里巴巴普惠体 B',
            size=0.5,
            lsh=0.8
        )

        text3 = Text("即:",           
            font='阿里巴巴普惠体 B',
            size=0.5
        )

        textab = TexMobject(
            "X",
            "=",
            "a+b",
            "\\\\or",
            tex_to_color_map={
                "X" : RED
            }
        )
        textab[-1].shift(1.2*LEFT)
        textabc = TexMobject(
            "X",
            "=",
            "a+bc",
            tex_to_color_map={
                "X" : RED
            }
        )

        abVG = VGroup(textab,textabc).arrange(DOWN,aligned_edge = LEFT,buff=MED_SMALL_BUFF)
        jiVG = VGroup(text3,abVG).arrange(RIGHT,aligned_edge = UP,buff=MED_SMALL_BUFF)
        textVG = VGroup(text2,jiVG).arrange(DOWN,buff=MED_LARGE_BUFF)
        text1.next_to(textVG,4*UP)

        text4 = TextMobject("偶数")
        brace1 = Brace(textabc[2])
        brace1t1 = brace1.get_text("a,b,c是质数")
        text4.next_to(textabc[0],DOWN+0.1*LEFT,buff=0.8)
        arr = Arrow(text4.get_top(),textabc[0].get_bottom(),buff=SMALL_BUFF)

        allVG = VGroup(text1,textVG,text4,brace1,brace1t1,arr)
        allVG.next_to(pic1,RIGHT,buff= MED_LARGE_BUFF)
        text1.rect = SurroundingRectangle(text1)

        self.play(FadeInFromLarge(pic1))
        self.wait()
        self.play(Write(text1),ShowCreation(text1.rect))
        self.wait()
        self.play(Write(text2),run_time=2)
        self.wait()
        self.play(Write(text3))
        self.wait()
        self.add(textab[0])
        self.play(Indicate(textab[0]))
        self.play(Write(textab[1:3]))
        self.play(LaggedStartMap(FadeInFromDown,(textab[-1],textabc,arr,text4,brace1,brace1t1)))
        self.wait(5)

    def imageObjAndText(self,imageName,text):
        pic = ImageMobject(imageName).shift(4*LEFT).scale(2)
        pic.rect = SurroundingRectangle(pic,color=WHITE,stroke_width=8,buff=0)
        picText = Text(text, 
                        font='阿里巴巴普惠体 B',
                        size=0.5).next_to(pic,DOWN)
        return Group(pic,pic.rect,picText)

class ep094(Scene):
    def construct(self):
        text1 = TexMobject("“1+3”").to_edge(UP)
        text1.rect = SurroundingRectangle(text1)

        textab = TexMobject(
            "X",
            "=",
            "a+b",
            "\\\\or",
            tex_to_color_map={
                "X" : RED
            }
        )
        textab[-1].shift(1.2*LEFT)
        textabc = TexMobject(
            "X",
            "=",
            "a+bc",
            "\\\\or",
            tex_to_color_map={
                "X" : RED
            }
        )
        textabc[-1].shift(1.43*LEFT)
        textabcd = TexMobject(
            "X",
            "=",
            "a+bcd",
            tex_to_color_map={
                "X" : RED
            }
        )

        VGroup(textab,textabc,textabcd).arrange(DOWN,aligned_edge = LEFT,buff=MED_SMALL_BUFF).next_to(text1,DOWN,buff=MED_LARGE_BUFF)

        text3 = TextMobject("偶数")
        brace1 = Brace(textabcd[2])
        brace1t1 = brace1.get_text("a,b,c,d是质数")

        text3.next_to(textabcd[0],DOWN+0.1*LEFT,buff=0.8)
        arr = Arrow(text3.get_top(),textabcd[0].get_bottom(),buff=SMALL_BUFF)

        self.play(Write(text1),ShowCreation(text1.rect))
        self.wait()
        self.play(FadeInFromDown(textab[0:3]))
        self.wait()
        self.play(FadeInFromDown(VGroup(textab[-1],textabc[0:3])))
        self.wait()
        self.play(LaggedStartMap(FadeInFromDown,(textabc[-1],textabcd,arr,text3,brace1t1,brace1)),run_time=2)
        self.wait(2)

class ep093(Scene):
    def construct(self):
        text1 = Text("布朗",size=0.65).to_edge(TOP)
        text2 = TexMobject(
            "X",
            "=",
            "a_1 a_2 a_3 \\dots a_m+b_1 b_2 b_3 \\dots b_n",
            tex_to_color_map={
                "X" : RED
            }
        ).next_to(text1,DOWN,buff=MED_LARGE_BUFF)
        text3 = TextMobject("偶数")
        text4 = TexMobject("m,n \\le 9 \\\\","“9+9”").arrange(DOWN,buff=MED_LARGE_BUFF)
        brace1 = Brace(text2[2])
        brace1t1 = TextMobject("$$a_i,b_i$$","是质数").arrange(RIGHT)
        brace1.put_at_tip(brace1t1)

        text3.next_to(text2[0],DOWN,buff=0.8)
        arr = Arrow(text3.get_top(),text2[0].get_bottom(),buff=SMALL_BUFF)
        text4.next_to(brace1t1,DOWN,buff=MED_SMALL_BUFF)

        self.play(Write(text1))
        self.wait()
        self.play(LaggedStartMap(FadeInFromDown,(text2,arr,text3,brace1t1,brace1)),run_time=2)
        self.wait()
        self.play(Write(text4))
        self.wait()
        self.play(ShowCreation(SurroundingRectangle(text4[1])))
        self.wait(5)

class ep092(Scene):
    def construct(self):
        text1 = Text("史尼尔曼",size=0.65).to_edge(TOP)
        text2 = TexMobject(
            "X",
            "=",
            "a_1 + a_2+ \\dots + a_k",
            tex_to_color_map={
                "X" : RED
            }
        ).next_to(text1,DOWN,buff=MED_LARGE_BUFF)
        text3 = TextMobject("偶数")
        text4 = TexMobject("k \\le 800000")
        brace1 = Brace(text2[2])
        brace1t1 = TextMobject("$$a_i$$","是质数").arrange(RIGHT)
        brace1.put_at_tip(brace1t1)

        text3.next_to(text2[0],DOWN,buff=0.8)
        arr = Arrow(text3.get_top(),text2[0].get_bottom(),buff=SMALL_BUFF)
        text4.next_to(brace1t1,DOWN,buff=MED_LARGE_BUFF)
        self.play(Write(text1))
        self.wait()
        self.add(text2[0])
        self.play(Indicate(text2[0]))
        self.wait()
        self.play(ShowCreation(arr),Write(text3))
        self.wait()
        self.play(LaggedStartMap(FadeInFromDown,(text2[1:3],brace1,brace1t1)),run_time=2)
        self.wait()
        self.add(text4)
        self.play(ShowCreation(SurroundingRectangle(text4)))
        self.wait(3)

class ep091(Scene):
    def construct(self):
        text1 = Text("偶数=质数+质数",size=0.5,gradient=(YELLOW,RED))
        text2 = TexMobject(
            "4=2+2",
            "6=3+3",
            "8=3+5",
            "10=3+7",
            "\\dots"
        )
        VGroup(text1,*text2).arrange(DOWN,buff=MED_LARGE_BUFF)

        self.add(text1)
        self.play(Indicate(text1,color=None))
        self.play(LaggedStartMap(FadeInFromDown,text2,lag_ratio=1.2),run_time=5)
        self.wait(3)

class ep085(Scene):
    def construct(self):
        AndrewWiles = ImageMobject("AndrewWiles").set_height(FRAME_HEIGHT+1).shift(0.1*BOTTOM)
        FieldsMedalFront = ImageMobject("FieldsMedalFront").set_height(FRAME_HEIGHT/2).shift(2*LEFT+UP)
        FieldsMedalFrontText = Text("菲尔兹奖", 
                        font='阿里巴巴普惠体 B',
                        size=0.5).next_to(FieldsMedalFront,DOWN)
        FieldsMedalFrontText.rect = SurroundingRectangle(
            FieldsMedalFrontText,
            color=BLUE,
            # fill_color=BLUE,
            # fill_opacity=1
            )
        self.play(FadeInFromLarge(AndrewWiles))
        self.wait()
        self.add(FieldsMedalFront)
        self.play(
            LaggedStart(
            Flash(FieldsMedalFront,num_lines=72,flash_radius=2.2),
            ShowCreation(FieldsMedalFrontText.rect),
            Write(FieldsMedalFrontText),
            lag_ratio=0.5
                )
            )
        self.wait()

class ep084(Scene):
    def construct(self):
        Taniyama = ImageMobject("Taniyama").shift(4*LEFT).scale(2)
        Taniyama.rect = SurroundingRectangle(Taniyama,color=WHITE,stroke_width=8,buff=0)
        TaniyamaGroup = Group(Taniyama, Taniyama.rect)
        TaniyamaText = Text("谷山丰", 
                        font='阿里巴巴普惠体 B',
                        size=0.5).next_to(Taniyama,DOWN)
        Wiles = ImageMobject("Wiles").shift(4*RIGHT).scale(2)
        Wiles.rect = SurroundingRectangle(Wiles,color=WHITE,stroke_width=8,buff=0)
        WilesGroup = Group(Wiles, Wiles.rect)
        WilesText = Text("怀尔斯", 
                        font='阿里巴巴普惠体 B',
                        size=0.5).next_to(Wiles,DOWN)

        text1 = Text("谷山丰猜想", 
                        font='阿里巴巴普惠体 B',
                        size=0.5,
                        color="#daab53")
        text1.rect = SurroundingRectangle(text1)

        text2 = Text("建立了椭圆曲线和模形式之间的重要联系", 
                        font='阿里巴巴普惠体 B',
                        size=0.2,
                        color="#daab53").next_to(text1,DOWN)

        VGroup(text1,text2).arrange_submobjects(DOWN,buff=0.4)

        text3 = Text("费马猜想", 
                        font='阿里巴巴普惠体 B',
                        size=0.5).next_to(text1,UP*5)
        text4 = Text("费马大定理", 
                        font='阿里巴巴普惠体 B',
                        size=0.5).next_to(text1,UP*5)

        arr1 = Arrow(text1.get_top(),text3.get_bottom())

        text1.rect = SurroundingRectangle(text1)
        self.play(FadeInFromLarge(TaniyamaGroup))
        self.play(Write(TaniyamaText))
        self.wait()

        self.play(Write(text1),run_time=2)
        self.play(ShowCreation(text1.rect),Write(text2),run_time=2)
        self.wait()

        self.play(FadeInFromLarge(WilesGroup),ShowCreation(arr1),Write(WilesText))

        self.wait()
        self.add(text3)
        self.play(Indicate(text3,scale_factor=1.5))
        self.wait()
        self.play(Transform(text3,text4))
        self.wait(5)

class ep083(Scene):
    def construct(self):
        text1 = Text("当整数 n<269 的时候，关于x,y,z的方程：", 
                        font='阿里巴巴普惠体 B',
                        size=0.5,
                        color="#daab53",
                        t2c={'n<269':WHITE }
        )
        text2 = TexMobject("x^n+y^n=z^n")
        text3 = Text("都没有正整数解。", font='阿里巴巴普惠体 B',size=0.5)

        text2.rect = SurroundingRectangle(text2)

        VGroup(text1,text2,text3).arrange_submobjects(DOWN,buff=0.4)
        self.play(Write(text1),run_time=2)
        self.wait()
        self.play(Write(text2),run_time=2)
        self.wait()
        self.play(Write(text3),run_time=2)
        self.wait()
        self.play(ShowCreation(text2.rect),run_time=2)
        self.wait(5)

class ep082(Scene):
    def construct(self):   
        Fermat = ImageMobject("Fermat").shift(5*LEFT+UP).scale(2)
        Fermat.rect = SurroundingRectangle(Fermat,color=WHITE,stroke_width=8,buff=0)
        FermatGroup = Group(Fermat, Fermat.rect)
        FermatText = Text("费马", 
                        font='阿里巴巴普惠体 B',
                        size=0.5).next_to(Fermat,DOWN)

        DiophantusMath = ImageMobject("DiophantusMath").shift(2*LEFT+0.25*BOTTOM).scale(2)
        DiophantusMath.rect = SurroundingRectangle(DiophantusMath,color=WHITE,stroke_width=4,buff=0)

        DiophantusMathText = Text("丢番图《算术》", 
                        font='阿里巴巴普惠体 B',
                        size=0.5).next_to(DiophantusMath,DOWN)

        DiophantusMathGroup = Group(DiophantusMath, DiophantusMath.rect,DiophantusMathText).scale(0.6)

        DiophantusMathText2 = Text("空白太小", 
                        font='阿里巴巴普惠体 B',
                        color=RED,
                        size=0.5).next_to(DiophantusMath.rect,RIGHT).scale(0.6).shift(0.18*BOTTOM)
        arr1 = Arrow(DiophantusMathText2.get_left(),DiophantusMath.rect.get_right(),buff=20,color=RED)
        arr1.shift(LEFT*0.1)
        text1 = TexMobject("x^2+y^2=z^2")
        text2 = Text("有无穷多整数解。", font='阿里巴巴普惠体 B',color="#daab53",size=0.5).next_to(text1,RIGHT)
        text12 = VGroup(text1,text2)
        text3 = Text("当整数n>2时，关于x,y,z的方程：", font='阿里巴巴普惠体 B', size=0.5, color = YELLOW )
        text4 = TexMobject("x^n+y^n=z^n")
        text5 = Text("没有正整数解。", font='阿里巴巴普惠体 B',size=0.5)

        self.play(FadeInFromLarge(FermatGroup))
        self.wait()
        self.play(Write(FermatText))
        self.wait()
        self.play(ShowCreation(DiophantusMathGroup))
        self.wait()
        VGroup(text12,text3,text4,text5).arrange_submobjects(DOWN,buff=0.4).shift(2*RIGHT+0.6*UP)
        text12.shift(0.36*UP)
        self.play(Write(text12),run_time=2)
        self.wait()
        self.play(Write(text3),run_time=2)
        self.wait()
        self.play(Write(text4),run_time=2)
        self.wait()
        self.play(FadeInFromLarge(text5),run_time=2)
        self.wait(3)
        self.play(ShowCreation(arr1),Write(DiophantusMathText2))
        self.wait()

class ep081(Scene):
    def construct(self):
        Diophantus = ImageMobject("Diophantus").shift(5*LEFT+UP).scale(2)
        Diophantus.rect = SurroundingRectangle(Diophantus,color=WHITE,stroke_width=8,buff=0)
        DiophantusText = Text("丢番图", 
                        font='阿里巴巴普惠体 B',
                        size=0.5).next_to(Diophantus,DOWN)
        DiophantusGroup = Group(Diophantus, Diophantus.rect,DiophantusText)

        text1 = TexMobject("x^2+y^2=z^2")
        text2 = Text("x,y,z 如果都是整数时，有多少组解呢？", font='阿里巴巴普惠体 B',color="#daab53",size=0.5)
        text3 = Text("毕达哥拉斯三角形", font='阿里巴巴普惠体 B',size=0.5)

        text = VGroup(text1,text2).arrange_submobjects(DOWN,aligned_edge = LEFT,buff=0.2).move_to(3*UP).shift(RIGHT*2)
        text3.next_to(text2,2*DOWN)

        shape1 = self.shapes(3,   4,  5,   2, 1.2)
        shape2 = self.shapes(5,  12, 13,   3, 2.2, 2)
        shape3 = self.shapes(24,  7, 25, 1.8, 2.3, 3, 2.5)
        
        VGroup(shape1,shape2,shape3).arrange_submobjects(RIGHT,buff=1).next_to(text,2.5*DOWN)
        
        self.play(FadeInFromLarge(DiophantusGroup))
        self.wait()
        self.play(Write(text1),run_time=2)
        self.wait()
        self.play(Write(text2),run_time=4)
        self.wait()

        self.play(FadeInFromLarge(shape1))
        self.wait()

        self.play(Write(text3),run_time=2)
        self.wait()

        self.play(FadeInFromLarge(shape2))
        self.wait()
        self.play(FadeInFromLarge(shape3))


        self.wait(5)

    def shapes(self,x,y,z,width=2,texSize=1,buff=0,x_axis=0):
        line1 = Line([0,0,0],[y,0,0])
        line2 = Line([y,0,0],[y,x,0])
        line3 = Line([y,x,0],[0,0,0])
        y = TexMobject("%s" % y).next_to(line1,DOWN+buff*DOWN).scale(texSize)
        x = TexMobject("%s" % x).next_to(line2,RIGHT+buff*RIGHT).scale(texSize)
        z = TexMobject("%s" % z).next_to(line3.get_center(),1.5*UP+buff*UP+LEFT*x_axis).scale(texSize)
        poly3 = VGroup(line1,line2,line3,x,y,z)
        poly3.set_width(width)
        return poly3

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