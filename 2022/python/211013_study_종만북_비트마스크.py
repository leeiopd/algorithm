# 비트마스크

##############################################

# 공집합
zero = 0
print(bin(zero))
# '0b0'


##############################################

# 꽉 찬 집합 ( 20 bit )
full = (1 << 20) - 1
print(bin(full))
# '0b11111111111111111111'
# '0b100000000000000000000'(21bit) 에서 1을 뺀 2진수 20bit 전체가 1인 2진수


##############################################

# 원소의 포함 여부 확인
# python 은 2진수가 str 형으로 표현됨

a = 1 << 19
# '0b10000000000000000000'
b = 1 << 5
# '0b100000'

if(a & b):
    print('YES')
else:
    print('No')
# No


##############################################

# 원소의 삭제

a = int('0b11111', 2)
b = int('0b00100', 2)

c = a & ~b
print(bin(c))
# '0b11011'
# b 의 원소 삭제


##############################################

# 원소의 토글

a = int('0b11011', 2)
b = int('0b00100', 2)

a ^= b
print(bin(a))
# a = '0b11111'

a ^= b
print(bin(a))
# a = '0b11011'


##############################################

# 최소 원소 지우기

a = int('0b100100100', 2)

b = a - 1
print(bin(b))
# a = '0b100100100'
# b = '0b100100011'
# b 는 켜져있는 최 하위 bit 를 끄고 그 밑의 bit 를 전부 켠 것

c = a & b
print(bin(c))
# c = '0b100100000'


##############################################

# 모든 부분집합 순회하기
origin = int('0b1101', 2)
subset = origin

while True:
    subset = (subset - 1) & origin

    if subset == 0:
        break

    print(bin(subset))
    # 0b1100 -> 1100
    # 0b1001 -> 1001
    # 0b1000 -> 1000
    # 0b101  -> 0101
    # 0b100  -> 0100
    # 0b1    -> 0001
