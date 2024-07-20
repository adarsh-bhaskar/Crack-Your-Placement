# Leetcode 20

def isValid(s: str) -> bool:
    if len(s) < 2:
        return False
    
    # Initalize a stack and start appending entry parenthesis
    stack = []

    for i in s:
        if i in ['(', '{', '[']:
            stack.append(i)
        else:
            if not len(stack):
                return False
            
            if stack:
                bracket = stack.pop()
                # Check if you can match each and every parenthesis with every bracket
                if bracket == '(' and i != ')':
                    return False
                if bracket == '{' and i != '}':
                    return False
                if bracket == '[' and i != ']':
                    return False
            # If not found matching pairs at all then return False
            else: return False

    if stack:
        return False
    else:
        return True
        
s = "()"
print(isValid(s))