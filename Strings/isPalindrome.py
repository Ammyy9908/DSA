def isPalindrome(string):
    print(string[::-1] == string)
    return 1 if string == string[::-1] else 0



isPalindrome('hq')