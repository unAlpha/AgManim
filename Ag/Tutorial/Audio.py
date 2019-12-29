from manimlib.imports import *

class SoundTest(Scene):
    CONFIG = {"include_sound": True}
    def construct(self):
        title=TextMobject("Sound Test").to_edge(UP)
        self.wait()
        # 注意目录
        self.add_sound("sound-pd",gain=-10)
        self.play(Write(title),run_time=5)

class AudioTest(Scene):
    def construct(self):
        group_dots=VGroup(*[Dot()for _ in range(3)])
        group_dots.arrange_submobjects(RIGHT)
        for dot in group_dots:
            self.add_sound("click",gain=-10)
            self.add(dot)
            self.wait()
        self.wait()
 