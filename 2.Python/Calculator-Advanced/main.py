def calc(s):
    plus_ind = s.rfind('+')
    minus_ind = s.rfind('-')

    if plus_ind > minus_ind:
        return calc(s[:plus_ind]) + calc(s[plus_ind+1:])
    if minus_ind != -1:
        if minus_ind == 0: 
            return -calc(s[1:])
        return calc(s[:minus_ind]) - calc(s[minus_ind+1:])

    mul_idx = s.rfind('*')
    div_idx = s.rfind('/')

    if mul_idx > div_idx:
        return calc(s[:mul_idx]) * calc(s[mul_idx+1:])
    if div_idx != -1:
        return calc(s[:div_idx]) / calc(s[div_idx+1:])

    return float(s)

expression = input("Enter expression: ")
print("Result:", calc(expression))