A = "{[}]"

stack = []
for ch in A:
    if ch == "{" or ch == "[" or ch == "(" or len(stack) == 0:
        stack.append(ch)
    else:
        if ch == "}" and stack[-1] == "{":
            stack.pop()

        if ch == "]" and stack[-1] == "[":
            stack.pop()

        if ch == ")" and stack[-1] == "(":
            stack.pop()

if len(stack) != 0:
    print(0)
else:
    print(1)










