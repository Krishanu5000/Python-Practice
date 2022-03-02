'''Given a string check if it is Pangram or not.
A pangram is a sentence containing every letter in the English Alphabet.'''

def checkPangram(s):
    #code here
    a="abcdefghijklmnopqrstuvwxyz"
    s1=s.lower()
    for i in a:
        if s1.find(i)==-1:
            return False
    return True

print(checkPangram("Bawds jog, flick quartz, vex nymph"))