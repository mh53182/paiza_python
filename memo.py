# N個のデータを持つリストにQ回の操作
# 未解決

# N, Q = input().split(' ')
# n = int(N)
# q = int(Q)
# l = [int(x) for x in input().split(' ')]

# for i in range(q):
#     j = input()

# for i in range(q):
#     if i == 1:
#         l.pop()
#     elif i == 2:
#         print(l)
#     else:
#         t, u = i.split(' ')
#         l.append(u)


# 模範解答

# N, Q = map(int, input().split())
# A = [int(x) for x in input().split()]

# for _ in range(Q):
#     query = [int(x) for x in input().split()]

#     cmd = query[0]
#     if cmd == 0:
#         # push_back
#         A.append(query[1])
#     elif cmd == 1:
#         # pop_back
#         A.pop()
#     else:
#         # print
#         print(" ".join(map(str, A)))



# F文字列
word = "test"
print("これは", 1, "回目の", word, "です", sep="")  #通常の記述方法
print(f"これは{2}回目の{word}です")  # f文字列を使用した場合



# s = input()
# i, c = input().split()
# i = int(i)

# print(s[:i-1] + c + s[i:])

class Student:
    def __init__(self, name, old, birth, state):
        self.name = name
        self.old = old
        self.birth = birth
        self.state = state
    
    def __repr__(self):
        return f"{self.name} {self.old} {self.birth} {self.state}\n"

n = int(input())

roster = [None] * n
for i in range(n):
    name, old, birth, state = input().split()
    roster[i] = Student(name, old, birth, state)

roster.sort(key=lambda student: int(student.old))
print(roster)