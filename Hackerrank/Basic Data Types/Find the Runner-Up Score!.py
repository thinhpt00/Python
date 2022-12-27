n = int(input())
arr = map(int, input().split())
s = list(arr)
s.sort()
x = [i for i in s if i != max(s)]
print(x[-1])