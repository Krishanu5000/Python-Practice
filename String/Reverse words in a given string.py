def reverseWords(S):
    # code here
    n=S.split(".")
    k=""
    for i in range(len(n)-1,-1,-1):
        k= k + n[i] + "."
    return k[0:len(k)-1]

print(reverseWords("i.like.this.program.very.much"))