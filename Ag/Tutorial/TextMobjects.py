from manimlib.imports import *

class RotateAndHighlight(Scene):
#Rotation of text and highlighting with surrounding geometries
    def construct(self):
        square=Square(side_length=5,fill_color=YELLOW, fill_opacity=1)
        label=TextMobject("Text at an angle")
        label.bg=BackgroundRectangle(label,fill_opacity=1)
        label_group=VGroup(label.bg,label) #Order matters
        label_group.rotate(TAU/8)
        label2=TextMobject("Boxed text",color=BLACK)
        label2.bg=SurroundingRectangle(label2,color=BLUE,fill_color=RED, fill_opacity=.5)
        label2_group=VGroup(label2,label2.bg)
        label2_group.next_to(label_group,DOWN)
        label3=TextMobject("Rainbow")
        label3.scale(2)
        label3.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        label3.to_edge(DOWN)
 
        self.add(square)
        self.play(FadeIn(label_group))
        self.play(FadeIn(label2_group))
        self.play(FadeIn(label3))


class WriteText(Scene): 
    def construct(self): 
        text = TextMobject("This is a regular text")
        text_underline = Underline(text)
        text_underline.points=np.array([[ -2.4,  -0.3,  0.],
                                        [ -0.8,  -0.3,  0.],
                                        [  0.8,  0.3,  0.],
                                        [  2.4,  0.3,  0.]])
        print(text_underline.points)
        self.play(Write(text))
        self.add(text_underline)
        self.wait(3)

class TypesOfText(Scene): 
    def construct(self): 
        tipesOfText = TextMobject("""
            This is a regular text,
            $this is a formula$,
            $$this is a formula$$
            """)
        self.play(Write(tipesOfText))
        self.wait(3)

class TypesOfText2(Scene): 
    def construct(self): 
        tipesOfText = TextMobject("""
            This is a regular text,
            $\\frac{x}{y}$,
            $$x^2+y^2=a^2,$$
            $x^2+y^2=a^2$
            """)
        self.play(Write(tipesOfText))
        self.wait(3)

class SizeTextOnLaTeX(Scene):
    def construct(self):
        #Huge 字的大小
        textHuge = TextMobject("{\\Huge Huge Text 012.\\#!?} Text")
        texthuge = TextMobject("{\\huge huge Text 012.\\#!?} Text")
        textLARGE = TextMobject("{\\LARGE LARGE Text 012.\\#!?} Text")
        textLarge = TextMobject("{\\Large Large Text 012.\\#!?} Text")
        textlarge = TextMobject("{\\large large Text 012.\\#!?} Text")
        textNormal = TextMobject("{\\normalsize normal Text 012.\\#!?} Text")
        textsmall = TextMobject("{\\small small Text 012.\\#!?} Texto normal")
        textfootnotesize = TextMobject("{\\footnotesize footnotesize Text 012.\\#!?} Text")
        textscriptsize = TextMobject("{\\scriptsize scriptsize Text 012.\\#!?} Text")
        texttiny = TextMobject("{\\tiny tiny Texto 012.\\#!?} Text normal")
        textHuge.to_edge(UP)
        texthuge.next_to(textHuge,DOWN,buff=0.1)
        textLARGE.next_to(texthuge,DOWN,buff=0.1)
        textLarge.next_to(textLARGE,DOWN,buff=0.1)
        textlarge.next_to(textLarge,DOWN,buff=0.1)
        textNormal.next_to(textlarge,DOWN,buff=0.1)
        textsmall.next_to(textNormal,DOWN,buff=0.1)
        textfootnotesize.next_to(textsmall,DOWN,buff=0.1)
        textscriptsize.next_to(textfootnotesize,DOWN,buff=0.1)
        texttiny.next_to(textscriptsize,DOWN,buff=0.1)
        self.add(textHuge,texthuge,textLARGE,textLarge,textlarge,textNormal,textsmall,textfootnotesize,textscriptsize,texttiny)
        self.wait(3)

class TextFonts(Scene):
    def construct(self):
        textNormal = TextMobject("{Roman serif text 012.\\#!?} Text")
        textItalic = TextMobject("\\textit{Italic text 012.\\#!?} Text")
        textTypewriter = TextMobject("\\texttt{Typewritter text 012.\\#!?} Text")
        textBold = TextMobject("\\textbf{Bold text 012.\\#!?} Text")
        textSL = TextMobject("\\textsl{Slanted text 012.\\#!?} Text")
        textSC = TextMobject("\\textsc{Small caps text 012.\\#!?} Text")
        textNormal.to_edge(UP)
        textItalic.next_to(textNormal,DOWN,buff=.5)
        textTypewriter.next_to(textItalic,DOWN,buff=.5)
        textBold.next_to(textTypewriter,DOWN,buff=.5)
        textSL.next_to(textBold,DOWN,buff=.5)
        textSC.next_to(textSL,DOWN,buff=.5)
        self.add(textNormal,textItalic,textTypewriter,textBold,textSL,textSC)
        self.wait(3)

class TypesText1(Scene): 
    def construct(self): 
        tipesOfText1 = TexMobject(
            "\\frac{\\text{d}y}{\\text{d}x}=f\\left( x \\right) g\\left( y \\right) ",
            "\\int{\\frac{\\text{d}y}{g\\left( y \\right)}}=\\int{f\\left( x \\right) \\text{d}x}+C"
            )
        # 推荐这个方法
        tipesOfText2 = TextMobject(
            "$$\\frac{\\text{d}y}{\\text{d}x}=f\\left( x \\right) g\\left( y \\right)$$",
            "$$\\int{\\frac{\\text{d}y}{g\\left( y \\right)}}=\\int{f\\left( x \\right) \\text{d}x}+C$$"
            )
        tipesOfText3 = TexMobject(
            r"\frac{\text{d}y}{\text{d}x}=f\left( x \right) g\left( y \right)",
            r"\int{f\left( x \right) \text{d}x}+C"
            )
        tipesOfText1[0].set_color(RED)
        tipesOfText2[0].set_color(YELLOW)
        tipesOfText3.set_color(BLUE)

        tipesOfText2.set_color_by_tex("\\frac",PINK)
        tipesOfText1.shift(2*UP)
        tipesOfText2.next_to(tipesOfText1,DOWN,buff=1.5)
        tipesOfText3[0].next_to(tipesOfText2[0],RIGHT,buff=1)
        tipesOfText3[1].next_to(tipesOfText2[0],LEFT,buff=1)

        self.play(Write(tipesOfText1))
        self.play(Write(tipesOfText2))
        self.play(Write(tipesOfText3))
        self.wait()

class TypesText2(Scene): 
    def construct(self): 
        tipesOfText4 = TextMobject("""
            $$\\frac{\\text{d}y}{\\text{d}x}=f\\left( x \\right) g\\left( y \\right)$$
            $$\\int{\\frac{\\text{d}y}{g\\left( y \\right)}}=\\int{f\\left( x \\right) \\text{d}x}+C$$
            """)
        self.play(Write(tipesOfText4))
        self.wait()

    
class TypesText3(Scene): 
    def construct(self): 
        tipesOfText4 = TextMobject("""
                $$
                \\boldsymbol{A}_{m\\times n}=\\left[ \\begin{matrix}{l}
                    a_{11}&		a_{12}&		\\cdots&		a_{1n}\\\\
                    a_{21}&		a_{22}&		\\cdots&		a_{2n}\\\\
                    \\vdots&	\\vdots&	\\ddots&		\\vdots\\\\
                    a_{m1}&		a_{m2}&		\\cdots&		a_{mn}\\\\
                \\end{matrix} \\right] =\\left[ a_{ij} \\right] 
                $$
            """,
            background_stroke_width=0)
        self.play(Write(tipesOfText4))
        self.wait()

COLOR_P="#3EFC24"

class TextColor(Scene):
    def construct(self):
        text = TextMobject("A","B","C","D","E","F")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(ORANGE)
        text[4].set_color("#DC28E2") #Hexadecimal color
        text[5].set_color(COLOR_P)
        screen_grid = ScreenGrid()
        self.add(screen_grid)
        self.play(Write(text))
        self.wait(2)

class FormulaColor1(Scene): 
    def construct(self):
        text = TexMobject("x","=","{a","\\over","b}")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(ORANGE)
        text[4].set_color("#DC28E2")
        screen_grid = ScreenGrid()
        self.add(screen_grid)
        self.play(Write(text))
        self.wait(2)

class FormulaColor2(Scene): 
    def construct(self): 
        text = TexMobject("x","=","\\frac{a}{b}")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        self.play(Write(text))
        self.wait(2)

class FormulaColor3(Scene): 
    def construct(self):
        text = TexMobject("\\sqrt{","\\int_{","a}^","{b}","\\left(","\\frac{x}{y}","\\right)","dx}")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(YELLOW)
        text[4].set_color(PINK)
        text[5].set_color(ORANGE)
        text[6].set_color(PURPLE)
        text[7].set_color(MAROON)
        self.play(Write(text))
        self.wait(2)

class FormulaColor3Fixed(Scene): 
    def construct(self): 
        text = TexMobject("\\sqrt{","\\int_{","a}^","{b}","\\left(","\\frac{x}{y}","\\right)","dx.}")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(YELLOW)
        text[4].set_color(PINK)
        text[5].set_color(ORANGE)
        text[6].set_color(PURPLE)
        text[7].set_color(MAROON)
        self.play(Write(text))
        self.wait(3)

class FormulaColor3Fixed2(Scene): 
    def construct(self): 
        text = TexMobject("\\sqrt{","\\int_","{a}^","{b}","{\\left(","{x","\\over","y}","\\right)}","d","x",".}")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(YELLOW)
        text[4].set_color(PINK)
        text[5].set_color(ORANGE)
        text[6].set_color(PURPLE)
        text[7].set_color(MAROON)
        text[8].set_color(TEAL)
        text[9].set_color(GOLD)
        self.play(Write(text))
        self.wait(3)

class FormulaColor4(Scene): 
    def construct(self): 
        text = TexMobject("\\sqrt{","\\int_","{a","+","c}^","{b}","{\\left(","{x","\\over","y}","\\right)}","d","x",".}")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(YELLOW)
        text[4].set_color(PINK)
        text[5].set_color(ORANGE)
        text[6].set_color(PURPLE)
        text[7].set_color(MAROON)
        text[8].set_color(TEAL)
        text[9].set_color(GOLD)
        text[10].set_color(GRAY)
        text[11].set_color(RED)
        self.play(Write(text))
        self.wait(3)

class FormulaColor5(Scene): 
    def construct(self): 
        text = TexMobject("\\sqrt{","\\int_","{a","+","c}^","{b}","{\\left(","{x","\\over","y}","\\right)}","d","x",".}")
        for i,color in zip(text,[PURPLE,BLUE,GREEN,YELLOW,PINK]):
            i.set_color(color)
        self.play(Write(text))
        self.wait(3)


class ColorByCaracter(Scene):
	def construct(self):
		text = TexMobject("{d","\\over","d","x","}","\\int_","{a}^","{","x","}","f(","t",")d","t","=","f(","x",")")
		text.set_color_by_tex("x",RED)
		self.play(Write(text))
		self.wait(2)

class ColorByCaracterFixed(Scene): 
	def construct(self):
		text = TexMobject("{d","\\over","d","x","}","\\int_","{a}^","{","x","}","f(","t",")d","t","=","f(","x",")")
		text.set_color_by_tex("x",RED)
		text[6].set_color(RED)
		text[8].set_color(WHITE)
		self.play(Write(text))
		self.wait(2)
	
class ListFor(Scene): 
    def construct(self): #no usar siempre frac
        text = TexMobject("[0]","[1]","[2]","[3]","[4]","[5]","[6]","[7]")
        for i in [0,1,3,4]:
        	text[i].set_color(RED)
        self.play(Write(text))
        self.wait(3)

class ForRange1(Scene): 
    def construct(self): #no usar siempre frac
        text = TexMobject("[0]","[1]","[2]","[3]","[4]","[5]","[6]","[7]")
        for i in range(3):
        	text[i].set_color(RED)
        self.play(Write(text))
        self.wait(3)

class ForRange2(Scene): 
    def construct(self): #no usar siempre frac
        text = TexMobject("[0]","[1]","[2]","[3]","[4]","[5]","[6]","[7]")
        for i in range(2,6):
        	text[i].set_color(RED)
        self.play(Write(text))
        self.wait(3)

class ForTwoVariables(Scene): 
    def construct(self): #no usar siempre frac
        text = TexMobject("[0]","[1]","[2]","[3]","[4]","[5]","[6]","[7]")
        for i,color in [(2,RED),(4,PINK)]:
        	text[i].set_color(color)
        self.play(Write(text))
        self.wait(3)

class ChangeSize(Scene):
    def construct(self):
        text = TexMobject("\\sum_{i=0}^n i=\\frac{n(n+1)}{2}")
        self.add(text)
        self.wait()
        #直接放大
        text.scale_in_place(2)
        self.wait(2)

class AddAndRemoveText(Scene):
    def construct(self):
        text = TextMobject("Text or object")
        self.wait()
        self.add(text)
        self.wait()
        self.remove(text)
        self.wait()

class FadeText(Scene):
    def construct(self):
        text = TextMobject("Text or object")
        self.play(FadeIn(text))
        self.wait()
        self.play(FadeOut(text),run_time=1)
        self.wait()

class FadeTextFromDirection(Scene):
    def construct(self):
        text = TextMobject("Text or object")
        self.play(FadeInFrom(text,DOWN),run_time=1)
        self.wait()

class GrowObjectFromCenter(Scene):
    def construct(self):
        text = TextMobject("Text or object")
        self.play(GrowFromCenter(text),run_time=1)
        self.wait()

class ShowCreationObject(Scene):
    def construct(self):
        text = TextMobject("Text or object")
        t2=text.copy()
        t2.next_to(text,DOWN)
        self.play(ShowCreation(text),Write(t2),run_time=1)
        self.wait()

class ColoringText(Scene):
    def construct(self):
        text = TextMobject("Text or object")
        self.add(text)
        self.wait(0.5)
        #err
        for letter in text:
            self.play(LaggedStart(
                ApplyMethod, letter,
                lambda m : (m.set_color, YELLOW),
                run_time = 0.12
            ))
        self.wait(0.5)

class CrossText1(Scene):
    def construct(self):
        text = TexMobject("\\sum_{i=1}^{\\infty}i","=","-\\frac{1}{2}")
        cross = Cross(text[2])
        cross.set_stroke(RED, 6)
        self.play(Write(text))
        self.wait(.5)
        self.play(ShowCreation(cross))
        self.wait(2)

class CrossText2(Scene):
    def construct(self):
        text = TexMobject("\\sum_{i=1}^{\\infty}i","=","-\\frac{1}{2}")
        eq = VGroup(text[1],text[2])
        cross = Cross(eq)
        cross.set_stroke(RED, 6)
        self.play(Write(text))
        self.wait(.5)
        self.play(ShowCreation(cross))
        self.wait(2)

class FrameBox1(Scene):
    def construct(self):
        text=TexMobject(
            "\\hat g(", "f", ")", "=", "\\int", "_{t_1}", "^{t_{2}}",
            "g(", "t", ")", "e", "^{-2\\pi i", "f", "t}", "dt"
        )
        frameBox = SurroundingRectangle(text[4], buff = 0.5*SMALL_BUFF)
        self.play(Write(text))
        self.wait(.5)
        self.play(ShowCreation(frameBox))
        self.wait(2)

class FrameBox2(Scene):
    def construct(self):
        text=TexMobject(
            "\\hat g(", "f", ")", "=", "\\int", "_{t_1}", "^{t_{2}}",
            "g(", "t", ")", "e", "^{-2\\pi i", "f", "t}", "dt"
        )
        seleccion=VGroup(text[4],text[5],text[6])
        frameBox = SurroundingRectangle(seleccion, buff = 0.5*SMALL_BUFF)
        frameBox.set_stroke(GREEN,9)
        self.play(Write(text))
        self.wait(.5)
        self.play(ShowCreation(frameBox))
        self.wait(2)

class BraceText1(Scene):
    def construct(self):
        text=TexMobject(
            "\\frac{d}{dx}f(x)g(x)=","f(x)\\frac{d}{dx}g(x)","+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        brace_top = Brace(text[1], UP, buff = 5*SMALL_BUFF)
        brace_bottom = Brace(text[3], DOWN, buff = SMALL_BUFF)
        text_top = brace_top.get_text("$g'f$")
        text_bottom = brace_bottom.get_text("$f'g$")
        self.play(
            GrowFromCenter(brace_top),
            GrowFromCenter(brace_bottom),
            FadeIn(text_top),
            FadeIn(text_bottom)
            )
        self.wait()