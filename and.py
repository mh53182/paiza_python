# AもBも真なら真
# if文で書くとこう

# A, B = map(int, input().split())

# if A == 1 and B == 1:
#     print(1)
# else:
#     print(0) 


# and演算子を使うとこう
a, b = map(int, input().split())
print(a and b)