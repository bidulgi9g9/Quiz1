N = list(input() for _ in range(9))
a = int(max(N))
print(a)
print(N.index(a) + 1)