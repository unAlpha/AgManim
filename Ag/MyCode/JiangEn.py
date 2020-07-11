import numpy
 
class helixMatrix():
    def __init__(self,BeginValu=1,Step=1,ChartSize=11):
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
    def Num90(self,Num,CW):
        if self.Step<0:
            CW=-CW
        if CW != 1 and CW != -1:
            raise Exception("请带参数，正转1，反转-1 ……")
        (x,y) = self.Num2XY(Num)
        if abs(x) == abs(y):
            raise Exception("值位于角线上，无90角转值 ……")
        if CW == -1:
            if x>=0 and abs(x)>abs(y):
                return self.XY2Num(y,x)
            if abs(y)>abs(x):
                return self.XY2Num(-y,-x)
            if x<0 and abs(x)>abs(y):
                return self.XY2Num(y-1,x+1)
        if CW == 1:
            if abs(x)>abs(y):
                return self.XY2Num(-y,-x)
            if y>=0 and abs(y)>abs(x):
                return self.XY2Num(y,x)
            if y<0 and abs(y)>abs(x):
                return self.XY2Num(y-1,x+1)

    # 180度转角数
    def Num180(self,Num,CW):
        if self.Step<0:
            CW=-CW
        if CW != 1 and CW != -1:
            raise Exception("请带参数，正转1，反转-1 ……")
        (x,y) = self.Num2XY(Num)

        if abs(x) == abs(y):
            raise Exception("值位于角线上，无180角转值 ……")

        if CW == -1:
            if x>=0 and abs(x)>abs(y):
                return self.XY2Num(-x,y)
            if y>=0 and abs(y)>abs(x):
                return self.XY2Num(x,-y+1)
            if x<0 and abs(x)>abs(y):
                return self.XY2Num(-x-1,y)
            if y<0 and abs(y)>abs(x):
                return self.XY2Num(x,-y)
        if CW == 1:
            if x>=0 and abs(x)>abs(y):
                return self.XY2Num(-x-1,y)
            if y>=0 and abs(y)>abs(x):
                return self.XY2Num(x,-y)
            if x<0 and abs(x)>abs(y):
                return self.XY2Num(-x,y)
            if y<0 and abs(y)>abs(x):
                return self.XY2Num(x,-y+1) 

    # 风车位的角线数
    def JiaoXian(self,Num,CW):
        # 仅配合风车位使用
        if self.Step<0:
            CW=-CW
        if CW != 1 and CW != -1:
            raise Exception("请带参数，正转1，反转-1 ……")
        (x,y) = self.Num2XY(Num)
        # print((x,y))
        if CW == -1:
            if x>=0 and y>=0:
                if x==y:
                    return self.XY2Num(-x+1,-y+1)
                return self.XY2Num(-y,-x)
            if x<=0 and y>=0:
                return self.XY2Num(y-1,x+1)
            if x<=0 and y<=0:
                if abs(x)>abs(y):
                    return self.XY2Num(-y-1,-x-1)
                else:
                    return self.XY2Num(-y,-x)
            if x>=0 and y<=0:
                return self.XY2Num(y,x)
            
        if CW == 1:
            if x>=0 and y>=0:
                if abs(y)>abs(x):
                    return self.XY2Num(-y-1,-x-1)
                else:
                    return self.XY2Num(-y,-x)
            if x<=0 and y>=0:
                return self.XY2Num(y,x)
            if x<=0 and y<=0:
                if abs(y)>abs(x):
                    return self.XY2Num(-y+1,-x+1)            
                else:  
                    return self.XY2Num(-y,-x)
            if x>=0 and y<=0:
                return self.XY2Num(y-1,x+1)

    # 过滤相连的目标数
    def FilterNumbers(self, num, CW, dnum=2):
        if not isinstance(num,list):
            return Exception("需要给个list……")
        if CW == 1:
            verse = False
        else:
            verse = True
        numSort = sorted(num, reverse = verse)
        delnumSort = []
        for i in range(len(numSort)):
            if i>0:
                if abs(numSort[i-1]-numSort[i]) <= dnum:
                    delnumSort.append(numSort[i])
        for delnum in delnumSort:
            numSort.remove(delnum)
        # print(delnumSort)
        return numSort
    
    # 风车位推图
    def Windmill(self,Num,CW,n):
        if CW != 1 and CW != -1:
            raise Exception("请带参数，正转1，反转-1 ……")
        if n<1:
            raise Exception("请输入要求的个数")
        (x,y) = self.Num2XY(Num) 
        WindmillTaget = []
        if abs(x)>2*abs(y) or abs(y)>2*abs(x):
            for i in range(n):
                if i!=0:
                    WindmillTaget.append(self.Num180(WindmillTaget[i-1],CW))
                else:
                    WindmillTaget.append(self.Num180(Num,CW)) 
            return WindmillTaget
        else:
            for i in range(n):
                if i!=0:
                    WindmillTaget.append(self.JiaoXian(WindmillTaget[i-1],CW))
                else:
                    WindmillTaget.append(self.JiaoXian(Num,CW)) 
            return WindmillTaget

    # Constellate推图
    def Constellate(self,Num,CW,N,dnum=2):
        if N<0:
            raise Exception("请输入大于1的段数")
        if self.BeginValu!=1:
            raise Exception("请使用基数1")
        num11 = self.Num90(Num,CW)
        num21 = self.Num180(Num,CW)
        num22 = self.Num90(num11,CW)
        num31 = self.Num180(num11,CW)
        num32 = self.Num90(num21,CW)
        num33 = self.Num90(num22,CW)       
        num1 = [num11]
        num2 = self.FilterNumbers([num21,num22],CW,dnum) 
        num3 = self.FilterNumbers([num31,num32,num33],CW,dnum) 
        num = [num1,num2,num3]
        if N>3:
            for i in range(3+1,N+1):
                newlist = []
                for ber1 in num[i-2]:
                    newlist.append(self.Num90(ber1,CW))
                for ber2 in num[i-3]:
                    newlist.append(self.Num180(ber2,CW))
                num.append(self.FilterNumbers(newlist,CW,dnum))
        return num[:N]

    # 同位阶
    def Apposition(self,Num,CW):
        n1 = self.Num180(Num,CW)
        n2 = self.Num90(n1,-CW)
        n3 = self.Num90(n2,-CW)
        
        m1 = self.Num90(Num,CW)
        m2 = self.Num90(m1,CW)
        m3 = self.Num180(m2,-CW)

        if n3 == m3:
            return n3
        else:
            return "无同位阶"

    # 四角推图
    def FourCorners(self,Num,CW,N):
        if N<0:
            raise Exception("请输入大于1的段数")
        num11 = self.Num90(Num,CW)
        num12 = self.Num180(num11,-CW)
        num = [[num11,num12]]
        if N>1:
            for i in range(1,N):
                num90 = self.Num90(num[i-1][0],CW)
                num180 = self.Num180(num90,-CW)
                num.append([num90,num180])
        return num[:N]

    # 夹角推图
    def Angle(self,num1,num2,step,chartSize,n=6,dnum=2):
        # n为对比的个数
        self.ChartSize = chartSize
        if num1==num2:
            return "两数相等无夹角"
        else:
            nummax = max([num1,num2])
            nummin = min([num1,num2])
        self.BeginValu = nummax
        self.Step = -abs(step)
        num1Windmill = self.Windmill(nummin,1,n)
        self.BeginValu = nummin
        self.Step = abs(step)
        num2Windmill = self.Windmill(nummax,-1,n)
        # 筛选的数与方向无关
        print(num1Windmill)
        print(num2Windmill)
        numSort = sorted(self.FilterNumbers(num1Windmill,1,dnum)\
            +self.FilterNumbers(num2Windmill,1,dnum))
        # print(numSort)
        delnumSort = []
        for i in range(len(numSort)):
            if i>0:
                if abs(numSort[i-1]-numSort[i]) > dnum:
                    delnumSort.append(numSort[i])
        delnumSort.append(numSort[0])
        # print(delnumSort)
        for delnum in delnumSort:
            numSort.remove(delnum)
        return numSort

if __name__ == '__main__':

    # 风车位
    # print(
    #     helixMatrix(BeginValu=506, Step=1, ChartSize=10)\
    #     .Windmill(750, CW=1, n=6)
    #     )

    # 夹角位
    print(helixMatrix()\
        .Angle(1818, 1773, step=1, chartSize=10, n=6))