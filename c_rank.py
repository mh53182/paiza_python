"""
アリスさんはじゃんけんが大好きで、過去に何度も友達のボブさんとじゃんけんを行いました。
手元には、アリスさんとボブさんとの間で、過去に行われたじゃんけんの結果を全て記録したノートがあります。

ノートの記録を元に、過去にアリスさんはボブさんに何回勝ったかを出力するプログラムを作成してください。

・1 行で過去に行われたじゃんけんの回数を表す整数 N が与えられます。
・続く N 行のうちの i 行目 (1 ≦ i ≦ N) には、(i 回目のじゃんけんにおいてアリスさんが出した手)、
    (i 回目のじゃんけんにおいてボブさんが出した手) を表す文字列 A_i, B_i がこの順で半角スペース区切りで与えられます。
・入力は合計で N + 1 行となり、末尾に改行が 1 つ入ります。
・じゃんけんの手は「グー」、「チョキ」、「パー」の 3 種類のみであり、それぞれ順番に 'G', 'C', 'P' というアルファベット 1 文字によって表現されます。
"""

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

print('###########################')

"""
あなたは自分のウェブサイトでプレゼント企画を実施しました。
プレゼントには A と B の二種類があります。

当選者は以下の条件に従って、選出されます。

・整数 X の倍数番目の応募者はプレゼント A の当選者とする
・整数 Y の倍数番目の応募者はプレゼント B の当選者とする

応募者の数が与えられるので、各応募者のプレゼント当選情報を出力してください。
プレゼント A と B の両方当選した人は AB、A だけ当選した人は A、B だけ当選した人は B、どちらも当選してない人は N を出力してください。

入力例 1 の場合、応募者の人数は 5 人なので、5 人の当選情報を出力します。
プレゼント A の当選者は、2 の倍数番目の応募者で、プレゼント B の当選者は 4 の倍数の当選者なので、
2 番目の応募者は A、4 番目の応募者は AB となり、それ以外の応募者は N になります。

1 行目にはそれぞれ整数 N, X, Y がこの順で半角スペース区切りで与えられます。
これらは応募者が N 人であることを示し、X の倍数番目の応募者がプレゼント A の当選者となり、Y の倍数番目の応募者がプレゼント B の当選者となることを示します。
"""

N, X, Y = map(int, input().split())

for i in range(1, N+1):
    # print(i)
    if i % X == 0 and i % Y == 0:
        print('AB')
    elif i % X != 0 and i % Y == 0:
        print('B')
    elif i % X == 0 and i % Y != 0:
        print('A')
    else:
        print('N')

print('#####################')

"""
# あなたは、高速道路の管理運営を仕事にしています。
# そこで、運転者に道路がどの程度渋滞しているかを知らせるシステムを作ることにしました。

# ある道路の車の数と、各車の車間距離が与えられるので、車間距離が M メートル以下の場合を渋滞と定義したとき、
# 渋滞の区間が合計で何メートルあるか求めるプログラムを作成してください。なお、車の車体の長さは無視して計算してください。

# ・1 行目には、車の数を表す整数 N と、渋滞を定義する整数 M がこの順で半角スペース区切りで与えられます。
# ・続く N - 1 行目の i 行目 (1 ≦ i ≦ N - 1) には、先頭から i 番目の車と i + 1 番目の車の車間距離を表す整数 A_i が与えられます。
# ・入力は合計で N 行となり、入力値最終行の末尾に改行が 1 つ入ります。
"""

n, m = map(int, input().split())

A = []
for i in range(n-1):
    a = int(input())
    A.append(a)

sum = 0

for j in range(len(A)):
    if A[j] <= m:
        sum += A[j]

print(sum)

print('############')

"""
クラスの学級委員である paiza 君は、クラスのみんなに次のような形式でアカウントの情報を送ってもらうよう依頼しました。

名前 年齢 誕生日 出身地

送ってもらったデータを使いやすいように整理したいと思った paiza 君はクラス全員分のデータを次の形式でまとめることにしました。

User{
nickname : 名前
old : 年齢
birth : 誕生日
state : 出身地
}

クラスメートの情報が与えられるので、それらを以上の形式でまとめたものを出力してください。
"""
# 提出版
n = int(input())

class_mate = {}

for i in range(n):
    info = input().split()
    class_mate[i] = info

for i in class_mate:
    print('User{')
    print('nickname :', class_mate[i][0])
    print('old :', class_mate[i][1])
    print('birth :', class_mate[i][2])
    print('state :', class_mate[i][3])
    print('}')

# 模範回答
N = int(input())

for _ in range(N):
    n, o, b, s = input().split()

    print("User{")
    print("nickname : " + n)
    print("old : " + o)
    print("birth : " + b)
    print("state : " + s)
    print("}")

print('##############')

"""
クラスの学級委員である paiza 君は、クラスのみんなに次のような形式でアカウントの情報を送ってもらうよう依頼しました。

名前 年齢 誕生日 出身地

送ってもらったデータを使いやすいように整理したいと思った paiza 君はクラス全員分のデータを次のような構造体でまとめることにしました。

student{
    name : 名前
    old : 年齢
    birth : 誕生日
    state : 出身地
}

年齢ごとの生徒の名簿を作る仕事を任された paiza 君はクラスメイトのうち、決まった年齢の生徒を取り出したいと考えました。
取り出したい生徒の年齢が与えられるので、その年齢の生徒の名前を出力してください。
"""
# 提出版
n = int(input())

class_mate = {}

for i in range(n):
    info = input().split()
    class_mate[i] = info

k = int(input())

for i in class_mate:
    if int(class_mate[i][1]) == k:
        print(class_mate[i][0])

# 模範回答　※いっそややこしい
# 解説はこちら ↓
# （https://paiza.jp/works/mondai/reviews/show/5eb7dc9a4117b4e51de97919f1ce1109）

class Student:
    def __init__(self, name, old, birth, state):
        self.name = name
        self.old = old
        self.birth = birth
        self.state = state

n = int(input())

roster = [None] * n
for i in range(n):
    name, old, birth, state = input().split()
    roster[i] = Student(name, old, birth, state)

k = input()
for student in roster:
    if student.old == k:
        print(student.name)
        break


print('##############')

"""
クラスの学級委員である paiza 君は、クラスのみんなに次のような形式でアカウントの情報を送ってもらうよう依頼しました。

名前 年齢 誕生日 出身地

送ってもらったデータを使いやすいように整理したいと思った paiza 君はクラス全員分のデータを次の形式でまとめることにしました。

User{
    nickname : 名前
    old : 年齢
    birth : 誕生日
    state : 出身地
}

この情報を扱いやすくするために、年齢が昇順になるようにデータを並び替えることにしました。
クラスメートの情報が与えられるので、並び替えた後のデータを出力してください。

"""
# 提出版
class Student:
    def __init__(self, name, old, birth, state):
        self.name = name
        self.old = old
        self.birth = birth
        self.state = state
    
    # リスト内容のプリント時にオブジェクトのメモリアドレスではなくリストの中身を表示させる
    def __repr__(self):
        return f"{self.name} {self.old} {self.birth} {self.state}"

n = int(input())

roster = [None] * n
for i in range(n):
    name, old, birth, state = input().split()
    roster[i] = Student(name, old, birth, state)

roster.sort(key=lambda student: int(student.old))

for i in range(len(roster)):
    print(roster[i])


# 解答例 1 (ソートを自分で書く)
class Student:
    def __init__(self, name, old, birth, state):
        self.name = name
        self.old = old
        self.birth = birth
        self.state = state

n = int(input())

roster = [None] * n
for i in range(n):
    name, old, birth, state = input().split()
    roster[i] = Student(name, old, birth, state)

# ソートする
# n回ループ
for i in range(n):
    # iの次のインデックスからループ
    for j in range(i+1, n):
        # あるインデックス[i]とその次のインデックスの年齢を比較
        # あるインデックスの方が次のインデックスより年齢が大きければ
        if roster[i].old > roster[j].old:
            # 順序を入れ替える
            roster[i], roster[j] = roster[j], roster[i]

for student in roster:
    print(student.name, student.old, student.birth, student.state)


# 解答例 2 (ソートを自分で書かない)
class Student:
    def __init__(self, name, old, birth, state):
        self.name = name
        self.old = old
        self.birth = birth
        self.state = state

n = int(input())

roster = [None] * n
for i in range(n):
    name, old, birth, state = input().split()
    # 後のソートのためoldをintで受ける
    roster[i] = Student(name, int(old), birth, state)

# ソート済リストを新たに作成
    
sorted_by_old = sorted(roster, key=lambda x: x.old)

for student in sorted_by_old:
    print(student.name, student.old, student.birth, student.state)
