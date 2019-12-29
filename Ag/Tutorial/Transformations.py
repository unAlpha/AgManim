from manimlib.imports import *

class HelloWorld(Scene):
    def construct(self):
        helloWorld = TexMobject("Hello World!", color=RED)

        rectangle = Rectangle(color=BLUE)
        rectangle.surround(helloWorld)

        group_HW_RCT = VGroup(helloWorld, rectangle)

        yesManim = TexMobject("Hello Manim", color=BLUE)
        yesManim.scale(2.5)

        self.play(Write(helloWorld))
        self.wait(1)
        self.play(FadeIn(rectangle))
        self.wait(1)
        self.play(ApplyMethod(group_HW_RCT.scale, 2.5))
        self.wait(1)
        self.play(Transform(helloWorld, yesManim))
        self.wait(1)


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(ShowCreation(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))


class SpinInFromNothingExample(Scene):
    def construct(self):
        mobjects = VGroup(
                Square(),
                RegularPolygon(fill_opacity=1),
                TextMobject("Text").scale(2)
            )
        mobjects.scale(1.5)
        mobjects.arrange_submobjects(RIGHT,buff=2)

        self.play(
            *[SpinInFromNothing(mob,path_arc=PI/2) for mob in mobjects]
        )

        self.wait()


class GrowFromEdgeExample(Scene):
    def construct(self):
        mobjects = VGroup(
                Circle(),
                Circle(fill_opacity=1),
                TextMobject("Text").scale(2)
            )
        mobjects.arrange_submobjects(RIGHT,buff=2)

        directions=[UP,LEFT,DOWN,RIGHT]

        for direction in directions:
            self.play(
                *[GrowFromEdge(mob,direction) for mob in mobjects]
            )

        self.wait()


class GrowFromPointExample(Scene):
    def construct(self):
        mobjects = VGroup(
                Circle(),
                Circle(fill_opacity=1),
                TextMobject("Text").scale(2)
            )
        mobjects.arrange_submobjects(RIGHT,buff=2)

        directions=[UP,LEFT,DOWN,RIGHT]

        for direction in directions:
            self.play(
                *[GrowFromPoint(mob,mob.get_center()+direction*3) for mob in mobjects]
            )

        self.wait()


class FadeInFromLargeExample(Scene):
    def construct(self):
        mobjects = VGroup(
                Circle(),
                Circle(fill_opacity=1),
                TextMobject("Text").scale(2)
            )
        mobjects.scale(1.5)
        mobjects.arrange_submobjects(RIGHT,buff=2)

        scale_factors=[0.3,0.8,1,1.3,1.8]

        for scale_factor in scale_factors:
            t_scale_factor = TextMobject(f"\\tt scale\\_factor = {scale_factor}")
            t_scale_factor.to_edge(UP)

            self.add(t_scale_factor)
            # 对于for，play(*[])每次播放一个
            self.play(
                *[FadeInFromLarge(mob,scale_factor) for mob in mobjects]
            )

            self.remove(t_scale_factor)

        self.wait(0.3)


class FadeOutAndShiftExample(Scene):
    def construct(self):
        mobjects = VGroup(
                Circle(),
                Circle(fill_opacity=1),
                TextMobject("Text").scale(2)
            )
        mobjects.scale(1.5)
        mobjects.arrange_submobjects(RIGHT,buff=2)

        directions=[UP,LEFT,DOWN,RIGHT]

        self.add(mobjects)
        self.wait(0.3)

        for direction in directions:
            self.play(
                *[FadeOutAndShift(mob,direction) for mob in mobjects]
            )

        self.wait()


class FadeInFromExample(Scene):
    def construct(self):
        mobjects = VGroup(
                Circle(),
                Circle(fill_opacity=1),
                TextMobject("Text").scale(2)
            )
        mobjects.scale(1.5)
        mobjects.arrange_submobjects(RIGHT,buff=2)

        directions=[UP,LEFT,DOWN,RIGHT]

        for direction in directions:
            self.play(
                *[FadeInFrom(mob,direction) for mob in mobjects]
            )

        self.wait()


class UncreateExample(Scene):
    def construct(self):
        mobjects = VGroup(
                Circle(),
                Circle(fill_opacity=1),
                TextMobject("Text").scale(2)
            )
        mobjects.scale(1.5)
        mobjects.arrange_submobjects(RIGHT,buff=2)

        self.add(mobjects)

        self.wait(0.3)

        self.play(
            *[Uncreate(mob) for mob in mobjects]
        )

        self.wait()


class ShowPassingFlashAroundExample(Scene):
    def construct(self):
        mobjects = VGroup(
                Circle(),
                Circle(fill_opacity=1),
                TextMobject("Text").scale(2)
            )
        mobjects.scale(1.5)
        mobjects.arrange_submobjects(RIGHT,buff=2)

        self.add(mobjects)

        self.play(
            *[ShowPassingFlashAround(mob) for mob in mobjects]
        )
        self.play(
            *[ShowCreationThenDestructionAround(mob) for mob in mobjects]
        )
        self.play(
            *[ShowCreationThenFadeAround(mob) for mob in mobjects]
        )
        self.play(
            *[ApplyWave(mob) for mob in mobjects]
        )
        self.play(
            *[WiggleOutThenIn(mob) for mob in mobjects]
        )
        self.play(
            *[TurnInsideOut(mob) for mob in mobjects]
        )

        self.wait()

class TestCirle(Scene):
	def construct(self):
		circle1 = Circle(color=WHITE)
		self.play(ShowCreation(circle1))
		self.wait()

class TransformationText1V1(Scene):
	def construct(self):
		texto1 = TextMobject("First text")
		texto2 = TextMobject("Second text")
		self.play(Write(texto1))
		self.wait()
		self.play(Transform(texto1,texto2))
		self.wait()

class TransformationText1V2(Scene):
	def construct(self):
		texto1 = TextMobject("First text")
		texto1.to_edge(UP)
		texto2 = TextMobject("Second text")
		self.play(Write(texto1))
		self.wait()
		self.play(Transform(texto1,texto2))
		self.wait()

class TransformationText2(Scene):
	def construct(self):
		text1 = TextMobject("Function")
		text2 = TextMobject("Derivative")
		text3 = TextMobject("Integral")
		text4 = TextMobject("Transformation")
		self.play(Write(text1))
		self.wait()
		#Trans text1 -> text2
		self.play(ReplacementTransform(text1,text2))
		self.wait()
		#Trans text2 -> text3
		self.play(ReplacementTransform(text2,text3))
		self.wait()
		#Trans text3 -> text4
		self.play(ReplacementTransform(text3,text4))
		self.wait()

class CopyTextV1(Scene):
	def construct(self):
		formula = TexMobject(
			"\\frac{d}{dx}", #0
			"(", #1
			"u", #2
			"+", #3
			"v", #4
			")", #5
			"=", #6
			"\\frac{d}{dx}", #7
			"u", #8
			"+", #9
			"\\frac{d}{dx}", #10
			"v" #11
			)
		formula.scale(2)
		self.play(Write(formula[0:7]))
		self.wait()
		self.play(
			#注意目标的变换
			ReplacementTransform(formula[2].copy(),formula[8]),
			ReplacementTransform(formula[4].copy(),formula[11]),
			ReplacementTransform(formula[3].copy(),formula[9])
			)
		self.wait()
		self.play(
			ReplacementTransform(formula[0].copy(),formula[7]),
			ReplacementTransform(formula[0].copy(),formula[10])
			)
		self.wait()

class CopyTextV2(Scene):
	def construct(self):
		formula = TexMobject("\\frac{d}{dx}",
			"(","u","+","v",")","=",
			"\\frac{d}{dx}","u","+","\\frac{d}{dx}","v"
			)
		formula.scale(2)
		self.play(Write(formula[0:7]))
		self.wait()
		self.play(
			ReplacementTransform(formula[2].copy(),formula[8]),
			ReplacementTransform(formula[4].copy(),formula[11]),
			ReplacementTransform(formula[3].copy(),formula[9]),
			run_time=3
			)
		self.wait()
		self.play(
			ReplacementTransform(formula[0].copy(),formula[7]),
			ReplacementTransform(formula[0].copy(),formula[10]),
			run_time=3
			)
		self.wait()

class CopyTextV3(Scene):
	def construct(self):
		formula = TexMobject("\\frac{d}{dx}",
			"(","u","+","v",")","=",
			"\\frac{d}{dx}","u","+","\\frac{d}{dx}","v"
			)
		formula.scale(2)
		formula[8].set_color(RED)
		formula[11].set_color(BLUE)
		self.play(Write(formula[0:7]))
		self.wait()
		self.play(
			ReplacementTransform(formula[2].copy(),formula[8]),
			ReplacementTransform(formula[4].copy(),formula[11]),
			ReplacementTransform(formula[3].copy(),formula[9]),
			run_time=3
			)
		self.wait()
		self.play(
			ReplacementTransform(formula[0].copy(),formula[7]),
			ReplacementTransform(formula[0].copy(),formula[10]),
			run_time=3
			)
		self.wait()

class CopyTextV4(Scene):
	def construct(self):
		formula = TexMobject("\\frac{d}{dx}",
			"(","u","+","v",")","=",
			"\\frac{d}{dx}","u","+","\\frac{d}{dx}","v"
			)
		formula.scale(2)
		for letter,color in [("u",RED),("v",BLUE)]:
			#根据tex设置颜色
			formula.set_color_by_tex(letter,color)
		self.play(Write(formula[0:7]))
		self.wait()
		self.play(
			ReplacementTransform(formula[2].copy(),formula[8]),
			ReplacementTransform(formula[4].copy(),formula[11]),
			ReplacementTransform(formula[3].copy(),formula[9]),
			run_time=1
			)
		self.wait()
		self.play(
			ReplacementTransform(formula[0].copy(),formula[7]),
			ReplacementTransform(formula[0].copy(),formula[10]),
			run_time=1
			)
		self.wait()

class CopyTwoFormulas1(Scene):
	def construct(self):
		formula1 = TexMobject(
				"\\neg",		#0
				"\\forall",		#1
				"x",			#2
				":",			#3
				"P(x)"			#4
			)
		formula2 = TexMobject(
				"\\exists",		#0
				"x",			#1
				":",			#2
				"\\neg",		#3
				"P(x)"			#4
			)
		# 整体放大和位置控制
		for size,pos,formula in [(3,2*UP,formula1),(2,2*DOWN,formula2)]:
			formula.scale(size)
			formula.move_to(pos)
		self.play(Write(formula1))
		self.wait()

		changes = [
			[(0,1,2,3,4),
			# | | | | |
			# v v v v v
			 (3,0,1,2,4)],
		]
		for pre_ind,post_ind in changes:
			self.play(*[
				ReplacementTransform(
					formula1[i].copy(),formula2[j]
					)
				for i,j in zip(pre_ind,post_ind)
				],
				run_time=2
			)
			self.wait()

class CopyTwoFormulas2(Scene):
	def construct(self):
		formula1 = TexMobject(
				"\\neg","\\forall","x",":","P(x)"
			)
		formula2 = TexMobject(
				"\\exists","x",":","\\neg","P(x)"
			)
		for tam,pos,formula in [(2,2*UP,formula1),(2,2*DOWN,formula2)]:
			formula.scale(tam)
			formula.move_to(pos)
		self.play(Write(formula1))
		self.wait()
		changes = [
			# First time
			[(2,3,4),
			# | | |
			# v v v
			 (1,2,4)],
			# Second time
			[(0,),
			# | 
			# v
			 (3,)],
			# Third time
			[(1,),
			# | 
			# v
			 (0,)]
		]
		#每次读取一组数据
		for pre_ind,post_ind in changes:
			self.play(*[
				ReplacementTransform(
					formula1[i].copy(),formula2[j]
					)
				for i,j in zip(pre_ind,post_ind)
				],
				run_time=2
			)
			self.wait()

class CopyTwoFormulas2Color(Scene):
	def construct(self):
		formula1 = TexMobject(
				"\\neg","\\forall","x",":","P(x)"
			)
		formula2 = TexMobject(
				"\\exists","x",":","\\neg","P(x)"
			)
		parametters = [(2,2*UP,formula1,GREEN,"\\forall"),
					  (2,2*DOWN,formula2,ORANGE,"\\exists")]
		for size,pos,formula,col,sim in parametters:
			formula.scale(size)
			formula.move_to(pos)
			formula.set_color_by_tex(sim,col)
			formula.set_color_by_tex("\\neg",PINK)
		self.play(Write(formula1))
		self.wait()
		changes = [
			[(2,3,4),(1,2,4)],
			[(0,),(3,)],
			[(1,),(0,)]
		]
		for pre_ind,post_ind in changes:
			self.play(*[
				ReplacementTransform(
					formula1[i].copy(),formula2[j]
					)
				for i,j in zip(pre_ind,post_ind)
				],
				run_time=2
			)
			self.wait()

class CopyTwoFormulas3(Scene):
	def construct(self):
		formula1 = TexMobject(
				"\\neg","\\forall","x",":","P(x)"
			)
		formula2 = TexMobject(
				"\\exists","x",":","\\neg","P(x)"
			)
		parametters = [(2,2*UP,formula1,GREEN,"\\forall"),
					  (2,2*DOWN,formula2,ORANGE,"\\exists")]
		for size,pos,formula,col,sim in parametters:
			formula.scale(size)
			formula.move_to(pos)
			formula.set_color_by_tex(sim,col)
			formula.set_color_by_tex("\\neg",PINK)
		self.play(Write(formula1))
		self.wait()
		changes = [
			[(2,3,4),(1,2,4)],
			[(0,),(3,)],
			[(1,),(0,)]
		]
		for pre_ind,post_ind in changes:
			self.play(*[
				ReplacementTransform(
					formula1[i],formula2[j]
					)
				for i,j in zip(pre_ind,post_ind)
				],
				run_time=2
			)
			self.wait()

class ChangeTextColorAnimation(Scene):
	def construct(self):
		text = TextMobject("Text")
		text.scale(3)
		self.play(Write(text))
		self.wait()
		self.play(
                text.set_color, YELLOW,
				rate_func=smooth,
                run_time=2
            )
		self.wait()

class ChangeSizeAnimation(Scene):
	def construct(self):
		text = TextMobject("Text")
		text.scale(2)
		self.play(Write(text))
		self.wait()
		self.play(
                text.scale, 3,
                run_time=2
            )
		self.wait()

class MoveText(Scene):
	def construct(self):
		text = TextMobject("Text")
		text.scale(2)
		text.shift(LEFT*2)
		self.play(Write(text))
		self.wait()
		# 变换的路径
		self.play(
                text.shift, RIGHT*2,
                run_time=2,
                path_arc=-np.pi/2,  #Change 0 by -np.pi
				rate_func=double_smooth,
            )
		self.wait()

class ChangeColorAndSizeAnimation(Scene):
	def construct(self):
		text = TextMobject("Text")
		text.scale(2)
		text.shift(LEFT*2)
		self.play(Write(text))
		self.wait()
		# 接受多个.func动作
		self.play(
                text.shift, RIGHT*2,
                text.scale, 2,
                text.set_color, RED,
                run_time=2,
            )
		self.wait()


class TransformExample(Scene):
    def construct(self):
        mobject = RegularPolygon(3).scale(2)

        self.add(mobject)

        for n in range(4,9):
            self.play(
                Transform(
                    mobject,
                    RegularPolygon(n).scale(2)
                )
            )

        self.wait(0.3)

class ReplacementTransformExample(Scene):
    def construct(self):
        polygons = [*[RegularPolygon(n).scale(2) for n in range(3,9)]]

        self.add(polygons[0])

        for i in range(len(polygons)-1):
            self.play(
                ReplacementTransform(
                    polygons[i],
                    polygons[i+1]
                )
            )

        self.wait(0.3)


class TransformFromCopyExample(Scene):
    def construct(self):
        mobject = RegularPolygon(3).scale(2)

        self.add(mobject)

        for n in range(4,9):
            self.play(
                TransformFromCopy(
                    mobject,
                    RegularPolygon(n).scale(2)
                )
            )

        self.wait(0.3)

class ClockwiseTransformExample(Scene):
    def construct(self):
        polygons = VGroup(
              *[RegularPolygon(n).scale(0.7) for n in range(3,9)]
        ).arrange_submobjects(RIGHT,buff=1)

        self.add(polygons[0])

        for i in range(len(polygons)-1):
            self.play(
                ClockwiseTransform(
                    polygons[0],
                    polygons[i+1]
                )
            )

        self.wait(0.3)


class CounterclockwiseTransformExample(Scene):
    def construct(self):
        polygons = VGroup(
            *[RegularPolygon(n).scale(0.7) for n in range(3,9)]
        ).arrange_submobjects(RIGHT,buff=1)

        self.add(polygons[0])

        for i in range(len(polygons)-1):
            self.play(
                CounterclockwiseTransform(
                    polygons[0],
                    polygons[i+1]
                )
            )

        self.wait(0.3)


class MoveToTargetExample(Scene):
    def construct(self):
        mobject=Square()
        mobject.generate_target()
        VGroup(mobject,mobject.target)\
            .arrange_submobjects(RIGHT,buff=3)

        mobject.target.rotate(PI/4)\
                      .scale(2)\
                      .set_stroke(PURPLE,9)\
                      .set_fill(ORANGE,1)

        self.add(mobject)
        self.wait(0.3)

        self.play(MoveToTarget(mobject))
        self.wait(0.3)


class ApplyMethodExample(Scene):
    def construct(self):
        dot = Dot()
        text = TextMobject("Text")

        dot.next_to(text,LEFT)

        self.add(text,dot)

        self.play(ApplyMethod(text.scale,3,{"about_point":dot.get_center()}))
        #                                  --------------------------------
        #                                          Optional parameters

        self.wait(0.3)


class ApplyPointwiseFunctionExample(Scene):
    def construct(self):
        text = TextMobject("Text")

        self.add(text)

        def spread_out(p):
            p = p + 2*DOWN
            return (FRAME_X_RADIUS+FRAME_Y_RADIUS)*p/get_norm(p)
            #      -------------------------------
            #          See manimlib/constants.py

        self.play(
            ApplyPointwiseFunction(spread_out, text)
        )


class FadeToColorExample(Scene):
    def construct(self):
        text = TextMobject("Text")\
               .set_width(FRAME_WIDTH)

        colors=[RED,PURPLE,GOLD,TEAL]

        self.add(text)

        for color in colors:
            self.play(FadeToColor(text,color))

        self.wait(0.3)

class ScaleInPlaceExample(Scene):
    def construct(self):
        text = TextMobject("Text")\
               .set_width(FRAME_WIDTH/2)

        scale_factors=[2,0.3,0.6,2]

        self.add(text)

        for scale_factor in scale_factors:
            self.play(ScaleInPlace(text,scale_factor))

        self.wait(0.3)


class RestoreExample(Scene):
    def construct(self):
        text = TextMobject("Original")\
               .set_width(FRAME_WIDTH/2)

        text.save_state()

        text_2 = TextMobject("Modified")\
               .set_width(FRAME_WIDTH/1.5)\
               .set_color(ORANGE)\
               .to_corner(DL)

        self.add(text)

        self.play(Transform(text,text_2))
        self.play(
            text.shift,RIGHT,
            text.rotate,PI/4
            )
        self.play(Restore(text))

        self.wait(0.7)


class ApplyFunctionExample(Scene):
    def construct(self):
        text = TextMobject("Text")\
               .to_corner(DL)

        self.add(text)

        def apply_function(mob):
            mob.scale(2)
            mob.to_corner(UR)
            mob.rotate(PI/4)
            mob.set_color(RED)
            return mob

        self.play(
            ApplyFunction(
                apply_function,
                text
            )
        )

        self.wait(0.3)