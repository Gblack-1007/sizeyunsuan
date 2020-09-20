#随机整数：rnum，随机真分数分子：snum，随机真分数分母：mnum
#随机四则运算符：rsign
#出题数：qes
#/第一代为二阶运算
#封装函数一：整数求解函数：zsResult；封装函数二：真分数求解函数：zfsResult；运算函数：result

import math
import random
import cProfile
import profile
from fractions import Fraction

def zsResult():
    qes = int(input())
    for a in range(qes):
        rsign = random.choice(['+','-','*','/'])  
        rnum1 = random.randint(0,100)
        rnum2 = random.randint(0,100)
        if rnum1 < rnum2:
            rnum1 = max(rnum1, rnum2)
            rnum2 = min(rnum1, rnum2)
            result(rsign,rnum1,rnum2)
        else:
            result(rsign,rnum1,rnum2)

def zfsResult():
    qes = int(input())
    for b in range(qes):
        rsign = random.choice(['+','-','*','/'])  
        snum1 = random.randint(0,100)
        mnum1 = random.randint(1,100)
        zfs1 = Fraction(snum1, mnum1)
        snum2 = random.randint(1,100)
        mnum2 = random.randint(1,100)
        zfs2 = Fraction(snum2, mnum2)
        if zfs1 < zfs2:
            zfs1 = max(zfs1, zfs2)
            zfs2 = min(zfs1, zfs2)
            result(rsign,zfs1,zfs2)
        else:
            result(rsign,zfs1,zfs2)

def result(s,n1,n2):
    if s == '+':
        print('{} + {} = {}'.format(n1,n2,n1 + n2))
    elif s == '-':
        print('{} - {} = {}'.format(n1,n2,n1 - n2))
    elif s == '*':
        print('{} * {} = {}'.format(n1,n2,n1 * n2))
    elif s == '/':
        if n2 == 0:
            print('***除数不能为零***')
        else:
            print('{} / {} = {}'.format(n1,n2,n1 / n2))
    else:
        print('输入有误，请重新输入！')
 
def main():
    fangshi = str(input())
    if fangshi == 'zs':
        zsResult()
    elif fangshi == 'zfs':
        zfsResult()
    else:
        print('输入有误，请重新输入！')
        
cProfile.run('main()') 
main()
