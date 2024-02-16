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

# A, B = map(int, input().split())
# N = 10000
# N = N / A
# N = N % B
# print(N)


s = input()

list = [str(x) for x in s]

for i in range(len(list)-1, 0, -1):
    if list[i] == "-" and list[i - 1] == "-":
        # ここでremoveは引数に一致するデータをリストから削除するのでpopを使う
        list.pop(i)

print(''.join(list))