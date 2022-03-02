def concatenatedString(s1,s2):
    #code here
    k=s1+s2
    s1_len=len(s1)
    s2_len=len(s2)
    n1=""
    n2=""
    for i in s1:
        if s2.find(i)==-1:
            n1+=i
    for i in s2:
        if s1.find(i)==-1:
            n2+=i
    if n1+n2=="":
        return -1
    return n1+n2
print(concatenatedString("abcs","cxzca"))