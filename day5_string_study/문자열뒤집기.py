words = input()

def my_strrev(words):
    long = int(len(words) // 2)
    re_words = list(words)
    for i in range(long):
        re_words[i], re_words[-i-1] = words[-i-1], words[i]
    return ''.join(re_words)

print(my_strrev(words))

#--------------------------------
s = "Reverse this strings"
s = s[::-1]
print(s)