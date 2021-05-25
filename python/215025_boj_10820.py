import sys

while 1:
    string = sys.stdin.readline().rstrip('\n')
    if not string:
        break
        
    upper = lower = decimal = blank = 0
    
    for s in string:
        if s == " ":
            blank += 1
        elif s.isdecimal():
            decimal += 1
        else:
            if s.isupper():
                upper+=1
            else:
                lower+=1
    
    print(lower, upper, decimal, blank)