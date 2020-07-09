import numpy
 
class helixMatrix():
    def __init__(self,BeginValu,Step,ChartSize):
        self.BeginValu=BeginValu
        self.ChartSize = ChartSize
        self.Step = Step
        self.MaxNums = (2*ChartSize+1)**2
    # 把数字转成坐标
    def Num2XY(self,Nums):
        NumInCycle = 0
        Num = (Nums-self.BeginValu+self.Step)/self.Step
        if Num > self.MaxNums:
            raise Exception("矩阵过小，请放大ChartSize ……")
        else:
            for i in range(1,self.ChartSize+1):
                if Num>(2*i-1)**2 and Num<=(2*i+1)**2:
                    NumInCycle = i
        
        NsqareNum = 2*NumInCycle+1

        if Num > (2*NumInCycle-1)**2 + NsqareNum*0 and Num < (2*NumInCycle-1)**2+NsqareNum*1-0:
            x = -NumInCycle
            y = Num - (2*NumInCycle-1)**2 - NsqareNum*0 -NumInCycle + 0
        
        if Num >= (2*NumInCycle-1)**2 + NsqareNum*1  and Num < (2*NumInCycle-1)**2+NsqareNum*2-1:
            x = Num - (2*NumInCycle-1)**2 - NsqareNum*1 -NumInCycle + 1
            y = NumInCycle

        if Num >= (2*NumInCycle-1)**2 + NsqareNum*2-1 and Num < (2*NumInCycle-1)**2+NsqareNum*3-2:
            x = NumInCycle
            y = - Num + (2*NumInCycle-1)**2 + NsqareNum*2 + NumInCycle - 2

        if Num >= (2*NumInCycle-1)**2 + NsqareNum*3-2  and Num < (2*NumInCycle-1)**2+NsqareNum*4-3:
            x = - Num + (2*NumInCycle-1)**2 + NsqareNum*3 + NumInCycle - 3
            y = - NumInCycle
        if x<0 or y<0:
            raise Exception("超出下(0,0)范围")
        return (x,y)
    # 把坐标转成数字    
    def XY2Num(self,x,y):
        if abs(y)>=abs(x):
            NumInCycle = abs(y)
            NsqareNum = (2*NumInCycle+1)
            if y < 0:
                Num = -x + (2*NumInCycle-1)**2 + NsqareNum*3 + NumInCycle - 3
            else:
                Num = x + (2*NumInCycle-1)**2 + NsqareNum*1 + NumInCycle - 1
        else:
            NumInCycle = abs(x)
            NsqareNum = 2*NumInCycle+1
            if x < 0:
                Num = y + (2*NumInCycle-1)**2 + NsqareNum*0 + NumInCycle + 0
            else:
                Num = -y + (2*NumInCycle-1)**2 + NsqareNum*2 + NumInCycle -2
        
        return Num*self.Step-self.Step+self.BeginValu

    # 90度转角数
    def Num90(self,Num,positiveORnegative):
        if self.Step<0:
            positiveORnegative=-positiveORnegative
        if positiveORnegative != 1 and positiveORnegative != -1:
            raise Exception("请带参数，正转1，反转-1 ……")
        (x,y) = self.Num2XY(Num)
        if abs(x) == abs(y):
            raise Exception("值位于角线上，无90角转值 ……")
        if positiveORnegative == -1:
            if x>=0 and abs(x)>abs(y):
                return self.XY2Num(y,x)
            if abs(y)>abs(x):
                return self.XY2Num(-y,-x)
            if x<0 and abs(x)>abs(y):
                return self.XY2Num(y-1,x+1)
        if positiveORnegative == 1:
            if abs(x)>abs(y):
                return self.XY2Num(-y,-x)
            if y>=0 and abs(y)>abs(x):
                return self.XY2Num(y,x)
            if y<0 and abs(y)>abs(x):
                return self.XY2Num(y-1,x+1)
    # 180度转角数
    def Num180(self,Num,positiveORnegative):
        if self.Step<0:
            positiveORnegative=-positiveORnegative
        if positiveORnegative != 1 and positiveORnegative != -1:
            raise Exception("请带参数，正转1，反转-1 ……")
        (x,y) = self.Num2XY(Num)

        if abs(x) == abs(y):
            raise Exception("值位于角线上，无90角转值 ……")

        if positiveORnegative == -1:
            if x>=0 and abs(x)>abs(y):
                return self.XY2Num(-x,y)
            if y>=0 and abs(y)>abs(x):
                return self.XY2Num(x,-y+1)
            if x<0 and abs(x)>abs(y):
                return self.XY2Num(-x-1,y)
            if y<0 and abs(y)>abs(x):
                return self.XY2Num(x,-y)
        if positiveORnegative == 1:
            if x>=0 and abs(x)>abs(y):
                return self.XY2Num(-x-1,y)
            if y>=0 and abs(y)>abs(x):
                return self.XY2Num(x,-y)
            if x<0 and abs(x)>abs(y):
                return self.XY2Num(-x,y)
            if y<0 and abs(y)>abs(x):
                return self.XY2Num(x,-y+1)

    def JiaoXian(self,Num,positiveORnegative):
        # 仅配合风车位使用
        if self.Step<0:
            positiveORnegative=-positiveORnegative
        if positiveORnegative != 1 and positiveORnegative != -1:
            raise Exception("请带参数，正转1，反转-1 ……")
        (x,y) = self.Num2XY(Num)
        if positiveORnegative == -1:
            if x>0 and y>0:
                if x==y:
                    return self.XY2Num(-x+1,-y+1)
                return self.XY2Num(-y,-x)
            if x<0 and y>0:
                return self.XY2Num(y-1,x+1)
            if x<0 and y<0:
                if abs(y)>abs(x):
                    return self.XY2Num(-y-1,-x-1)
                else:
                    return self.XY2Num(-y,-x)
            if x>0 and y<0:
                return self.XY2Num(y,x)
            
        if positiveORnegative == 1:
            if x>0 and y>0:
                if abs(y)>abs(x):
                    return self.XY2Num(-y-1,-x-1)
                else:
                    return self.XY2Num(-y,-x)
            if x<0 and y>0:
                return self.XY2Num(y,x)
            if x<0 and y<0:
                if abs(y)>abs(x):
                    return self.XY2Num(-y+1,-x+1)            
                else:  
                    return self.XY2Num(-y,-x)
            if x>0 and y<0:
                return self.XY2Num(y-1,x+1)

    # 风车位推图
    def Windmill(self,Num,positiveORnegative,n):
        if positiveORnegative != 1 and positiveORnegative != -1:
            raise Exception("请带参数，正转1，反转-1 ……")
        if n<1:
            raise Exception("请输入要求的个数")
        (x,y) = self.Num2XY(Num)
        WindmillTaget = []
        if abs(x)>2*abs(y) or abs(y)>2*abs(x):
            for i in range(n):
                if i!=0:
                    WindmillTaget.append(self.Num180(WindmillTaget[i-1],positiveORnegative))
                else:
                    WindmillTaget.append(self.Num180(Num,positiveORnegative)) 
            return WindmillTaget
        else:
            for i in range(n):
                if i!=0:
                    WindmillTaget.append(self.JiaoXian(WindmillTaget[i-1],positiveORnegative))
                else:
                    WindmillTaget.append(self.JiaoXian(Num,positiveORnegative)) 
            return WindmillTaget

    # 四角推图
    def FourCorners(self,Num,positiveORnegative,N):
        pass

if __name__ == '__main__':
    BeginValu = 922
    Step = -1
    ChartSize = 15
    JinagEnMatrix = helixMatrix(BeginValu,Step,ChartSize)
    print(JinagEnMatrix.Windmill(807,1,3))
