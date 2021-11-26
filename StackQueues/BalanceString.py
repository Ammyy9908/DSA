from Stack import Stack

def balance_string(string):

    s = Stack()
    for char in string:
        if char == '{' or char == '[' or char == '(':
            s.push(char)
        else:
            if s.isEmpty():
                return False
            else:
                top = s.pop()
                if (top == '{' and char != '}') or (top == '[' and char != ']') or (top == '(' and char != ')'):
                    return False
    return s.isEmpty()




print(balance_string('{[)]}'))