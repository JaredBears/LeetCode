# Given a string s containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    openSet = ['(', '{', '[']

    stack = []

    for c in s:
        if c in openSet:
            stack.append(c)
        elif len(stack) == 0:
            return False
        else:
            prev = stack.pop()
            valid = (c == ")") and (prev == "(")
            valid = valid or ((c == "}") and (prev == "{"))
            valid = valid or ((c == "]") and (prev == "["))
            if not valid:
                return False
    if len(stack) > 0:
        return False
    return True

print(isValid("()") == True)
print(isValid("()[]{}") == True)
print(isValid("(]") == False)
print(isValid("(({[]}))") == True)
print(isValid("(({)})") == False)
print(isValid("]") == False)
