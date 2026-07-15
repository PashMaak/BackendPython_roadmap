l, r = 0, 101
while r-l > 1:
    m = (l + r) >> 1
    flag = (input(f"Is your number greater or equal than {m}? (1:yes | 0:no) "))

    if (flag == "1"):
        l = m
    else:
        r = m
print("Your number is: ", (l+r) >> 1)