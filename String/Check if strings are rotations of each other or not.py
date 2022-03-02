def areRotations(s1,s2):
    #code here
    if (len(s1) != len(s2)):
        return 0

    q1 = []
    for i in range(len(s1)):
        q1.insert(0, s1[i])

    q2 = []
    for i in range(len(s2)):
        q2.insert(0, s2[i])

    k = len(s2)
    while (k > 0):
        ch = q2[0]
        q2.pop(0)
        q2.append(ch)
        if (q2 == q1):
            return True

        k -= 1

    return False
print(areRotations("dylsebxjwlmpamjneoehhlgayxtgs","lsebxjwlmpamjneoehhlgayxfgsdy"))