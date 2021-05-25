asciiCode = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

rot = ""

for s in input():
    if s.isalpha():
        if s.isupper():
            idx = asciiCode.index(s.lower())
            idx = (idx + 13)%26
            rot += asciiCode[idx].upper()
        else:
            idx = asciiCode.index(s)
            idx = (idx + 13)%26
            rot += asciiCode[idx]
    else:
        rot += s
        
print(rot)