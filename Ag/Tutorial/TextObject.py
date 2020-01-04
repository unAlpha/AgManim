from manimlib.imports import *

class Demo1(Scene):
    def construct(self):
        # text = Text('Hello, world!')
        # text = Text('Hello', color=BLUE)
        # text = Text('Hello, world!', t2c={'world':BLUE})
        # text = Text('Hello', gradient=(BLUE, GREEN))
        # text = Text('Hello, world!', t2g={'world':(BLUE, GREEN)})
        # text = Text('Hello', font='Eraser')
        # text = Text('Hello, world!', t2f={'world':'Forte'})
        # text = Text('Hello', slant=ITALIC)
        # text = Text('Hello, world!', t2s={'world':ITALIC})
        # text = Text('Hello', weight=BOLD)
        # text = Text('Hello', size=5)
        text = Text('Hello\nWorld', lsh=1.5)
        self.play(Write(text))

class Demo2(Scene):
    def construct(self):
        text = Text(
            'Google', 
            t2c={
                '[:1]':'#3174f0', '[1:2]':'#e53125', 
                '[2:3]':'#fbb003', '[3:4]':'#3174f0', 
                '[4:5]':'#269a43', '[5:]':'#e53125',
            }
        )
        self.play(Write(text))

class Demo3(Scene):
    def construct(self):
        text = Text('Hello, world!')
        text.set_color(BLUE)
        text[7:12].set_color(BLUE)
        text.set_color_by_gradient(BLUE, GREEN)
        text[7:12].set_color_by_gradient(BLUE, GREEN)
        text.set_color_by_t2c({'world':BLUE})
        text.set_color_by_t2g({'world':(BLUE, GREEN)})
        self.play(Write(text))


script = '''
Hello
你好
こんにちは
안녕하세요
'''
class Demo4(Scene):
    def construct(self):
        text = Text(script, font='Source Han Sans')
        self.play(Write(text))
        
