def swap_case(s):
    ss = []
    for i in range(len(s)):
        if s[i] > 'A' and s[i] < 'Z':
            ss.append(s[i].lower())
        elif s[i] > 'a' and s[i] < 'z':
            ss.append(s[i].upper())
        else:
            ss.append(s[i])
    return ''.join(ss)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)