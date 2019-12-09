from manimlib.imports import *

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