def palindrome(s):
    i=0
    j=len(s)-1
    while i<j:
        while i<j and not s[i].isalnum():
            i+= 1
        while i<j and not s[j].isalnum():
            j-=1
        if s[i].lower() != s[j].lower():
            return False
        i,j=i+1, j-1
    return True
print(palindrome("race a car"))
print(palindrome("yash"))
print(palindrome("madam"))
print(palindrome("honest"))
print(palindrome("A man,a plan,a canal:Panama"))
