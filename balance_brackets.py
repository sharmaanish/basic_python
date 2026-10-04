def balance_brackets(chs):
    pairs = {
        ')' : '(',
        ']' : '[',
        '}' : '{'
    }

    stack = []
    for c in chs:
        if c in '([{' :
            stack.append(c)

        elif c in ')]}':
            if len(stack) == 0 or stack[-1] != pairs[c]:
                return False

            stack.pop()
    
    if len(stack) ==0:
        return True

# Examples
print(balance_brackets("()[]{}"))   # True
print(balance_brackets("([{}])"))   # True
print(balance_brackets("([)]"))     # False
print(balance_brackets("((("))      # False