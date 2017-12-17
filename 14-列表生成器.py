# -*- coding: utf-8 -*-
# 生成一个自然数,非常简单

list(range(1, 11))

print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])


# 请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
# L1 = ['Hello', 'World', 18, 'Apple', None]
# L2 = []
# for x in L1:
#     if isinstance(x, str):
#         L2.append(lower(x))
# print(L2)
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x, str)]
print(L2)