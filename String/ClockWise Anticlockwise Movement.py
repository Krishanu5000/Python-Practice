def clockwiseAnticlockwisemvmnt(s):
    #s1=s.replace("?","A")
    #s2=s.replace("?","C")
    #print(s1)
    #print(s2)
    a_cnt=0
    c_cnt=0
    for i in range(len(s)):
        if s[i]=="A" or s[i]=="?":
            a_cnt+=1
    print(a_cnt)
    print(s)
    for j in range(0,len(s)):
        if s[j]=="C" or s[j]=="?":
            c_cnt+=1
    print(c_cnt)
    print(max(a_cnt,c_cnt))
print(clockwiseAnticlockwisemvmnt("????"))