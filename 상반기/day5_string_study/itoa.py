def itoa(x):
    strs = ''
    while True:
        i = x % 10
        x = x // 10
        strs = (chr(i + ord('0'))) + strs

        if x == 0:
            return strs








x = 123
print(x, type(x))

str1 = itoa(x)
print(str1, type(str1))