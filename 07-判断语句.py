# if <条件判断1>:
#     <执行1>
# elif <条件判断2>:
#     <执行2>
# elif <条件判断3>:
#     <执行3>
# else:
#     <执行4>
weight = 50
height = 1.70
bmi = weight / (height * height)
if bmi < 18.5:
    print("过轻")
elif bmi < 25 and bmi > 18.5:
    print("正常")
elif bmi < 28 and bmi > 25:
    print("过重")
elif bmi < 32 and bmi > 28:
    print("肥胖")
else:
    print("严重肥胖")
