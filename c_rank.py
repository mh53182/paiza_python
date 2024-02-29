# アリスさんはじゃんけんが大好きで、過去に何度も友達のボブさんとじゃんけんを行いました。
# 手元には、アリスさんとボブさんとの間で、過去に行われたじゃんけんの結果を全て記録したノートがあります。

# ノートの記録を元に、過去にアリスさんはボブさんに何回勝ったかを出力するプログラムを作成してください。

# ・1 行で過去に行われたじゃんけんの回数を表す整数 N が与えられます。
# ・続く N 行のうちの i 行目 (1 ≦ i ≦ N) には、(i 回目のじゃんけんにおいてアリスさんが出した手)、
#     (i 回目のじゃんけんにおいてボブさんが出した手) を表す文字列 A_i, B_i がこの順で半角スペース区切りで与えられます。
# ・入力は合計で N + 1 行となり、末尾に改行が 1 つ入ります。
# ・じゃんけんの手は「グー」、「チョキ」、「パー」の 3 種類のみであり、それぞれ順番に 'G', 'C', 'P' というアルファベット 1 文字によって表現されます。

n = int(input())
alice = []
bob = []

for i in range(n):
    alice_hand, bob_hand = input().split()
    alice.append(alice_hand)
    bob.append(bob_hand)

alice_win = 0

for i in range(n):
    if alice[i] == 'G' and bob[i] == 'C':
        alice_win += 1
    elif alice[i] == 'C' and bob[i] == 'P':
        alice_win += 1
    elif alice[i] == 'P' and bob[i] == 'G':
        alice_win += 1

print(alice_win)

