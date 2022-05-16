a = int(input())
b = list(input() for _ in range(a))
c = set(b)
for i in c:
    print(i)