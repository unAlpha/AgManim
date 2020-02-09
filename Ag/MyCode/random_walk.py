from random import choice
from manimlib.imports import *

class RandomWalk():
    """随机漫步类"""
    random.seed()
    def __init__(self, num_points = 10):
        self.num_points = num_points
        mu = 0
        sigma = 1.2
        xy = np.array([np.random.normal(mu, sigma, 2)])
        z0 = np.array([[0]])
        self.position = np.hstack([xy,z0])
        self.step_count = np.size(self.position,0)
     
    def fill_walk(self, u=0.1):
        while self.step_count < self.num_points:
            mu = 0
            sigma = np.random.normal(0, u, 1).tolist()[0]
            if sigma <= 0:
                sigma = 1e-6
            xy = np.array([np.random.normal(mu, sigma, 2)])
            z0 = np.array([[0]])
            step = np.hstack([xy,z0])
            next_position = self.position[-1] + step
            self.position = np.vstack((self.position,next_position))
            self.step_count+=1

class TransformFromEnding(Transform):
    def __init__(self, mobject, vector, **kwargs):
        digest_config(self, kwargs, locals())
        Animation.__init__(self, mobject, **kwargs)
    def interpolate_mobject(self, alpha):
        d_alpha = alpha - self.last_alpha
        self.last_alpha = alpha
        self.mobject.rotate_in_place(
            d_alpha*self.radians,
            self.rotation_vector
        )
        self.mobject.shift(d_alpha*self.vector)

class DrawWalk(Scene):
    def construct(self):
        plane = NumberPlane(
            axis_config = {
                "stroke_color": GRAY,
                "stroke_width": 1,
                },
            background_line_style = {
                "stroke_color": GRAY,
                "stroke_width": 2,
                "stroke_opacity": 0.5,
                }
            )
        self.add(plane)
        people = self.RandomWalkMan(people=2, num_points=30, u=60)

        thePeopleLine = self.draw_walk_line(people[0],1)
        
        for i in range(1,people[0].num_points):
            self.play(
                *[ApplyMethod(oneA.dot.move_to,oneA.position[i]) for oneA in people],
                Transform(
                    thePeopleLine,
                    self.draw_walk_line(people[0],i+1),
                    ),
                run_time=1)
        self.wait()

    def RandomWalkMan(self, people=2, num_points=10, u=10):
        all_people = VGroup()
        while people:
            oneX = RandomWalk(num_points)
            oneX.fill_walk(u/100)
            oneX.dot = Dot(radius= DEFAULT_SMALL_DOT_RADIUS).shift(oneX.position[0])
            all_people.add(oneX)
            people -=1
        return all_people

    def draw_walk_line(self, people, i):
        polyline = VMobject().set_color(RED)
        if i <= 1:
            polyline = Dot(radius=1e-6).shift(people.position[0])
        else:
            polyline.set_points_as_corners(people.position[:i])
        return polyline

        

