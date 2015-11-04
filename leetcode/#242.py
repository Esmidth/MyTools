__author__ = 'Esmidth'

def isAnagram(s,t):
    return sorted(s)==sorted(t)

print(isAnagram("anagram","nagaram"))
