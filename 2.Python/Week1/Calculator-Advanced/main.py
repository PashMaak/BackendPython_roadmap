# Thought normal cal would be too easy so implemented more fun version
# in takes an mathematical expresison and calculates its output
# main idea is in recursion the answer of a+b is know only of we know answer of a and b 
# where a,b or left and right part of expression acordingly
# Since it is a recursion we can add priory of the mathematic operations by simply writing it in reverse order
# Hence we process +,- first and *,/ last by recursion it would firstly calculate *,/ then +,-

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

try:
    expression = input("Enter expression: ")
    print("Result:", calc(expression))
except ValueError:
    raise ValueError("Incorectr Mathematical expression")