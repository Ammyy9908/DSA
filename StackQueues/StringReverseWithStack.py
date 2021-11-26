from Stack import Stack

def reverseStringWithStack(string):
    stack = Stack()
    reversed = ""
    for char in string:
        stack.push(char)
    while not stack.isEmpty():
        reversed += stack.pop()
    return reversed


if __name__ == "__main__":
    print(reverseStringWithStack("Sumit"))
