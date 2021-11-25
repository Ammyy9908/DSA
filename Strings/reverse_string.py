def reverse_string(string):
    string_list = []
    string_list[:0] = string
    start = 0
    end = len(string) - 1
    revered = ""
    while start < end:
        string_list[start], string_list[end] = string_list[end], string_list[start]
        start += 1
        end -= 1
    
    for i in string_list:
        revered += i
    return revered

original = "Hello World"
print("Original string:", original)
reversed = reverse_string(original)
print("Reversed string:", reversed)