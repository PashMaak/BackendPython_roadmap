# Uses bin search to find a number O(log(100))
# the left bound is 0 and right bound is 101
# and for the implementation i used half-interval [l, r) for easy math

l, r = 0, 101
while r - l > 1:
    m = (l + r) >> 1

    try:
        flag = int(input(f"Is your number greater or equal than {m}? (1:yes | 0:no) "))

        if flag not in (0, 1):
            raise ValueError("Please enter 0 or 1.")

    except ValueError as e:
        print(e)
        continue

    if flag == 1:
        l = m
    else:
        r = m

print("Your number is:", (l + r) >> 1)