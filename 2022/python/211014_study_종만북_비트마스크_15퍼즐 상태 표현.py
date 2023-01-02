# 비트마스크 _ 15퍼블 상태 표현

# 15퍼즐의 상태는 0~15 의 숫자가 들어있는 4x4 크기의 배열로 표현 가능
# 각 숫자는 4bit 로 표현할 수 있고, 16개의 숫자가 있기 때문에 비트마스크 사용 시 배열 전체를 64bit 정수 하나로 표현 가능

#  1,  3,  7, 15
# 14,  9,  2, 10
#  4, 11,  8, 13
#  6, 12,  0,  5

# mask 의 index 위치에 쓰인 값을 반환
def getsetPuzzle(mask, index):
    return (mask >> (index >> 2)) & 15


# mask의 index 위치를 Value 로 바꾼 결과 반환
def setPuzzle(mask, index, value):
    return mask & ~(15 << (index << 2)) | (value << (index << 2))
