def find_first(haystack, needle):

    if needle == "":
        return 0

    for i in range(len(haystack) + 1 - len(needle)):
        for j in range(len(needle)):
            if haystack[i+j] != needle[j]:
                break
            if j == len(needle) - 1:
                return i
    return -1


haystack = "sadbutsad"
needle = "sad"

print("\nOutput is: ")
print(find_first(haystack, needle))