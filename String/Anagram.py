def isAnagram(a,b):
    a_length= len(a)
    b_length = len(b)

    if a_length!=b_length:
        return False
    res1 = ''.join(sorted(a))
    res2 = ''.join(sorted(b))
    if res1==res2:
        return True
    return False

print(isAnagram("tac","act"))