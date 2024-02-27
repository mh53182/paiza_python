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