def isPalindrome(text):
    length=len(text)
    for i in range(0,length//2):
        if(text[i] != text[length-i-1]):
            return False
    return True

text=input("Enter string:")

if(isPalindrome(text)):
    print(text, "is Palindrome.")
else:
    print(text, "is NOT Palindrome.")