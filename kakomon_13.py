# 文字列 a と文字列 b が与えらます。
# b の先頭に a が現れるならば、"Yes" を、そうでないならば "No" を出力してください。
# さらに、a の先頭に b が現れるならば、"Yes" を、そうでないならば "No" を出力してください。

a = input()
b = input()

if b.startswith(a):
    print('YES')
else:
    print('NO')

if a.startswith(b):
    print('YES')
else:
    print('NO')

print('#######################')

# n 個の整数が与えられます。
# それらの合計値と平均値を計算して出力してください。
# 計算した値は小数点以下を切り捨てて出力してください。

# 提出解
n = int(input())
A = []
for i in range(n):
    a = int(input())
    A.append(a)

ave = sum(A) // n
print(sum(A))
print(ave)

# 模範解答
n = int(input())

# リストにせず変数sumに足していく
sum = 0
for i in range(n):
    sum += int(input())

avg = sum // n

print(sum)
print(avg)

print('#######################')

# 3辺の長さがそれぞれ a, b, c である三角形が二等辺三角形であれば、"Yes"をそうでないならば、"No"を出力してください。
# 二等辺三角形とは、2つの辺の長さが等しい三角形のことです。

a = int(input())
b = int(input())
c = int(input())

if a == b or a == c:
    print('Yes')
# 以下の行もorでif文に一緒に繋げればOK　なぜ分けた
elif b == c:
    print('Yes')
else:
    print('No')

print('#######################')

# パイザ君はダイエットのため 1 日 2 食で生活しており、パイザ君の自宅にはおにぎりが a 個、パンが b 個あります。
# パイザ君は飽き性のため、なるべく 1 日に同じ種類の食べ物を食べたくありません。
# この場合、1 日に異なる 2 種類の食べ物を食べられる最大の日数と 1 日に同じ種類の食べ物を 2 回食べなければならない日数を求めてください。

# 提出解
a, b = map(int, input().split())

if a > b:
    print(b, (a-b) // 2)
elif a < b:
    print(a, (b-a) // 2)
else:
    print(a, 0)

# 模範解答　※2行!!!
a, b = map(int, input().split())
# abs(x)関数で絶対値（absolute）を返す
print(min(a, b), abs(a - b) // 2)

print('#######################')

# ある占いでは、n 個のサイコロを振り、各々の数字の総和が 7 の倍数であれば大吉と言われています。
# この占いのルールに準じて、n 個のサイコロ各々の数字が与えられるとき、大吉かどうかを判定してください。

n = int(input())
m = list(map(int, input().split()))
sum = 0

for i in range(n):
    sum += m[i]

if sum % 7 == 0:
    print('Yes')
else:
    print('No')

print('#######################')