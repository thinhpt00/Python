if __name__ == '__main__':
    s = input()
    print (True in [a.isalnum() for a in s])
    print (True in [a.isalpha() for a in s])
    print (True in [a.isdigit() for a in s])
    print (True in [a.islower() for a in s])
    print (True in [a.isupper() for a in s])
    
    # 'IN' operator 
    #Returns True if a sequence with the specified value is present in the object