# Two strings str1 and str2 are called isomorphic if there is a one-to-one mapping possible for every character of str1 to every character of str2. And all occurrences of every character in ‘str1’ map to the same character in ‘str2’.
#
# Examples:
#
# Input:  str1 = “aab”, str2 = “xxy”
# Output: True
# Explanation: ‘a’ is mapped to ‘x’ and ‘b’ is mapped to ‘y’.
#
# Input:  str1 = “aab”, str2 = “xyz”
# Output: False
def isoMorphic(str1,str2):

    char=26

    c1=[0]*char
    c2=[0]*char

    for i in range(len(str1)):
        c1[ord(str1[i])-ord('a')] += 1
        c2[ord(str2[i]) - ord('a')] += 1



    for i in range(len(str2)):
        print(c1[ord(str1[i]) - ord('a')], c2[ord(str2[i]) - ord('a')])
        if c1[ord(str1[i])-ord('a')]!=c2[ord(str2[i])-ord('a')]:
            return False
    return True

print(isoMorphic("aab", "xyx"))