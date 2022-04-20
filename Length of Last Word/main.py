def lenoflastword(s):
    l_s=s.split()
    length=len(l_s)
    return len(l_s[length-1])
s = input("Enter: ")
print(lenoflastword(s))