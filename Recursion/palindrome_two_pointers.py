def isPalindrome(word):
    l, r = 0, len(word) - 1

    while l < r and r > l:
        if word[l] == word[r]:
            l+=1
            r-=1
        else:
            return False
    return True


word = ""
print(isPalindrome(word))