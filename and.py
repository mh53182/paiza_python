# 論理積：AもBも真なら真
# if文で書くとこう

# A, B = map(int, input().split())

# if A == 1 and B == 1:
#     print(1)
# else:
#     print(0) 

# and演算子を使うとこう
a, b = map(int, input().split())
print(a and b)


print('#############')

# 論理和：AまたはBが真なら真、も同じく
a, b = map(int, input().split())
print(a or b)


print('##########################')

# 否定の場合
a = int(input())
print(int(not a)) # intに変換しないとtrue/falseが出力される

print('##########################')

# 排他的論理和(XOR)の場合
# 両方真・または両方偽の場合は偽
a, b = map(int, input().split())
print(a ^ b) # 演算子は"^"


print('##########################')
# 以下、まだメモ

# NOR演算(否定的論理和）
print(int(not(A or B)))
# NAND演算(否定的論理積）
print(int(not(A and B)))
# XNOR演算(排他的否定的論理和）
print(int(not(A ^ B)))