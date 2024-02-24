# 変数 N を 0 で初期化する
# N に 3,286 を足した値を N へ代入する
# N に 4,736 をかけた値を N へ代入する
# N を 12,312 で割った余りを N へ代入する
# N を出力する

N = 0
N = N + 3286
N = N * 4736
N = N % 12312
print(N)

print('#########')

input_line1 = input()
input_line2 = input()
print(input_line1)
print(input_line2)

print('#########')

# 半角スペースを含むデータを受け取って、スペースで改行して表示
# パターン1　スペースを改行に置換
input_line3 = input('スペースを含んで入力').replace(' ', '\n')
print(input_line3)

# パターン2　受け取ったデータをスペースで2つに分割し、それぞれ別の変数に代入する
input_line4, input_line5 = input().split(' ')
print(input_line4)
print(input_line5)

# もっとたくさん繰り返す
for i in range(10):
    s = input()
    print(s)

# 規定の文字列をスペースごとに改行出力
# パターン1
s = "one two three four five"
for i in s.split(" "):
    print(i)

# パターン2
s = "one two three four five"
a, b, c, d, e = s.split(" ")
print(s.replace(" ", "\n"))

print('################')

# 数列の長さが与えられる
# 数列がスペース区切りで与えられる
# 探索すべき値が与えられる
# 値が数列の何番目にあるか(インデックス0を1番目とする)改行出力

# 模範解答
n = int(input())
a = [int(x) for x in input().split()]
k = int(input())

for i in range(n):
    if a[i] == k:
        print(i + 1)


# 提出したコード
n = int(input())
l = []

# 数列の格納が1行入力ではない
for i in range(n):
    num = int(input())
    l.append(num)

t = int(input())

# rangeの引数の取り方に注意
for i in range(n):
    if l[i] == t:
        print(i + 1)

# 修正版
n = int(input())
l = [int(x) for x in input().split(' ')]
t = int(input())

for i in range(len(l)):
    print('i=', i)
    print('L=', l[i])
    if l[i] == t:
        print(i + 1)

print('################')

N, M = input().split(' ')
n = int(N)
m = int(M)
A = [int(x) for x in input().split(' ')]

for i in range(len(A)):
    if i - 1 == m:
        print(A[i])

print('#################')

A, B, C, D = map(int, input().split())
N = ((A + B) * C) ** 2 % D
print(N)

print('#######################')

# 連続するハイフンをひとつにするプログラム
s = input()

list = [str(x) for x in s]

for i in range(len(list)-1, 0, -1):
    if list[i] == "-" and list[i - 1] == "-":
        # removeは引数に一致するデータをリストから削除するので、ここではインデックス指定のpopを使う
        list.pop(i)

print(''.join(list))

print('#########################')

# 食べたいものとメニューを照らし合わせる

s = input()
n = int(input())
t = list(input().split())

# for i in range(n):
#     if t[i] == s:
#         print('yes')
#         break
#     else:
#         print('no')

# ループを回さなくても"in"を使えばリスト内に一致するデータがあるか確認できる
if s in t:
    print('Yes')
else:
    print('No')

print('######################')

# n個の文字列を連結して出力する。
n = int(input())

# リストに入れてリストの中身を連結した
# list = []
# for _ in range(n):
#     list.append(input())

# print(''.join(list))

# 直接変数に突っ込む方法も。
ans = ""
for _ in range(n):
    ans += input()

print(ans)

print('#######################')

# 与えられた文字列sの中の何番目にcがあるか
s = input()
c = input()

# 失敗
# for i in range(len(s)-1, 0):
#     print(s[i])
#     if c == s[i]:
#         print(i)

# enumerate(s)でインデックス番号と要素を同時にループ処理する
for i, ele in enumerate(s):
    if ele == c:
        print(i + 1)

# findメソッド使えば1行
print(s.find(c) + 1)


print('################')

# 与えられた文字列sのi文字目からj文字目までを出力
s = input()
i, j = map(int, input().split())

print(s[i - 1 : j])

print('################')

# 文字列sのn文字目の後ろに文字列tを挿入して出力
# ※文字列はイミュータブルなのでsそのものは書き換えられない
s = input()
t = input()
n = int(input())

print(s[:n], end='')
print(t, end='')
print(s[n:])

# 出力はこれ1行でよかった
print(s[:n] + t + s[n:])

print('#########################')

# 入力値X、Yの和のN文字目を出力

X = int(input())
Y = int(input())
N = int(input())
sum = X + Y
ans = str(sum)
print(ans[N-1])

print('##################')

# 入力された文字列sの大文字と小文字を入れ替える

# メソッドひとつで一発
s = input()
print(s.swapcase())

# 模範解答はこちら
s = input()

for ele in s:
    # islowerで小文字かどうかを判定、小文字なら大文字で出力して改行を回避、elseもまた然り
    if ele.islower():
        print(ele.upper(), end="")
    else:
        print(ele.lower(), end="")

print('######################')

# 入力された文字列Sに文字列Tと一致する部分はあるか？

S = input()
T = input()

if T in S:
    print('YES')
else:
    print('NO')

print('#####################')

# 文字列の反転
# 文字列はイミュータブルなので直接書き換えることはできない

s = input()
# 直接　print(s[::-1])としてもOK
s_reverse = s[::-1]
print(s_reverse)