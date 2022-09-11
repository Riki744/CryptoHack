chall = 'label'

flag = []
for c in chall:
    flag.append(chr(ord(c)^13))

    
print(*flag, sep="")
