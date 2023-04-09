A = "abccbaa"

stack = []
for c in A:
        if stack and c == stack[-1]:
            stack.pop()
        else:
            stack.append(c)
print(stack)


