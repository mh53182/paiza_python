# 要素数の出力

L = [5, 1, 3, 4, 5, 12, 6, 8, 1, 3]
print(len(L))

print('#####################')

# 配列の入力

li = list(map(int, input().split()))
# 提出した回答
for i in range(len(li)):
    print(li[i])

# 模範回答　※入力受付時、li = input().split()　で文字列のリストとして受け取っている。
for a in li:
    print(a)

print('##################')

n = int(input())
A = input().split()

for a in A:
    print(a)

print('##################')

# 1 行目に整数 N と整数 K が与えられます。
# 2 行目に N 個の整数 a_i (1 ≤ i ≤ N) が半角スペース区切りで与えられます。
# K 番目の整数 a_K を出力してください。

n, k = map(int, input().split())
li = list(map(int, input().split()))
print(li[k-1])

