from manimlib.imports import *

def imageObjAndText(imageName,text1,text2):
    pic = ImageMobject(imageName).scale(2)
    picText1 = Text(text1,
                    font='阿里巴巴普惠体 B',
                    color="#308032"
        )\
        .set_height(0.23)\
        .next_to(pic,DOWN,buff=SMALL_BUFF)
    picText2 = Text(text2, 
                    font='阿里巴巴普惠体 B',
                    color=BLACK
        )\
        .set_height(0.28)\
        .next_to(picText1,DOWN,buff=SMALL_BUFF)
    picAndText = Group(pic,picText1,picText2).center()
    pic.rect = RoundedRectangle(
                    corner_radius=0.1,
                    color="#DDDDDD",
                    fill_color = "#DDDDDD",
                    fill_opacity = 1,
                    height=picAndText.get_height()+0.2,
                    width=picAndText.get_width()+0.2
        )
    return Group(pic.rect,pic,picText1,picText2)

def palyALL(self,allParts):
    self.play(
        FadeInFromLarge(allParts[:2]),
        AnimationGroup(
                    Animation(Mobject(),run_time=0.1),
                    FadeInFromDirections(allParts[2]),
                    FadeInFromDirections(allParts[3]),
                    lag_ratio=0.1
            )
        )
    self.wait(15)
    self.play(FadeOutAndShiftDown(allParts))

class StockIndex1(Scene):
    def construct(self):
        allParts = imageObjAndText(
                        "StockIndex/1、道琼斯工业平均指数走势图",
                        "Dow Jones Industrial Average",
                        "道琼斯工业平均指数走势图"        
            )
        palyALL(self,allParts)

class StockIndex2(Scene):
    def construct(self):
        allParts = imageObjAndText(
                        "StockIndex/2、1947年上海证券交易所",
                        "Shanghai Stock Exchange in 1947",
                        "1947年上海证券交易所"        
            )
        palyALL(self,allParts)

class StockIndex3(Scene):
    def construct(self):
        allParts = imageObjAndText(
                        "StockIndex/3、查尔斯道",
                        "Charles Henry Dow",
                        "查尔斯·道"        
            )
        palyALL(self,allParts)

class StockIndex4(Scene):
    def construct(self):
        allParts = imageObjAndText(
                        "StockIndex/4、邓丽君",
                        "Teresa Teng",
                        "邓丽君"        
            )
        palyALL(self,allParts)

class StockIndex5(Scene):
    def construct(self):
        allParts = imageObjAndText(
                        "StockIndex/5、邓小平和约翰·范尔霖",
                        "Deng Xiaoping and John Joseph Phelan Jr.",
                        "邓小平和约翰·范尔霖"        
            )
        palyALL(self,allParts)

class StockIndex61(Scene):
    def construct(self):
        allParts = imageObjAndText(
                        "StockIndex/61、道琼斯指数跌幅排行2",
                        "Largest daily point losses",
                        "道琼斯指数跌幅排行"        
            )
        line = Line(LEFT*1.6,RIGHT*2.8,color=RED).move_to(1.35*UP+0.33*RIGHT)
        self.play(
            FadeInFromLarge(allParts[:2]),
            AnimationGroup(
                    Animation(Mobject(),run_time=0.1),
                    FadeInFromDirections(allParts[2]),
                    FadeInFromDirections(allParts[3]),
                    lag_ratio=0.1
                )
            )
        self.wait(2)
        self.play(ShowCreation(line))
        self.wait(10)
        self.play(
                FadeOutAndShiftDown(allParts),
                FadeOutAndShiftDown(line)
            )

class StockIndex62(Scene):
    def construct(self):
        allParts = imageObjAndText(
                        "StockIndex/62、道琼斯指数涨幅排行",
                        "Largest daily point gains",
                        "道琼斯指数涨幅排行"        
            )
        palyALL(self,allParts)

class StockIndex7(Scene):
    def construct(self):
        allParts = imageObjAndText(
                        "StockIndex/7、约翰·范尔霖去上海过户",
                        "John goes to Shanghai",
                        "约翰·范尔霖去上海过户"        
            )
        palyALL(self,allParts)

class StockIndex8(Scene):
    def construct(self):
        allParts = imageObjAndText(
                        "StockIndex/8、飞乐音响股票",
                        "Feilo Acoustics Stock",
                        "飞乐音响股票"        
            )
        palyALL(self,allParts)
    
class StockIndex9(Scene):
    def construct(self):
        allParts = imageObjAndText(
                        "StockIndex/9、费城证券交易所",
                        "Philadelphia Stock Exchange",
                        "费城证券交易所"        
            )
        palyALL(self,allParts)

class StockIndex10(Scene):
    def construct(self):
        allParts = imageObjAndText(
                        "StockIndex/10、工商银行上海信托静安营业部",
                        "The Jing'an Sales Department of ICBC Shanghai",
                        "工商银行上海信托静安营业部"        
            )
        palyALL(self,allParts)

class StockIndex11(Scene):
    def construct(self):
        allParts = imageObjAndText(
                        "StockIndex/11、华尔街日报",
                        "The Wall Street Journal",
                        "华尔街日报"        
            )
        palyALL(self,allParts)

class StockIndex12(Scene):
    def construct(self):
        allParts = imageObjAndText(
                        "StockIndex/12、纳斯达克交易所",
                        "NASDAQ",
                        "纳斯达克交易所"        
            )
        palyALL(self,allParts)

class StockIndex13(Scene):
    def construct(self):
        allParts = imageObjAndText(
                        "StockIndex/13、纽约证券交易所",
                        "The New York Stock Exchange",
                        "纽约证券交易所"        
            )
        palyALL(self,allParts)

class StockIndex14(Scene):
    def construct(self):
        allParts = imageObjAndText(
                        "StockIndex/14、上海证券交易所",
                        "Shanghai Stock Exchange",
                        "上海证券交易所"        
            )
        palyALL(self,allParts)

class StockIndex15(Scene):
    def construct(self):
        allParts = imageObjAndText(
                        "StockIndex/15、上证综合指数走势图",
                        "SSE Index",
                        "上证综合指数走势图"        
            )
        palyALL(self,allParts)

class StockIndex16(Scene):
    def construct(self):
        allParts = imageObjAndText(
                        "StockIndex/16、深圳证券交易所",
                        "Shenzhen Stock Exchange",
                        "深圳证券交易所"        
            )
        palyALL(self,allParts)

class StockIndex17(Scene):
    def construct(self):
        allParts = imageObjAndText(
                        "StockIndex/17、梧桐树协议",
                        "Buttonwood Agreement",
                        "梧桐树协议"        
            )
        palyALL(self,allParts)

class StockIndex18(Scene):
    def construct(self):
        allParts = imageObjAndText(
                        "StockIndex/18、新民晚报",
                        "Xinmin Evening News",
                        "新民晚报"        
            )
        palyALL(self,allParts)

class StockIndex19(Scene):
    def construct(self):
        allParts = imageObjAndText(
                        "StockIndex/19、道琼斯指数12个原始股",
                        "The original 12 industrials",
                        "道琼斯指数12个原始股"        
            )
        palyALL(self,allParts)

class StockIndex20(Scene):
    def construct(self):
        allParts = imageObjAndText(
                        "StockIndex/20、深圳成份指数",
                        "SZSE Composite Index",
                        "深圳成份指数"        
            )
        palyALL(self,allParts)

class StockIndex21(Scene):
    def construct(self):
        allParts = imageObjAndText(
                        "StockIndex/21、道琼斯指数最近表现",
                        "The latest data on Dow Jones Industrial Average",
                        "道琼斯指数最近表现"        
            )
        palyALL(self,allParts)

