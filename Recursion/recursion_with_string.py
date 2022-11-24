def reverse_string(string):
    if len(string) == 0:
        return string
    if len(string) == 1:
        return string
    if len(string) > 2:
        string = string[::-1]
    return string



string = "helloworld"
print(reverse_string(string))