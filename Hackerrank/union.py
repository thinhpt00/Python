n = int(input())
E = set(map(int,input().split()))
b = int(input())
F = set(map(int,input().split()))

s = E | F  # s = E.union(F)
print(len(s))
