K = int(input())
rooms = list(input().split())
a = set()
b = set()
for i in rooms :
    if i not in a:
        a.add(i)
        b.add(i)
    else :
        b.discard(i)
b=list(b)
print(b[0])