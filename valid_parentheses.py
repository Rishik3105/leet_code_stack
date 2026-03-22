def isvalid(input_string):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in input_string:
        if char in mapping:  
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else: 
            stack.append(char)
    return len(stack) == 0

if __name__ == "__main__":
    input_string = input("Enter your sequence: ")
    print(isvalid(input_string))
