from random import choice

def stay():
    doors = ['car','goat','goat']       #设置三扇门，其中两扇门后面是山羊，一扇门后是汽车
    choose = choice(doors)              #随机选择一扇门
    if choose == 'car':                 #不换门则直接判断
        return 'win'
    else:
        return 'lose'

def switch():
    doors = ['car', 'goat', 'goat']
    choose = choice(doors)
    doors.remove(choose)               #选择的门放一边
    doors.remove('goat')               #剩下的门，去掉一只山羊
    if doors == ['car']:               #换门
        return 'win'
    else:
        return 'lose'

if __name__ == '__main__':
    total = 100000
    count_switch = 0
    win_switch = 0
    count_stay = 0
    win_stay = 0
    for i in range(total):
        choose = choice([1,2])          #随机选择换门还是不换门
        if choose == 1:
            count_switch += 1
            if switch() == 'win':
                win_switch += 1
        else:
            count_stay += 1
            if stay() == 'win':
                win_stay += 1

    print('换门次数:',count_switch)
    print('换门后得到汽车:',win_switch,'%.2f%%'%(100*win_switch/count_switch))
    print('不换门:',count_stay)
    print('不换门后得到汽车:',win_stay,'%.2f%%'%(100*win_stay/count_stay)) 
    