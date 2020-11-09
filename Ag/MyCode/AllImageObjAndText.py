from manimlib.imports import *

def imageObjAnd2Text(imageName,text1,text2):
    pic = ImageMobject(imageName).scale(2)
    picText1 = Text(text1,
                    font='Microsoft YaHei',
                    color="#308032"
        )\
        .set_height(0.23)
    if picText1.get_width() > pic.get_width():
        picText1.set_width(pic.get_width()*0.96)
    picText1.next_to(pic,DOWN,buff=SMALL_BUFF)
    picText2 = Text(text2, 
                    font='Microsoft YaHei',
                    color=BLACK
        )\
        .set_height(0.28)
    if picText2.get_width() > pic.get_width():
        picText2.set_width(pic.get_width()*0.96)
    picText2.next_to(picText1,DOWN,buff=SMALL_BUFF*1.1)
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

def imageObjAnd1Text(imageName,text2,lsh=1):
    pic = ImageMobject(imageName).scale(2)
    picText2 = Text(text2, 
                    font='Microsoft YaHei',
                    color=BLACK,
                    lsh=1.2
        )\
        .set_height(0.28*lsh)
    if picText2.get_width() > pic.get_width():
        picText2.set_width(pic.get_width()*0.96)
    picText2.next_to(pic,DOWN,buff=SMALL_BUFF*1.1)
    picAndText = Group(pic,picText2).center()
    pic.rect = RoundedRectangle(
                    corner_radius=0.1,
                    color="#DDDDDD",
                    fill_color = "#DDDDDD",
                    fill_opacity = 1,
                    height=picAndText.get_height()+0.2,
                    width=picAndText.get_width()+0.2
        )
    return Group(pic.rect,pic,picText2)

def palyALL2(self,allParts):
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

def palyALL1(self,allParts):
    self.play(
        FadeInFromLarge(allParts[:2]),
        AnimationGroup(
                    Animation(Mobject(),run_time=0.1),
                    FadeInFromDirections(allParts[2]),
                    lag_ratio=0.1
            )
        )
    self.wait(15)
    self.play(FadeOutAndShiftDown(allParts))


class Autism01(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "Autism/Leo-Kanner",
                        "Leo Kanner",
                        "利奥·堪纳",     
            )
        palyALL2(self,allParts)

class Autism02(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "Autism/Hans-Asperger",
                        "Hans Asperger",
                        "汉斯·艾斯伯格",     
            )
        palyALL2(self,allParts)

class Autism03(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "Autism/Autism in the US",
                        "Actual and projected % Prevalence of Autism in the US",
                        "美国自闭症的实际和预计患病率",     
            )
        palyALL2(self,allParts)

class Autism04(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "Autism/Artist Stephen",
                        "Artist Stephen Wiltshire draws New York City from memory",
                        "斯蒂芬·威尔特郡从记忆中画出纽约的作画",     
            )
        palyALL2(self,allParts)


class BottomFrog1(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "BottomFrog/1、门镜",
                        "Peephole",
                        "门镜"        
            )
        palyALL2(self,allParts)

class BottomFrog2(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "BottomFrog/2、门镜图",
                        "View through a peephole",
                        "门镜图像"        
            )
        palyALL2(self,allParts)

class BottomFrog3(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "BottomFrog/3、鱼眼图A",
                        "Fisheye picture A",
                        "鱼眼图A"        
            )
        palyALL2(self,allParts)

class BottomFrog4(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "BottomFrog/4、鱼眼图B",
                        "Fisheye picture B",
                        "鱼眼图B"        
            )
        palyALL2(self,allParts)

class BottomFrog5(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "BottomFrog/5、克劳狄乌斯·托勒密",
                        "Claudius Ptolemaeus",
                        "克劳狄乌斯·托勒密"        
            )
        palyALL2(self,allParts)

class BottomFrog6(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "BottomFrog/6、威理博·斯涅尔",
                        "Willebrord Snellius",
                        "威理博·斯涅耳"        
            )
        palyALL2(self,allParts)

class BottomFrog7(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "BottomFrog/7、克里斯蒂安·惠更斯",
                        "Christiaan Huygens",
                        "克里斯蒂安·惠更斯"        
            )
        palyALL2(self,allParts)

class BottomFrog8(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "BottomFrog/8、笛卡尔",
                        "René Descartes",
                        "勒内·笛卡尔"        
            )
        palyALL2(self,allParts)


class DrinkBird01(Scene):
    def construct(self):
        txt = Text("两个小时后",font='Microsoft YaHei')
        self.play(FadeInFromDirections(txt))
        self.wait(3)
        self.play(FadeOut(txt))

class DrinkBird02(Scene):
    def construct(self):
        txt = Text("一个小时后",font='Microsoft YaHei',)
        self.play(FadeInFromDirections(txt))
        self.wait(3)
        self.play(FadeOut(txt))

class DrinkBird03(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "DrinkingBird/饮水鸟",
                        "Drinking bird",
                        "饮水鸟"  
            )
        palyALL2(self,allParts)

class DrinkBird04(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "DrinkingBird/异形中的饮水鸟",
                        "《异形》中的饮水鸟画面"  
            )
        palyALL1(self,allParts)


class Dujiangyan1(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "Dujiangyan/1亚非大河文明",
                        "四大文明古国及对应的河流"         
            )
        palyALL1(self,allParts)

class Dujiangyan2(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "Dujiangyan/2郑国渠",
                        "郑国渠修建位置"         
            )
        palyALL1(self,allParts)

class Dujiangyan3(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "Dujiangyan/3秦灭巴蜀",
                        "公元前316年 秦灭巴蜀"         
            )
        palyALL1(self,allParts)

class Dujiangyan4(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "Dujiangyan/4都江堰开凿前的地图",
                        "都江堰开凿前的地形图"       
            )
        palyALL1(self,allParts)

class Dujiangyan5(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "Dujiangyan/5二八分沙",
                        "都江堰 二八分沙"       
            )
        palyALL1(self,allParts)

class Dujiangyan6(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "Dujiangyan/6四六分水",
                        "都江堰 四六分水"       
            )
        palyALL1(self,allParts)

class Dujiangyan7(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "Dujiangyan/7都江堰的结构图",
                        "都江堰的结构图"       
            )
        palyALL1(self,allParts)

class Dujiangyan8(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "Dujiangyan/8东汉李冰石像",
                        "1974年出土的李冰石像"       
            )
        palyALL1(self,allParts)

class Dujiangyan9(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "Dujiangyan/9热胀冷缩原理",
                        "采用“热胀冷缩”原理使山石裂开"  
            )
        palyALL1(self,allParts)


class Flu1(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Flu1918/1918费城大游行",
                        "1918年费城大游行"        
            )
        palyALL1(self,allParts)

class Flu2(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Flu1918/1918年流感期间西雅图电车乘务员拒绝没戴口罩的乘客",
                        """
                        1918年流感期间的西雅图
                        电车乘务员拒绝没戴口罩的乘客
                        """
                        ,2
            )
        self.play(
            FadeInFromLarge(allParts[:2]),
            AnimationGroup(
                        Animation(Mobject(),run_time=1),
                        FadeInFromRandomB(allParts[2]),
                        lag_ratio=0.5
                )
            )
        self.wait(15)
        self.play(FadeOutAndShiftDown(allParts))

class Flu3(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "Flu1918/1918年流行病的流感死亡率年龄分布与正常流行病之间的差异",
                        "美国每个年龄组的100,000人死亡",
                        "1918年流感与正常流行病之间的死亡率差异"
            )
        palyALL2(self,allParts)

class Flu4(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Flu1918/1951年赫尔汀和队友",
                        "1951年赫尔汀和其队友"        
            )
        palyALL1(self,allParts)

class Flu5(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Flu1918/巴黎和会中的领导人",
                        "巴黎和会中的领导人"        
            )
        palyALL1(self,allParts)

class Flu6(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Flu1918/戴口罩的西雅图警察",
                        "戴口罩的西雅图警察"        
            )
        palyALL1(self,allParts)

class Flu7(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "Flu1918/德国皇帝威廉二世",
                        "Wilhelm II",
                        "德国皇帝威廉二世"
            )
        palyALL2(self,allParts)

class Flu8(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Flu1918/护士正在处理尸体",
                        "护士正在处理尸体"        
            )
        palyALL1(self,allParts)

class Flu9(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "Flu1918/甲型流感病毒",
                        "Influenza A virus",
                        "甲型流感病毒"
            )
        palyALL2(self,allParts)

class Flu10(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Flu1918/堪萨斯州赖利堡福斯顿军营中的患病士兵",
                        "堪萨斯州赖利堡芬斯顿军营中的患病士兵"        
            )
        palyALL1(self,allParts)

class Flu11(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Flu1918/流感病毒的感染路径",
                        "流感病毒的感染路径"        
            )
        palyALL1(self,allParts)

class Flu12(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Flu1918/流感病毒中片段化的RNA",
                        "流感病毒中片段化的RNA"        
            )
        palyALL1(self,allParts)

class Flu13(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "Flu1918/美国红十字会医护倾向于在1918年奥克兰市政厅内设立的临时病房中对患者进行流感治疗",
                        "在1918年奥克兰市政厅内设立的临时病房",
                        "美国红十字会设立临时病房"
            )
        palyALL2(self,allParts)

class Flu14(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Flu1918/美国人均预期寿命",
                        "美国人均预期寿命"        
            )
        palyALL1(self,allParts)

class Flu15(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "Flu1918/美国总统威尔逊",
                        "Thomas Woodrow Wilson",
                        "美国总统威尔逊"
            )
        palyALL2(self,allParts)

class Flu16(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Flu1918/齐默尔曼电报",
                        "齐默尔曼电报"
            )
        palyALL1(self,allParts)

class Flu17(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Flu1918/三波流感中英国病死率",
                        "三波流感中 英国病死率"
            )
        palyALL1(self,allParts)

class Flu18(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Flu1918/陶本伯格和赫尔汀",
                        "陶本伯格和赫尔汀"
            )
        palyALL1(self,allParts)

class Flu19(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "Flu1918/西班牙国王阿方索十三世",
                        "Alfonso XIII",
                        "西班牙国王 阿方索十三世"
            )
        palyALL2(self,allParts)

class Flu20(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "Flu1918/英国首相大卫·劳合·乔治",
                        "David Lloyd George",
                        "英国首相 大卫·劳合·乔治"           
            )
        palyALL2(self,allParts)

class Flu21(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Flu1918/重建的西班牙流感病毒",
                        "重建的西班牙流感病毒"         
            )
        palyALL1(self,allParts)

class Flu22(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "Flu1918/乔治五世",
                        "George V",
                        "英国国王 乔治五世" 
            )
        palyALL2(self,allParts)


class Gastr1(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Gastrointestinal/1黑豹剧照",
                        "黑豹剧照"         
            )
        palyALL1(self,allParts)

class Gastr2(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Gastrointestinal/2发病率",
                        """
                        2015年中国城市和农村地区
                        恶性肿瘤年龄别发病情况
                        """,
                        0.5
            )
        palyALL1(self,allParts)

class Gastr3(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Gastrointestinal/3死亡率",
                        """
                        2015年中国恶性肿瘤年龄别
                        死亡情况估计
                        """,
                        0.5
            )
        palyALL1(self,allParts)

class Gastr4(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Gastrointestinal/4上消化道肿瘤发病风险的单因素分析",
                        "上消化道肿瘤发病风险的单因素分析",
            )
        palyALL1(self,allParts)

class Gastr51(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Gastrointestinal/5.1胃癌演变过程",
                        "胃癌的演变过程",
            )
        palyALL1(self,allParts)

class Gastr52(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Gastrointestinal/5.2肠癌演变过程",
                        "肠癌的演变过程",
            )
        palyALL1(self,allParts)

class Gastr6(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Gastrointestinal/6食管癌不同临床分期的五年生存率",
                        "食管癌不同临床分期的五年生存率",
            )
        palyALL1(self,allParts)

class Gastr7(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Gastrointestinal/7胃癌不同临床分期的五年生存率",
                        "胃癌不同临床分期的五年生存率",
            )
        palyALL1(self,allParts)

class Gastr8(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Gastrointestinal/8中国韩国日本胃癌早癌检出率对比",
                        "中国、韩国、日本胃癌早癌检出率对比",
            )
        palyALL1(self,allParts)

class Gastr9(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Gastrointestinal/9医生给自己做胃镜图",
                        "医生给自己做胃镜图",
            )
        palyALL1(self,allParts)

class Gastr10(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Gastrointestinal/10电子胃镜仪及其使用",
                        "电子胃镜仪及其使用",
            )
        palyALL1(self,allParts)

class Gastr11(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Gastrointestinal/11胶囊内镜图",
                        "胶囊内镜",
            )
        palyALL1(self,allParts)

class Gastr12(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Gastrointestinal/12日本胃癌开展率持续提升（每10万人）",
                        "日本胃镜开展率持续提升（每10万人）",
            )
        palyALL1(self,allParts)

class Gastr13(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Gastrointestinal/13日本胃癌死亡率（每10万人，年均矫正）",
                        "日本胃癌死亡率（每10万人，年均矫正）",
            )
        palyALL1(self,allParts)

class Gastr14(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Gastrointestinal/14中国与其他国家肠镜开展率对比（每10万人）",
                        "中国与其他国家肠镜开展率对比（每10万人）",
            )
        palyALL1(self,allParts)

class Gastr15(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Gastrointestinal/15中国与其他国家胃镜开展率对比（每10万人）",
                        "中国与其他国家胃镜开展率对比（每10万人）",
            )
        palyALL1(self,allParts)

script = [
"""（1）胃癌高发地区人群；""",
"""（2）幽门螺杆菌感染者；""",
"""（3）既往患有慢性萎缩性胃炎、胃溃疡、胃息肉、
          手术后残胃、肥厚性胃炎、恶性贫血等胃癌前疾病；""",
"""（4）胃癌患者的一级亲属；""",
"""（5）存在胃癌的其它高危因素，比如：
          高盐、腌制饮食、吸烟、重度饮酒等。"""
]

class Gastr16(Scene):
    def construct(self):
        textList = []
        for txt in script:
            text = Text(txt,size=0.3,lsh=0.4)
            textList.append(text)
        allVG = VGroup(*textList).arrange(DOWN, aligned_edge = LEFT, buff = MED_SMALL_BUFF).shift(0.2*UP)
        allVG.set_color_by_gradient(RED, YELLOW)

        allParts = imageObjAnd1Text(
                        allVG,
                        "推荐做胃镜的高危人群"         
            )
        
        self.play(
            FadeInFromLarge(allParts[:2]),
            FadeInFrom(allParts[2])
            )

        self.play(FadeInFromDirections(allVG[0]))
        self.wait(2)
        self.play(FadeInFromDirections(allVG[1]))
        self.wait(2)
        self.play(FadeInFromDirections(allVG[2]))
        self.wait(2)
        self.play(FadeInFromDirections(allVG[3]))
        self.wait(2)
        self.play(FadeInFromDirections(allVG[4]))
        self.wait(5)

        self.play(FadeOutAndShiftDown(allParts),FadeOutAndShiftDown(allVG))

class Gastr18(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Gastrointestinal/18医生给自己做胃镜图",
                        "医生给自己做肠镜图",
            )
        palyALL1(self,allParts)

class Gastr20(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Gastrointestinal/20电子胃镜仪导管末端功能",
                        "电子胃镜仪导管末端功能",
            )
        palyALL1(self,allParts)


class HumenBridge01(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "HumenBridge/1冯卡门",
                        "Theodore von Kármán",
                        "西奥多·冯·卡门",     
            )
        palyALL2(self,allParts)

class HumenBridge02(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "HumenBridge/2普朗特",
                        "Ludwig Prandtl",
                        "路德维希·普朗特",
                        
            )
        palyALL2(self,allParts)

class HumenBridge03(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "HumenBridge/3哈依门兹",
                        "Karl Hiemenz",
                        "卡尔·海门兹",
                        
            )
        palyALL2(self,allParts)

class HumenBridge05(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "HumenBridge/5圣克里斯多福",
                        "聖克里斯多福背耶稣过河",
            )
        palyALL1(self,allParts)

class HumenBridge06(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "HumenBridge/6卫星拍摄的大气卡门涡街",
                        "大气中的卡门涡街现象",
            )
        palyALL1(self,allParts)

class HumenBridge09(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "HumenBridge/9科塔马大桥原貌",
                        "塔科马大桥原貌",
            )
        palyALL1(self,allParts)

class HumenBridge11(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "HumenBridge/11水马",
                        "虎门大桥两侧水马",
            )
        palyALL1(self,allParts)

class IncomeTax01(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "IncomeTax/个人所得税税率",
                        "个人所得税税率"        
            )
        palyALL1(self,allParts)

class IncomeTax02(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "IncomeTax/个税扣除项",
                        "个人所得税扣除项"        
            )
        palyALL1(self,allParts)

class IncomeTax03(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "IncomeTax/个税收入来源",
                        "个人所得税包括项"        
            )
        palyALL1(self,allParts)

class IncomeTax04(Scene):
    def imageObjAnd1Text(self,imageName,text2,lsh=1):
        pic = ImageMobject(imageName).scale(1.2)
        picText2 = Text(text2, 
                        # font='Microsoft YaHei',
                        color=BLACK,
                        lsh=1.2
            )\
            .set_height(0.28*lsh)
        if picText2.get_width() > pic.get_width():
            picText2.set_width(pic.get_width()*0.96)
        picText2.next_to(pic,DOWN,buff=SMALL_BUFF*1.1)
        picAndText = Group(pic,picText2).center()
        pic.rect = RoundedRectangle(
                        corner_radius=0.1,
                        color="#DDDDDD",
                        fill_color = "#DDDDDD",
                        fill_opacity = 1,
                        height=picAndText.get_height()+0.2,
                        width=picAndText.get_width()+0.2
            )
        return Group(pic.rect,pic,picText2)
    def construct(self):
        allParts = self.imageObjAnd1Text(
                        "IncomeTax/应纳税收入",
                        "劳动报酬应纳税收入"        
            )
        palyALL1(self,allParts)

class IncomeTax05(Scene):
    def imageObjAnd1Text(self,imageName,text2,lsh=1):
        pic = ImageMobject(imageName).scale(1.5)
        picText2 = Text(text2, 
                        # font='Microsoft YaHei',
                        color=BLACK,
                        lsh=1.2
            )\
            .set_height(0.28*lsh)
        if picText2.get_width() > pic.get_width():
            picText2.set_width(pic.get_width()*0.96)
        picText2.next_to(pic,DOWN,buff=SMALL_BUFF*1.1)
        picAndText = Group(pic,picText2).center()
        pic.rect = RoundedRectangle(
                        corner_radius=0.1,
                        color="#DDDDDD",
                        fill_color = "#DDDDDD",
                        fill_opacity = 1,
                        height=picAndText.get_height()+0.2,
                        width=picAndText.get_width()+0.2
            )
        return Group(pic.rect,pic,picText2)
    def construct(self):
        allParts = self.imageObjAnd1Text(
                        "IncomeTax/应纳税预扣",
                        "劳动报酬应纳税预扣"        
            )
        palyALL1(self,allParts)

class IncomeTax06(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "IncomeTax/张三每个月的预缴个税",
                        "张三每个月的预缴个税"        
            )
        palyALL1(self,allParts)

class IncomeTax07(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "IncomeTax/综合所得额",
                        "综合所得额包括项"        
            )
        palyALL1(self,allParts)

class IncomeTax08(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "IncomeTax/奖金计税方式选择",
                        "奖金计税方式选择"        
            )
        palyALL1(self,allParts)

class IncomeTax09(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "IncomeTax/申报导入",
                        "申报导入"        
            )
        palyALL1(self,allParts)

class IncomeTax10(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "IncomeTax/填写扣除",
                        "专项扣除填写"        
            )
        palyALL1(self,allParts)


class keju01(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "keju/1、分封制金字塔",
                        "分封制金字塔", 
            )
        palyALL1(self,allParts)

class keju02(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "keju/2、隋文帝",
                        "隋文帝", 
            )
        palyALL1(self,allParts)

class keju03(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "keju/3、隋炀帝",
                        "隋炀帝", 
            )
        palyALL1(self,allParts)

class keju04(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "keju/4、范仲淹",
                        "范仲淹", 
            )
        palyALL1(self,allParts)

class keju05(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "keju/5、王安石",
                        "王安石", 
            )
        palyALL1(self,allParts)

class keju06(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "keju/6、司马光",
                        "司马光", 
            )
        palyALL1(self,allParts)

class keju07(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "keju/7、欧阳修",
                        "欧阳修", 
            )
        palyALL1(self,allParts)

class keju08(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "keju/8、朱元璋",
                        "朱元璋", 
            )
        palyALL1(self,allParts)

class keju09(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "keju/9、北京贡院",
                        "北京贡院", 
            )
        palyALL1(self,allParts)

class keju10(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "keju/10、慈禧太后",
                        "慈禧太后", 
            )
        palyALL1(self,allParts)

class keju11(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "keju/11、光绪帝",
                        "光绪帝", 
            )
        palyALL1(self,allParts)

class keju12(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "keju/12、康有为",
                        "康有为", 
            )
        palyALL1(self,allParts)

class keju13(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "keju/13、梁启超",
                        "梁启超", 
            )
        palyALL1(self,allParts)

class Txt1(Scene):
    def construct(self):
        txt = (
            "富家不用买良田，书中自有千钟粟。",
            "安居不用架高堂，书中自有黄金屋。",
            "出门无车毋须恨，书中有马多如簇。",
            "娶妻无媒毋须恨，书中有女颜如玉。",
            "男儿欲遂平生志，五经勤向窗前读。"
            )
        
        txtT = []
        for i in range(5):
            txtTmp = Text(txt[i])
            txtT.append(txtTmp)
        TxtGroup=VGroup(*txtT).arrange_submobjects(DOWN,buff=0.4)

        self.play(LaggedStartMap(Write,[obj for obj in TxtGroup],lag_ratio=1.5),run_time=10)
        self.wait()

class Txt2(Scene):
    def construct(self):
        txt = ("""
                    八股文是指文章的八个部分，文体有
            固定格式：由破题、承题、起讲、入题、
            起股、中股、后股、束股八部分组成，题
            目一律出自四书五经中的原文。""")
        txtTmp = Text(txt,lsh=1)
 
        self.play(Write(txtTmp))
        self.wait()

class Txt3(Scene):
    def construct(self):
        txt = (
            "离离原上草，一岁一枯荣。",
            "野火烧不尽，春风吹又生。",
            "远芳侵古道，晴翠接荒城。",
            "又送王孙去，萋萋满别情。",
            )
        
        txtT = []
        for i in range(4):
            txtTmp = Text(txt[i])
            txtT.append(txtTmp)
        TxtGroup=VGroup(*txtT).arrange_submobjects(DOWN,buff=0.4)

        self.play(LaggedStartMap(Write,[obj for obj in TxtGroup],lag_ratio=1.5),run_time=10)
        self.wait()

class Milk1(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Milk/1、巴氏奶制造运输流程",
                        "巴氏奶制造运输流程"        
            )
        palyALL1(self,allParts)

class Milk2(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "Milk/2、巴斯德",
                        "Louis Pasteur",
                        "路易·巴斯德"        
            )
        palyALL2(self,allParts)

class Milk3(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Milk/3、不同物质含钙量",
                        "不同物质的含钙量"        
            )
        palyALL1(self,allParts)

class Milk4(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Milk/4、乳糖耐受和乳糖不耐受原理",
                        "乳糖耐受与不耐受原理"        
            )
        palyALL1(self,allParts)

class Milk5(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "Milk/5、乳酸菌",
                        "Lactic Acid Bacteria",
                        "乳酸菌"        
            )
        palyALL2(self,allParts)

class Milk6(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Milk/6、骨质疏松图",
                        "骨质疏松的骨骼"        
            )
        palyALL1(self,allParts)

class Milk7(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Milk/7、世界各国乳糖不耐受比例",
                        "世界各国乳糖不耐受比例"        
            )
        palyALL1(self,allParts)

class Milk8(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Milk/8、钙摄入量建议图",
                        "钙摄入量建议图"        
            )
        palyALL1(self,allParts)

class Milk9(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Milk/9、骨量",
                        "不同时期人的骨量"        
            )
        palyALL1(self,allParts)

class Milk10(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "Milk/10、世界各国奶制品消费量",
                        "世界各国奶制品消费量"        
            )
        palyALL1(self,allParts)

class PrinceRupertsDrop01(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "PrinceRupertsDrop/prince-ruperts-drop",
                        "Prince Rupert's Drop",
                        "鲁珀特之泪",     
            )
        palyALL2(self,allParts)

class PrinceRupertsDrop02(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "PrinceRupertsDrop/glass",
                        "家用车内使用头枕的自救方法",
            )
        palyALL1(self,allParts)


class R01(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "R0/1、鲍里斯·约翰逊",
                        "Boris Johnson",
                        "鲍里斯·约翰逊"        
            )
        palyALL(self,allParts)

class R02(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "R0/2、帕特里克·瓦兰斯",
                        "Patrick Vallance",
                        "帕特里克·瓦兰斯"       
            )
        palyALL(self,allParts)

class R03(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "R0/3、陈薇院士",
                        "中国工程院院士",
                        "陈薇"       
            )
        palyALL(self,allParts)

class R04(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "R0/4、麻疹",
                        "Measles",
                        "麻疹"       
            )
        palyALL(self,allParts)

class R05(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "R0/5、部分疾病的R0值",
                        "The R0 of some diseases",
                        "部分疾病的R0值"       
            )
        palyALL(self,allParts)


class StockIndex1(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "StockIndex/1、道琼斯工业平均指数走势图",
                        "Dow Jones Industrial Average",
                        "道琼斯工业平均指数走势图"        
            )
        palyALL(self,allParts)

class StockIndex2(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "StockIndex/2、1947年上海证券交易所",
                        "Shanghai Stock Exchange in 1947",
                        "1947年上海证券交易所"        
            )
        palyALL(self,allParts)

class StockIndex3(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "StockIndex/3、查尔斯道",
                        "Charles Henry Dow",
                        "查尔斯·道"        
            )
        palyALL(self,allParts)

class StockIndex4(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "StockIndex/4、邓丽君",
                        "Teresa Teng",
                        "邓丽君"        
            )
        palyALL(self,allParts)

class StockIndex5(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "StockIndex/5、邓小平和约翰·范尔霖",
                        "Deng Xiaoping and John Joseph Phelan Jr.",
                        "邓小平和约翰·范尔霖"        
            )
        palyALL(self,allParts)

class StockIndex61(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
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
        allParts = imageObjAnd2Text(
                        "StockIndex/62、道琼斯指数涨幅排行",
                        "Largest daily point gains",
                        "道琼斯指数涨幅排行"        
            )
        palyALL(self,allParts)

class StockIndex7(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "StockIndex/7、约翰·范尔霖去上海过户",
                        "John goes to Shanghai",
                        "约翰·范尔霖去上海过户"        
            )
        palyALL(self,allParts)

class StockIndex8(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "StockIndex/8、飞乐音响股票",
                        "Feilo Acoustics Stock",
                        "飞乐音响股票"        
            )
        palyALL(self,allParts)
    
class StockIndex9(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "StockIndex/9、费城证券交易所",
                        "Philadelphia Stock Exchange",
                        "费城证券交易所"        
            )
        palyALL(self,allParts)

class StockIndex10(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "StockIndex/10、工商银行上海信托静安营业部",
                        "The Jing'an Sales Department of ICBC Shanghai",
                        "工商银行上海信托静安营业部"        
            )
        palyALL(self,allParts)

class StockIndex11(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "StockIndex/11、华尔街日报",
                        "The Wall Street Journal",
                        "华尔街日报"        
            )
        palyALL(self,allParts)

class StockIndex12(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "StockIndex/12、纳斯达克交易所",
                        "NASDAQ",
                        "纳斯达克交易所"        
            )
        palyALL(self,allParts)

class StockIndex13(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "StockIndex/13、纽约证券交易所",
                        "The New York Stock Exchange",
                        "纽约证券交易所"        
            )
        palyALL(self,allParts)

class StockIndex14(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "StockIndex/14、上海证券交易所",
                        "Shanghai Stock Exchange",
                        "上海证券交易所"        
            )
        palyALL(self,allParts)

class StockIndex15(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "StockIndex/15、上证综合指数走势图",
                        "SSE Index",
                        "上证综合指数走势图"        
            )
        palyALL(self,allParts)

class StockIndex16(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "StockIndex/16、深圳证券交易所",
                        "Shenzhen Stock Exchange",
                        "深圳证券交易所"        
            )
        palyALL(self,allParts)

class StockIndex17(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "StockIndex/17、梧桐树协议",
                        "Buttonwood Agreement",
                        "梧桐树协议"        
            )
        palyALL(self,allParts)

class StockIndex18(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "StockIndex/18、新民晚报",
                        "Xinmin Evening News",
                        "新民晚报"        
            )
        palyALL(self,allParts)

class StockIndex19(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "StockIndex/19、道琼斯指数12个原始股",
                        "The original 12 industrials",
                        "道琼斯指数12个原始股"        
            )
        palyALL(self,allParts)

class StockIndex20(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "StockIndex/20、深圳成份指数",
                        "SZSE Composite Index",
                        "深圳成份指数"        
            )
        palyALL(self,allParts)

class StockIndex21(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "StockIndex/21、道琼斯指数最近表现",
                        "The latest data on Dow Jones Industrial Average",
                        "道琼斯指数最近表现"        
            )
        palyALL(self,allParts)


class Tech01(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "teach/飞机投弹A",
                        "以飞机为参照的投弹轨迹",
            )
        palyALL1(self,allParts)

class Tech02(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "teach/飞机投弹B",
                        "以地面为参照的投弹轨迹",
            )
        palyALL1(self,allParts)

class Tech03(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "teach/伽利略·伽利莱",
                        "Galileo Galilei",
                        "伽利略·伽利莱",     
            )
        palyALL2(self,allParts)

class Tech04(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "teach/克劳狄乌斯·托勒密",
                        "Claudius Ptolemaeus",
                        "克劳狄乌斯·托勒密",     
            )
        palyALL2(self,allParts)

class Tech05(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "teach/尼古拉·哥白尼",
                        "Nicolaus Copernicus",
                        "尼古拉·哥白尼",     
            )
        palyALL2(self,allParts)

class Tech06(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "teach/约翰内斯·开普勒",
                        "Johannes Kepler",
                        "约翰内斯·开普勒",     
            )
        palyALL2(self,allParts)

class Tech07(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "teach/球坐标系",
                        "Spherical Coordinate System",
                        "球坐标系",     
            )
        palyALL2(self,allParts)

class Tech08(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "teach/柱坐标系",
                        "Cylindrical Coordinate system",
                        "柱坐标系",     
            )
        palyALL2(self,allParts)

class DeferentandEpicycle(Scene):
    def construct(self):
        self.t_offset=0
        orbit=Circle(radius=2.5,color=GREEN,stroke_width=8.32)
        orbitMin=Circle(radius=1,color=RED)
        planet=Dot(radius=0.2)
        earth = ImageMobject("teach/earth").scale(0.832)
        cross = Cross(orbit).scale(0.03).set_color(GRAY)
        earth.move_to(DOWN*0.5)
        text1=Text("均轮",color=GREEN)
        text1.to_corner(UR).shift(1.5*LEFT)
        text2=Text("本轮",color=RED)
        text2.next_to(text1,DOWN)
        orbitMin.move_to(orbit.point_from_proportion(0))
        planet.move_to(orbitMin.point_from_proportion(0))

        def update_planet(mob,dt):
            rate=dt*0.1
            if self.t_offset>2:
                rate = 0
            mob.move_to(orbitMin.point_from_proportion(((self.t_offset + rate))%1))
            self.t_offset += rate

        planet.add_updater(update_planet)
        self.add(cross)
        self.play(FadeInFromLarge(earth))
        self.play(Write(orbit),ShowCreation(orbitMin))
        self.play(Write(text1),Write(text2))
        self.add(planet)
        self.play(Rotate(orbitMin,PI*10/3,about_point=ORIGIN,rate_func=linear,run_time=20))
        self.wait()


class WTI200501(Scene):
    def construct(self):
        allParts = imageObjAnd1Text(
                        "WTI2005/2020年4月20日WTI原油2005合约价格变化",
                        "2020年4月20日WTI原油2005合约价格变化"  
            )
        palyALL1(self,allParts)

class WTI200502(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "WTI2005/芝加哥期货交易所",
                        "The Chicago Board of Trade (CBOT)",
                        "芝加哥期货交易所"
            )
        palyALL2(self,allParts)

class WTI200503(Scene):
    def construct(self):
        allParts = imageObjAnd2Text(
                        "WTI2005/芝加哥商品交易所",
                        "The Chicago Mercantile Exchange (CME)",
                        "芝加哥商品交易所"
            )
        palyALL2(self,allParts)
