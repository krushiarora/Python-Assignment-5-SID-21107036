n = 5


k = ord('A')

for i in range(n):
    for j in range(i+1):
        print(chr(k),end='')
        k+=1
    print()     