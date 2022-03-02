def printNumber(s):

    #CODE HERE
    '''alpha = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
    d={}
    n=""

    for i in range(len(alpha)):
        if i==5 or i==7:
            d[alpha[i][0]]=i+2
            d[alpha[i][1]]=i+2
            d[alpha[i][2]]=i+2
            d[alpha[i][3]]=i+2
        else:
            d[alpha[i][0]]=i+2
            d[alpha[i][1]]=i+2
            d[alpha[i][2]]=i+2

    #print(d)
    for i in s:
        n+=str(d[i.upper()])
    print(n)'''
    n=""
    print(len(s))
    for i in range(0,len(s)):
        print(i)
        print(s[i],end=" ")
        if s[i]=='a' or s[i]=='b' or s[i]=='c':
                n+='2';
        elif s[i]=='d' or s[i] =='e' or s[i]=='f':
                print("**")
                n+='3';
        elif s[i]=='g' or s[i]=='h' or s[i]=='i':
                n=n+'4';
        elif s[i]=='j' or s[i]=='k' or s[i]=='l':
                n+='5';
        elif s[i]=='m' or s[i]=='n'  or s[i]=='o':
                n+='6';
        elif s[i]=='p' or s[i]=='q' or s[i]=='r' or s[i]=='s':
                n+='7';
        elif s[i]=='t' or s[i]=='u' or  s[i]=='v':
                n+='8';
        elif s[i]=='w' or s[i]=='x' or s[i]=='y' or s[i]=='z':
                n+='9';
        return n

print(printNumber("geeks"))