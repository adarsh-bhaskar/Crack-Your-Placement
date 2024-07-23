# Leetcode 12

def intToRoman(num: int) -> str:
    isValid = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    map = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }
    ans = []

    def helper(num , res):
        nonlocal map

        for i in range(len(isValid)):
            if num in isValid:
                res = map[num]
                remainder = 0
                break
            if isValid[i] < num:
                quotient = num // isValid[i]
                remainder = num % isValid[i]
                res = res + map[isValid[i]] * quotient
                break
        
        ans.append(res)
        if remainder == 0:
            pass
        else:
            helper(remainder, "")
    
    helper(num, "")
    return "".join(ans)

num = 3749
print(intToRoman(num))