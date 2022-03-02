import re
def search(p,s):
    M = len(p)
    N = len(s)
    # A loop to slide pat[] one by one */
    for i in range(N - M + 1):
        j = 0
        # For current index i, check
        # for pattern match */
        while(j < M):
            if (s[i + j] != p[j]):
                break
            j += 1
        if (j == M):
            return True
    return False
print(search("aaba","aabaacaadaabaaabaaa"))