#随机整数：rnum，随机真分数分子：snum，随机真分数分母：mnum
#随机四则运算符：rsign
#出题数：qes
#式子项数：rtype，式子最大项数：maxone
#第一代为二阶运算
#封装函数一：整数求解函数：zsResult()；封装函数二：真分数求解函数：zfsResult()；运算函数：result(bo,k)

import math
import random
import cProfile
from fractions import Fraction

def zsResult():            #整数运算
    qes = int(input())
    maxone = int(input())
    for a in range(qes):
        result(1,maxone)   #调用实际运算函数result(bo,k)


def zfsResult():           #真分数运算
    qes = int(input())
    maxone = int(input())
    for b in range(qes):
        result(2,maxone)   #调用实际运算函数result(bo,k)

def result(bo,k):          #运算函数分类别计算
    contain = ''
    num = 0
    rtype = random.randint(2,k)          #生成随机项目数
    if bo == 1:
        for i in range(rtype):           #生成随机数以及随机运算符
            rsign = random.choice(['+','-','*','/'])  
            rnum1 = random.randint(0,100)
            contain += str(rnum1)+str(rsign)
            num += 1
            if num == rtype:
                contain = contain[0:-1] + '='     #置换最后一个字符为“=”放在contain字符串中
                rescon = contain.replace('=','')  #置换最后一个字符为空放在rescon字符串中
        if eval(rescon) < 0:                      #判断结果是否为负数
            print('***结果为负数，不显示***')
        print('式子为：{}{}'.format(contain,eval(rescon)))#输出
    else:
        for i in range(rtype):
            #生成随机真分数以及随机运算符
            rsign = random.choice(['+','-','*','/'])  
            snum1 = random.randint(0,100)
            mnum1 = random.randint(1,100)
            zfs1 = Fraction(snum1, mnum1)
            contain += str(zfs1)+str(rsign)
            num += 1
            if num == rtype:
                contain = contain[0:-1] + '='
                rescon = contain.replace('=','')
        if eval(rescon) < 0:
            print('***结果为负数，不显示***')
        print('式子为：{}{}'.format(contain,eval(rescon)))#输出

 
def main():                        #主函数
    fangshi = str(input())
    if fangshi == 'zs':
        zsResult()
    elif fangshi == 'zfs':
        zfsResult()
    else:
        print('输入有误，请重新输入！')

cProfile.run('main()')             #效能分析
main()


