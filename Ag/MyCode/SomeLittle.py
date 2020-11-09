from Ag.MyCode.imports_ag import *

class Some1(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "SomeLittle/电磁波蓝移与红移",
                        "电磁波的蓝移与红移",
            )
        palyALL1(self,allParts)

class Some2(Scene):
    def construct(self):
        allParts = ObjAnd1Text(
                        "SomeLittle/经典多普勒效应",
                        "经典多普勒效应",
            )
        palyALL1(self,allParts)