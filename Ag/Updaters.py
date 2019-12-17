from manimlib.imports import *

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