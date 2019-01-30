def atoi(string):
    value = 0
    i = 0
    while (i < len(string)):
        c = string[i]
        if c >= '0' and c <= '9':       # 문자열 이지만 아스키코드의 대소가 있다.
            digit = ord(c) - ord('0')   # ord() - 아스키코드로 바꾸기, 아스키 코드의 차이로 0~9까지 정수 구하기
        else:
            break
        value = (value * 10) + digit;
        i += 1
    return value

a = "123"
print(type(a))
b = atoi(a)
print(type(b))
c = int(a)
print(type(c))