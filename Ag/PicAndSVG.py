from manimlib.imports import *

class ShowPicture(Scene):
        CONFIG = {
            'pic1' : 'assets\\pic\\pic1.png',
            'facebook' : 'assets\\pic\\Facebook.png',
            'power' : 'assets\\pic\\Power.png'
        }
        def construct(self):
            pic1 = ImageMobject(self.pic1)
            pic1.set_height(1)
            facebook = ImageMobject(self.facebook)
            facebook.set_height(1)
            power = ImageMobject(self.power)
            power.set_height(1)

            facebook.shift(UP*0.6)
            pic1.next_to(facebook, LEFT)
            power.next_to(facebook, RIGHT)

            invokerText = TextMobject("I N V O K E R")
            invokerText.set_width(3.2)
            invokerText.next_to(facebook, DOWN)

            self.play(FadeInFromLarge(pic1), run_time=1.5)
            self.play(FadeInFromLarge(facebook), run_time=1.5)
            self.play(FadeInFromLarge(power), run_time=1.5)

            self.play(Write(invokerText), run_time=1.5)
            self.wait(1)
