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
