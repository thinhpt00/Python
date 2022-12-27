if __name__ == '__main__':
    N = int(input())
    a = []
    for i in range(N):
        s,*x = list(input().split())
        y = list(map(int,x))
        if 'insert' in s:
            a.insert(y[0],y[1])
        elif 'print' in s:
            print(a)
        elif 'remove' in s:
            a.remove(y[0])
        elif 'append' in s:
            a.append(y[0])
        elif 'sort' in s:
            a.sort()
        elif 'pop' in s:
            a.pop()
        elif 'reverse' in s:
            a.reverse()