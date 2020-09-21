from manimlib.imports import *

class WriteRandomScene(Scene):
    def construct(self):
        text = TextMobject("This is some text 晃是").set_width(FRAME_WIDTH-0.5)
        self.play(WriteRandom(text[0]))
        self.wait()
        self.play(UnWriteRandom(text[0]))
        self.wait(3)


class FadeFromRandomScene(Scene):
    def construct(self):
        text = TextMobject("This is some text").set_width(FRAME_WIDTH-0.5)
        self.play(FadeInFromRandomA(text[0]))
        self.wait()
        self.play(FadeOutFromRandom(text[0]))
        self.wait(3)

class GrowFromRandomScene(Scene):
    def construct(self):
        text = TextMobject("This is some text").set_width(FRAME_WIDTH-0.5)
        self.play(GrowFromRandom(text[0]))
        self.wait()
        self.play(UnGrowFromRandom(text[0]))
        self.wait(3)

class FadeRandomScene(Scene):
    def construct(self):
        text = TextMobject("This is some text").set_width(FRAME_WIDTH-0.5)
        self.play(FadeInRandom(text[0]))
        self.wait()
        self.play(FadeOutRandom(text[0]))
        self.wait(3)

class GrowRandomScene(Scene):
    def construct(self):
        text = TextMobject("This is some text").set_width(FRAME_WIDTH-0.5)
        self.play(GrowRandom(text[0]))
        self.wait()
        self.play(UnGrowRandom(text[0]))
        self.wait(3)

