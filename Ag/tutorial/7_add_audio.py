from manimlib.imports import *

class SoundTest(Scene):
    CONFIG = {"include_sound": True}
    def construct(self):
        title=TextMobject("Sound Test").to_edge(UP)
        self.wait()
        #注意目录
        self.add_sound("sound-pd",gain=-10)
        self.play(Write(title),run_time=5)
