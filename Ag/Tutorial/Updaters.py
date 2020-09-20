from manimlib.imports import *

class addPointsLine(Scene):
    def construct(self):
        dot = Dot(point=LEFT_SIDE+RIGHT,radius= 0.3, color= RED)
        path = VMobject()
        path.set_points_as_corners([dot.get_center(),dot.get_center()+UP*0.01])
        def update_path(path):
            previus_path = path.copy()
            previus_path.add_points_as_corners([dot.get_center()])
            path.become(previus_path)
        path.add_updater(update_path)
        self.add(path,dot)
        self.play(dot.shift,RIGHT*10, run_time=3 ,rate_func= linear)


class UpdatersExample(Scene):
    def construct(self):
        decimal = DecimalNumber(
            0,
            #显示省略号
            show_ellipsis=True,
            #小数位数
            num_decimal_places=3,
            #包括符号
            include_sign=True,
        )
        square = Square().to_edge(UP)

        decimal.add_updater(lambda d: d.next_to(square, RIGHT))
        decimal.add_updater(lambda d: d.set_value(square.get_center()[1]))
        
        self.add(square, decimal)
        self.play(
            square.to_edge, DOWN,
            rate_func=there_and_back,
            run_time=5,
        )
        self.wait()

class AddUpdaterFail(Scene):
    def construct(self):
        dot = Dot()
        text = TextMobject("Label")\
               .next_to(dot,RIGHT,buff=SMALL_BUFF)

        self.add(dot,text)

        self.play(dot.shift,UP*2)
        self.wait()

class AddUpdater1(Scene):
    def construct(self):
        dot = Dot()
        text = TextMobject("Label")\
               .next_to(dot,RIGHT,buff=SMALL_BUFF)

        self.add(dot,text)

        # Update function
        def update_text(obj):
            obj.next_to(dot,LEFT,buff=SMALL_BUFF)

        # Add update function to the objects
        text.add_updater(update_text)

        # Add the object again
        self.add(text)

        self.play(dot.shift,UP*2)

        # Remove update function
        text.remove_updater(update_text)

        self.wait()

class AddUpdater2(Scene):
    def construct(self):
        dot = Dot()
        text = TextMobject("Label")\
               .next_to(dot,RIGHT,buff=SMALL_BUFF)

        self.add(dot,text)

        # Add update function to the objects
        text.add_updater(lambda m: m.next_to(dot,RIGHT,buff=SMALL_BUFF))

        # Add the object again
        self.add(text)

        self.play(dot.shift,UP*2)

        # Remove update function
        text.clear_updaters()

        self.wait()

class AddUpdater3(Scene):
    def construct(self):
        dot = Dot()
        text = TextMobject("Label")\
               .next_to(dot,RIGHT,buff=SMALL_BUFF)

        self.add(dot,text)

        def update_text(obj):
            obj.next_to(dot,RIGHT,buff=SMALL_BUFF)

        # Only works in play
        self.play(
                dot.shift,UP*2,
                UpdateFromFunc(text,update_text)
            )

        self.wait()

class UpdateNumber(Scene):
    def construct(self):
        number_line = NumberLine(x_min=-2,x_max=2)
        triangle = RegularPolygon(3,start_angle=-PI/2)\
                   .scale(0.2)\
                   .next_to(number_line.get_left(),UP,buff=SMALL_BUFF)
        decimal = DecimalNumber(
                0,
                num_decimal_places=1,
                include_sign=True,
                unit="\\rm cm", # Change this with None
            )

        decimal.add_updater(lambda d: d.next_to(triangle, UP*0.5))
        # [0] [1] [2]表示x y z
        decimal.add_updater(lambda d: d.set_value(triangle.get_center()[0]))
        # You can get the value of decimal with: .get_value()

        self.add(number_line,triangle,decimal)

        self.play(
                triangle.shift,RIGHT*2,
                rate_func=there_and_back, # Change this with: linear,smooth
                run_time=5
            )

        self.wait()

class UpdateValueTracker1(Scene):
    def construct(self):
        # 要变化的Value
        theta = ValueTracker(PI/2)
        line_1= Line(ORIGIN,RIGHT*3,color=RED)
        line_2= Line(ORIGIN,RIGHT*3,color=GREEN)

        line_2.rotate(theta.get_value(),about_point=ORIGIN)

        line_2.add_updater(lambda m: m.set_angle(theta.get_value()))

        self.add(line_1,line_2)

        self.play(theta.increment_value,PI/2)

        self.wait()

class UpdateValueTracker2(Scene):
    CONFIG={
        "line_1_color":ORANGE,
        "line_2_color":PINK,
        "lines_size":3.5,
        "theta":PI/2,
        "increment_theta":PI/2,
        "final_theta":PI,
        "radius":0.2,
        "radius_color":YELLOW,
    }
    def construct(self):
        # Set objets
        theta = ValueTracker(self.theta)
        line_1= Line(ORIGIN,RIGHT*self.lines_size,color=self.line_1_color)
        line_2= Line(ORIGIN,RIGHT*self.lines_size,color=self.line_2_color)

        line_2.rotate(theta.get_value(),about_point=ORIGIN)
        line_2.add_updater(lambda m: m.set_angle(theta.get_value()))

        angle= Arc(
                    radius=self.radius,
                    start_angle=line_1.get_angle(),
                    angle =line_2.get_angle(),
                    color=self.radius_color
            )

        # Show the objects
        self.play(*[
                ShowCreation(obj) for obj in [line_1,line_2,angle]
            ])

        # Set update function to angle
        angle.add_updater(
                    lambda m: m.become(
                            Arc(
                                radius=self.radius,
                                start_angle=line_1.get_angle(),
                                angle =line_2.get_angle(),
                                color=self.radius_color
                            )
                        )
            )
        # Remember to add the objects again to the screen 
        # 需要再次add()
        # when you add the add_updater method.
        self.add(angle)

        self.play(theta.increment_value,self.increment_theta)
        # self.play(theta.set_value,self.final_theta)

        self.wait()
        
# dt = 1 / fps

class UpdateFunctionWithDt1(Scene):
    CONFIG={
        "amp": 2.3,
        "t_offset": 0,
        # 移动的速度
        "rate": TAU/4,
        "sine_graph_config":{
            "x_min": -TAU/2,
            "x_max": TAU/2,
            "color": RED,
            },
    }
 
    def construct(self):
        # 更新函数, dt是一个特殊的存在,根据视频的长度来的
        # 如果不想用dt,可以用def update_curve(c, alpha):
        def update_curve(fig, dt):
            rate = self.rate * dt
            # 变化对象
            fig.become(self.get_sin_graph(self.t_offset + rate))
            # Every frame, the t_offset increase rate / fps
            self.t_offset += rate
            # 移动对象
            fig.shift(np.array([-self.t_offset,0,0]))
   
        sinGraph = self.get_sin_graph(0)

        self.play(ShowCreation(sinGraph))

        print(f"fps: {self.camera.frame_rate}")
        print(f"dt: {1 / self.camera.frame_rate}")
        print(f"rate: {self.rate / self.camera.frame_rate}")
        print(f"cy_start: {sinGraph.points[0][1]}")
        print(f"cy_end:   {sinGraph.points[-1][1]}")
        print(f"t_offset: {self.t_offset}\n")

        sinGraph.add_updater(update_curve)
        self.add(sinGraph)

        # The animation begins
        self.wait(4)
        
        sinGraph.remove_updater(update_curve)
        self.wait()

        print(f"cy_start:  {sinGraph.points[0][1]}")
        print(f"cy_end:    {sinGraph.points[-1][1]}")
        print(f"t_offset: {self.t_offset}\n")

    def get_sin_graph(self, dx):
        sineGraph = FunctionGraph(
                lambda x: self.amp * np.sin(x - dx),
                **self.sine_graph_config
                )
        return sineGraph

class UpdateFunctionMydt(Scene):
    CONFIG={
        "amp": 2.3,
        "sine_graph_config":{
            "x_min": -TAU,
            "x_max": TAU,
            "color": RED,
            },
    }
    def construct(self):
        theta = ValueTracker(-TAU)
        sinGraph = self.get_sin_graph(theta.get_value())

        def update_curve(fig):
            vlu = theta.get_value()
            fig.become(self.get_sin_graph(vlu))
            fig.shift(np.array([-vlu,0,0]))
        sinGraph.add_updater(update_curve)

        self.play(ShowCreation(sinGraph))
        self.add(sinGraph)
        self.wait()
        # 在全长的时间里折成rate_func的0到1内,点的密度会改变
        self.play(theta.increment_value,TAU,rate_func=linear,run_time=3)
        # The animation begins
        sinGraph.remove_updater(update_curve)
        self.wait()

    def get_sin_graph(self, dx):
        sinGraph = FunctionGraph(
                lambda x: self.amp * np.sin(x - dx),
                **self.sine_graph_config
                )
        return sinGraph

class PlanetScene1(Scene):
    def construct(self):
        self.t_offset=0
        orbit=Ellipse(color=GREEN).scale(5)
        planet=Dot()
        text=TextMobject("Update function")

        planet.move_to(orbit.point_from_proportion(0))

        def update_planet(mob,dt):
            rate=dt*0.2
            # 0.8为一圈的百分比
            if self.t_offset>0.8:
                rate = 0
            mob.move_to(orbit.point_from_proportion(((self.t_offset + rate))%1))
            self.t_offset += rate

        planet.add_updater(update_planet)
        self.add(orbit,planet)
        self.wait(3)
        self.play(Write(text))
        self.wait(3)

t_offset=0
c_t=0
class PlanetScene2(Scene):
    def construct(self):
        # FPS
        velocity_factor=0.2
        frame_rate = self.camera.frame_rate
        self.dt=1/frame_rate
        # ----------------
        orbit=Ellipse(color=GREEN).scale(2.5)
        planet=Dot()
        text=TextMobject("Update function")

        planet.move_to(orbit.point_from_proportion(0))
        reference_planet=planet.copy()
        reference_planet.set_color(RED)
        self.add(reference_planet)
        def update_planet(mob,dt):
            global t_offset,c_t
            if dt==0 and c_t==0:
                rate=velocity_factor*self.dt
                c_t+=1
            else:
                rate=dt*velocity_factor
            if dt>0:
                c_t=0
            mob.move_to(orbit.point_from_proportion(((t_offset + rate))%1))
            t_offset += rate

        planet.add_updater(update_planet)
        self.add(orbit,planet)
        self.wait(3)
        self.play(Write(text))
        self.wait(3)
        self.play(Write(text,rate_func=lambda t:smooth(1-t)))
        self.wait(3)


class UpdateCurve(Scene):
    def construct(self):
        def func(dx=1):
            return FunctionGraph(lambda x: 2*np.exp(-2 * (x - dx) ** 2))

        cmob = func()
        axes=Axes(y_min=-3, y_max=3)
 
        def update_curve(mob, alpha):
            dx = interpolate(1, 4, alpha)
            c_c = func(dx)
            cmob.become(c_c)
 
        self.play(ShowCreation(axes), ShowCreation(cmob))
        self.wait()
        self.play(UpdateFromAlphaFunc(cmob,update_curve),rate_func=there_and_back,run_time=4)
        self.wait()

class UpdateSinCurve(Scene):
    def construct(self):
        def f(dx=1):
            return FunctionGraph(lambda x: np.sin(x-dx),x_min=-TAU/2,x_max=TAU/2)

        c = f()
        axes=Axes(y_min=-3, y_max=3)

        # 摆掉dt的限制
        def update_curve(c, alpha):
            dx = interpolate(1, 10, alpha)
            c_c = f(dx)
            c.become(c_c)
 
        self.play(ShowCreation(axes), ShowCreation(c))
        self.wait()
        self.play(UpdateFromAlphaFunc(c,update_curve),rate_func=linear,run_time=4)
        self.wait()
        
class InterpolateColorScene(Scene):
    def construct(self):
        shape = Square(fill_opacity=1).scale(2)
        shape.set_color(RED)

        def update_color(mob,alpha):
            # 插值单个值
            dcolor = interpolate(0,mob.alpha_color,alpha)
            mob.set_color(self.interpolate_color_mob(mob.initial_state,shape.new_color,dcolor))

        self.add(shape)
        self.change_init_values(shape,WHITE,1)
        self.play(UpdateFromAlphaFunc(shape,update_color))

        self.change_init_values(shape,PINK,1)
        self.play(UpdateFromAlphaFunc(shape,update_color))
        self.wait()
    
    # 颜色初始化
    def change_init_values(self,mob,color,alpha):
        mob.initial_state = mob.copy()
        mob.new_color = color
        mob.alpha_color = alpha

    # 插值RGB
    def interpolate_color_mob(self,mob,color,alpha):
        # 返回args1和args2之前的插值颜色RGB
        return interpolate_color(mob.get_color(),color,alpha)


class FadeToColorExample(Scene):
    def construct(self):
        text = TextMobject("Text")\
               .set_width(FRAME_WIDTH)

        colors=[RED,PURPLE,GOLD,TEAL]

        self.add(text)

        for color in colors:
            self.play(FadeToColor(text,color))

        self.wait(0.3)


class SuccessionExample1Fail(Scene):
    def construct(self):
        number_line=NumberLine(x_min=-2,x_max=2)
        text=TextMobject("Text")\
             .next_to(number_line,DOWN)
        dashed_line=DashedLine(
                                number_line.get_left(),
                                number_line.get_right(),
                                color=YELLOW,
                              ).set_stroke(width=11)

        self.add(number_line)
        self.wait(0.3)
        self.play(ShowCreationThenDestruction(dashed_line),run_time=5)
        self.play(Write(text))

        self.wait()


class SuccessionExample1(Scene):
    def construct(self):
        number_line=NumberLine(x_min=-2,x_max=2)
        text=TextMobject("Text")\
             .next_to(number_line,DOWN)
        dashed_line=DashedLine(
                                number_line.get_left(),
                                number_line.get_right(),
                                color=YELLOW,
                              ).set_stroke(width=100)

        self.add(number_line)
        self.wait(0.3)
        
        self.play(
                    LaggedStart(
                        *[ShowCreationThenDestruction(dashed_segment)
                        for dashed_segment in dashed_line],
                        run_time=5
                    ),
                    # Animation(Mobject(),run_time=2.1)空动画运行2.1秒,再加上lag_ratio的滞后时间
                    AnimationGroup(Animation(Mobject(),run_time=2.1),Write(text),lag_ratio=10)
            )
        self.wait()

class SuccessionExample2(Scene):
    def construct(self):
        number_line=NumberLine(x_min=-2,x_max=2)
        triangle=RegularPolygon(3,start_angle=-PI/2)\
                   .scale(0.2)\
                   .next_to(number_line.get_left(),UP,buff=SMALL_BUFF)
        text_1=TextMobject("1")\
               .next_to(number_line.get_tick(-1),DOWN)
        text_2=TextMobject("2")\
               .next_to(number_line.get_tick(0),DOWN)
        text_3=TextMobject("3")\
               .next_to(number_line.get_tick(1),DOWN)
        text_4=TextMobject("4")\
               .next_to(number_line.get_tick(2),DOWN)

        self.add(number_line)
        self.play(ShowCreation(triangle))
        self.wait(0.3)
        
        self.play(
                    ApplyMethod(triangle.shift,RIGHT*4,rate_func=linear,run_time=4),
                    # 用于时间配合
                    AnimationGroup(
                        Animation(Mobject(),run_time=1),
                        Write(text_1),lag_ratio=1
                    ),
                    AnimationGroup(
                        Animation(Mobject(),run_time=2),
                        Write(text_2),lag_ratio=1
                    ),
                    AnimationGroup(
                        Animation(Mobject(),run_time=3),
                        Write(text_3),lag_ratio=1
                    ),
                    AnimationGroup(
                        Animation(Mobject(),run_time=4),
                        Write(text_4),lag_ratio=1
                    )
            )

        self.wait()

class SuccessionExample2Compact(Scene):
    def construct(self):
        number_line=NumberLine(x_min=-2,x_max=2)
        triangle=RegularPolygon(3,start_angle=-PI/2)\
                   .scale(0.2)\
                   .next_to(number_line.get_left(),UP,buff=SMALL_BUFF)
        numbers=VGroup(
             *[TextMobject("%s"%i)\
              .next_to(number_line.get_tick(i-2),DOWN) for i in range(1,5)]
            )

        self.add(number_line)
        self.play(ShowCreation(triangle))
        self.wait(0.3)
        
        self.play(
                    ApplyMethod(triangle.shift,RIGHT*4,rate_func=linear,run_time=4),
                    *[AnimationGroup(
                        Animation(Mobject(),run_time=i+1),
                        Write(numbers[i]),lag_ratio=1
                    )for i in range(4)],
            )

        self.wait()

class SuccessionExample3(Scene):
    def construct(self):
        number_line=NumberLine(x_min=-2,x_max=2)
        text_1=TextMobject("Theorem of")\
             .next_to(number_line,DOWN)
        text_2=TextMobject("Beethoven")\
             .next_to(number_line,DOWN)
        dashed_line=DashedLine(
                                number_line.get_left(),
                                number_line.get_right(),
                                color=YELLOW,
                              ).set_stroke(width=11)

        self.add(number_line,text_1)
        
        self.play(
                    LaggedStart(
                        *[ShowCreationThenDestruction(dashed_segment)
                        for dashed_segment in dashed_line],
                        run_time=5
                    ),
                    AnimationGroup(
                        Animation(Mobject(),run_time=2.1),
                        ReplacementTransform(text_1,text_2),lag_ratio=1
                    )
            )

        self.wait()