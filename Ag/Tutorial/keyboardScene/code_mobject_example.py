from manimlib.imports import *

class BasicCodeMobject(Scene):
    CONFIG = {
        "code_config": {
            "file_name": "./assets/code/code_example.py",
            "font": 'Fira Code',
            "tab_width": 3,
            "style": "monokai",  # <- See https://help.farbox.com/pygments.html
            # insert_line_no=False, # <- Insert number lines
            "language": "python" # <- See https://pygments.org/languages/
        }
    }
    def setup(self):
        code = Code(**self.code_config)
        code.set_width(FRAME_WIDTH-4)
        code.move_to(ORIGIN)
        self.modify_code(code)
        self.draw_code_all_lines_at_a_time(code,run_time=2)
        self.wait()

    def draw_code_all_lines_at_a_time(self, code, **kwargs):
        self.play(LaggedStart(*[
                Write(code[i]) 
                for i in range(code.__len__())
            ]),
            **kwargs
        )
    
    def modify_code(self, code):
        pass

class CodeWindow(BasicCodeMobject):
    CONFIG = {
        "code_config": {
            "background": "window"
        }
    }

class CodeBackground(BasicCodeMobject):
    def modify_code(self, code):
        code[0].set_color(RED)     # <- Background color
        code[1].set_color(PURPLE)  # <- Number lines VGroup

class CodeLines(BasicCodeMobject):
    def modify_code(self, code):
        lines = code[2:]
        colors = it.cycle([RED, TEAL, PURPLE, BLUE])
        for line in lines:
            line.set_color(next(colors))

class DisappearEmptyLines(BasicCodeMobject):
    def modify_code(self, code):
        lines = code[2:]
        self.disappear_empty_lines(lines)

    def disappear_empty_lines(self, lines):
        min_width = lines[0].get_width()
        for line in lines[1:]:
            width = line.get_width()
            min_width = width if width <= min_width else min_width
        for line in lines:
            if line.get_width() < min_width * 1.01:
                line.fade(1)

class ChangeTabs(BasicCodeMobject):
    def modify_code(self, code):
        lines = code[2:]
        no_fade_lines = self.disappear_empty_lines(lines)
        self.change_tabs(no_fade_lines, 1.6)  # <- Change the 1.6

    def disappear_empty_lines(self, lines):
        no_fade_lines = VGroup()
        min_width = lines[0].get_width()
        for line in lines[1:]:
            width = line.get_width()
            min_width = width if width <= min_width else min_width
        for line in lines:
            if line.get_width() < min_width * 1.01:
                line.fade(1)
            else:
                no_fade_lines.add(line[:-1])
        return no_fade_lines

    def change_tabs(self, lines, n, default=5):
        first_letter_width = lines[0][0].get_width()
        def get_tab_width(lines):
            for line in lines[1:]:
                w = line[0].get_width()
                if w > first_letter_width * 1.3:
                    return w

        tab_width = get_tab_width(lines)
        new_tab = tab_width * n / default
        for line in lines:
            left_coord = line.get_left()
            flw = line[0].get_width()
            distance = abs(flw - first_letter_width)
            if distance > 0.26:
                n_tabs = flw / tab_width
                n_tabs_round = int(np.round(n_tabs))
                line[n_tabs_round:].next_to(left_coord,RIGHT,buff=0)
                vector = RIGHT * new_tab * n_tabs
                line[n_tabs_round:].shift(vector)