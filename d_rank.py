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