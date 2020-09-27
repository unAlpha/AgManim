from manimlib.imports import *


class KeyboardScene(Scene):
    CONFIG = {
        "lag": 0.1,
        "rate_factor": 0.05,
        "time_factor": 0.13,
        "lag_spaces": 0.2,
        "range_random": 3
    }
    def keyboard(self, text):
        def return_random():
            return random.randint(1, self.range_random)
        for i in range(len(text)):
            self.add_sound("keyboard/key%s"%return_random())
            text[i].set_fill(None, 1)
            self.play(LaggedStartMap(FadeIn, 
                        text[i],
                        run_time=self.rate_factor*len(text[i]),
                        lag_ratio=self.lag/len(text[i])
                        ))
            self.wait(0.3*return_random()*self.time_factor)
            if i < len(text) - 1:
                pre_ty = text[i].get_center()[1]
                pre_tx = text[i].get_center()[0]
                pos_ty = text[i+1].get_center()[1]
                pos_tx = text[i+1].get_center()[0]
                pre_width = text[i].get_width() / 2
                pos_width = text[i+1].get_width() / 2
                pre_height = text[i].get_height() / 2
                pos_height = text[i+1].get_height() / 2
                dist_min_x = (pre_width + pos_width) * 1.6
                dist_min_y = (pre_height + pos_height) * 1.2
                if i == 0 or dist_max_x < dist_min_x:
                    dist_max_x = dist_min_x
                if i == 0 or dist_max_y < dist_min_y:
                    dist_max_y = dist_min_y
                if abs(pre_ty - pos_ty) > dist_max_y:
                    self.add_sound("keyboard/enter")
                    self.wait(self.time_factor)
                elif abs(pre_tx - pos_tx) > dist_max_x and abs(pre_ty - pos_ty) < dist_max_y:
                    self.add_sound("keyboard/space")
                    self.wait(self.time_factor)
            if i == len(text) - 1:
                self.add_sound("keyboard/enter")
                self.wait(self.time_factor)

class CodeKeyboardScene(KeyboardScene):
    CONFIG = {
        "code_config": {
            "file_name": "./assets/code/code_example.py",
            "font": "Fira Code",
            "tab_width": 3,
            "style": "monokai", 
            "language": "python",
            "background": "window"
        }
    }
    def setup(self):
        code = Code(**self.code_config, scale_factor=0.5)
        code.set_width(FRAME_WIDTH-2)
        code.move_to(ORIGIN)
        lines = code[2:]
        no_fade_lines = self.disappear_empty_lines(lines)
        full_lines = self.change_tabs(no_fade_lines, 1.6)
        self.code_lines = full_lines
        self.code_window = code[0]
        self.code_line_numbers = code[1]

    def disappear_empty_lines(self, lines):
        no_fade_lines = VGroup()
        min_width = lines[0].get_width()
        tab_width = self.get_tab_width(lines)
        for line in lines[1:]:
            width = line.get_width()
            min_width = width if width <= min_width else min_width
        for line in lines:
            if line.get_width() < min_width * 1.01:
                line.set_style(fill_opacity=1)
            else:
                no_fade_lines.add(line[:-1])
        return no_fade_lines

    def change_tabs(self, lines, n, default=5):
        first_letter_width = lines[0][0].get_width()
        full_lines = VGroup()

        tab_width = self.get_tab_width(lines)
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
                full_lines.add(line[n_tabs_round+1:])
            else:
                full_lines.add(line)
        return full_lines

    def get_tab_width(self, lines):
        first_letter_width = lines[0][0].get_width()
        for line in lines[1:]:
            w = line[0].get_width()
            if w > first_letter_width * 1.3:
                return w

class CodeKeyboardExample(CodeKeyboardScene):
    def construct(self):
        lines = self.code_lines
        all_letters = VGroup(*[
            mob
            for submob in lines
            for mob in submob
        ])
        self.play(
            ShowCreation(self.code_window),
            Write(self.code_line_numbers)
        )
        self.keyboard(all_letters)
        self.wait()