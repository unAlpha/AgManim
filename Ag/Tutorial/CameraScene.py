from manimlib.imports import *

class ChangePositionAndSizeCamera(MovingCameraScene):
    def construct(self):
        text = TexMobject("\\nabla\\textbf{u}").scale(3)
        square = Square()

        # Arrange the objects
        VGroup(text, square).arrange(RIGHT, buff=3)

        self.add(text, square)

        # Save the state of camera
        self.camera_frame.save_state()

        # Animation of the camera
        self.play(
            # Set the size with the width of a object
            self.camera_frame.set_width,
            text.get_width() * 1.2,
            # Move the camera to the object
            self.camera_frame.move_to,
            text)
        self.wait()

        # Restore the state saved
        self.play(Restore(self.camera_frame))

        self.play(self.camera_frame.set_height,
                  square.get_width() * 1.2, self.camera_frame.move_to, square)
        self.wait()

        self.play(Restore(self.camera_frame))

        self.wait()

"""        
如果要在其它特定的场景（指一些 Scene 的派生类，比如 GraphScene）中变更视角，
除了需要同时继承该类和 MovingCameraScene 类之外，
还需要自己定义一个 setup 方法，否则会报错。举个例子。
""" 

class ChangePositionAndSizeCameraInAnotherScene(GraphScene, MovingCameraScene):
    CONFIG = {
        "y_max": 50,
        "y_min": 0,
        "x_max": 7,
        "x_min": 0,
        "y_tick_frequency": 5,
        "x_tick_frequency": 0.5,
    }

    # Setup the scenes
    def setup(self):
        GraphScene.setup(self)
        MovingCameraScene.setup(self)

    def construct(self):
        self.setup_axes(animate=False)

        graph = self.get_graph(lambda x: x**2, color=GREEN, x_min=0, x_max=7)
        dot_at_start_graph = Dot().move_to(graph.points[0])
        dot_at_end_grap = Dot().move_to(graph.points[-1])

        self.add(graph, dot_at_end_grap, dot_at_start_graph)

        self.play(self.camera_frame.scale, .5, self.camera_frame.move_to,
                  dot_at_start_graph)

        self.play(self.camera_frame.move_to, dot_at_end_grap)
        self.wait()

class RemoveAllObjectsInScreen(Scene):
    def construct(self):
        self.play(
            ShowCreation(
                VGroup(*[
                    VGroup(*[Dot() for i in range(30)]).arrange(RIGHT)
                    for j in range(10)
                ]).arrange(DOWN)))
        self.play(*[FadeOut(mob) for mob in self.mobjects]
                  # All mobjects in the screen are saved in self.mobjects
                  )

        self.wait()

class ZoomedSceneExample(ZoomedScene):
    CONFIG = {
        "zoom_factor": 0.3,
        "zoomed_display_height": 1,
        "zoomed_display_width": 6,
        "image_frame_stroke_width": 20,
        "zoomed_camera_config": {
            "default_frame_stroke_width": 3,
        },
    }

    def construct(self):
        # Set objects
        dot = Dot().shift(UL * 2)

        image = ImageMobject(np.uint8([[0, 100, 30, 200], [255, 0, 5, 33]]))
        image.set_height(7)
        frame_text = TextMobject("Frame", color=PURPLE).scale(1.4)
        zoomed_camera_text = TextMobject("Zommed camera", color=RED).scale(1.4)

        self.add(image, dot)

        # Set camera
        zoomed_camera = self.zoomed_camera
        zoomed_display = self.zoomed_display
        frame = zoomed_camera.frame
        zoomed_display_frame = zoomed_display.display_frame

        frame.move_to(dot)
        frame.set_color(PURPLE)

        zoomed_display_frame.set_color(RED)
        zoomed_display.shift(DOWN)

        # brackground zoomed_display
        zd_rect = BackgroundRectangle(
            zoomed_display,
            fill_opacity=0,
            buff=MED_SMALL_BUFF,
        )

        self.add_foreground_mobject(zd_rect)

        # animation of unfold camera
        unfold_camera = UpdateFromFunc(
            zd_rect, lambda rect: rect.replace(zoomed_display))

        frame_text.next_to(frame, DOWN)

        self.play(ShowCreation(frame), FadeInFromDown(frame_text))

        # Activate zooming
        self.activate_zooming()

        self.play(
            # You have to add this line
            self.get_zoomed_display_pop_out_animation(),
            unfold_camera)

        zoomed_camera_text.next_to(zoomed_display_frame, DOWN)
        self.play(FadeInFromDown(zoomed_camera_text))

        # Scale in     x   y  z
        scale_factor = [0.5, 1.5, 0]

        # Resize the frame and zoomed camera
        self.play(frame.scale, scale_factor,
                  zoomed_display.scale, scale_factor,
                  FadeOut(zoomed_camera_text), FadeOut(frame_text))

        # Resize the frame
        self.play(frame.scale, 3, frame.shift, 2.5 * DOWN)

        # Resize zoomed camera
        self.play(ScaleInPlace(zoomed_display, 2))

        self.wait()

        self.play(
            self.get_zoomed_display_pop_out_animation(),
            unfold_camera,
            # -------> Inverse
            rate_func=lambda t: smooth(1 - t),
        )
        self.play(
            Uncreate(zoomed_display_frame),
            FadeOut(frame),
        )
        self.wait()
