from manimlib.imports import *

class HomotopyExample(Scene):
    def construct(self):
        def plane_wave_homotopy(x, y, z, t):
            norm = get_norm([x, y])
            tau = interpolate(5, -5, t) + norm/FRAME_X_RADIUS
            alpha = sigmoid(tau)
            return [x, y + 0.5*np.sin(2*np.pi*alpha)-t*SMALL_BUFF/2, z]

        mobjects=VGroup(
            TextMobject("Text").scale(3),
            Square(),
        ).arrange_submobjects(RIGHT,buff=2)

        self.add(mobjects)
        self.play(
            *[Homotopy(
                plane_wave_homotopy,
                mob
            ) for mob in mobjects]
        )
        self.wait(0.3)

class PhaseFlowExample(Scene):
    def construct(self):
        def func(t):
            return t*0.5*RIGHT

        mobjects=VGroup(
            TextMobject("Text").scale(3),
            Square(),
        ).arrange_submobjects(RIGHT,buff=2)

        self.play(
            *[PhaseFlow(
                func, mob,
                run_time = 2,
            )for mob in mobjects]
        )

        self.wait()

class MoveAlongPathExample(Scene):
    def construct(self):
        line=Line(ORIGIN,RIGHT*FRAME_WIDTH,buff=1)
        line.move_to(ORIGIN)
        dot=Dot()
        dot.move_to(line.get_start())

        self.add(line,dot)
        self.play(
            MoveAlongPath(dot,line)
        )
        self.wait(0.3)

class RotatingExample(Scene):
    def construct(self):
        square=Square().scale(2)
        self.add(square)

        self.play(
            Rotating(
                square,
                radians=PI/4,
                run_time=2
            )
        )
        self.wait(0.3)
        self.play(
            Rotating(
                square,
                radians=PI,
                run_time=2,
                axis=RIGHT
            )
        )
        self.wait(0.3)

class RotateExample(Scene):
    def construct(self):
        square=Square().scale(2)
        self.add(square)

        self.play(
            Rotate(
                square,
                PI/4,
                run_time=2
            )
        )
        self.wait(0.3)
        self.play(
            Rotate(
                square,
                PI,
                run_time=2,
                axis=RIGHT
            )
        )
        self.wait(0.3)