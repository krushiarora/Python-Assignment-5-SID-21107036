n=int(input("Enter the no. of rows:"))
a=0
for i in range(n):
    for j in range(i+1):
        print(chr(65+a),end="")
        a+=1
    print()
        
    
