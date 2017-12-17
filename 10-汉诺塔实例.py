# def move(n,a,b,c):
#     global s
#     if n==1:
#         print(a,'-->',c)
#         s += 1
#         return
#     move(n-1,a,c,b)
#     move(1,a,b,c)
#     move(n-1,b,a,c)
# move(3,'A','B','C')
# print(s)

s = 0


def move(n, a='A', b='B', c='C'):  # move(盘子个数，起点，缓冲区，终点）
    global s
    if n == 1:
        print(a, '-->', c)
        s = s + 1
        return
    else:  # 汉诺塔可以抽象为两个盘子（(n-1)+1)
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)

# n - 1代表当前被移动的盘子数
# n = int(input('请输入盘子数'))
move(4)
print(s)
