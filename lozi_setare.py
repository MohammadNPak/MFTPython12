n = int(input())
for i in range(n//2+1):
    print((n - (i*2+1))//2*" " + (i*2+1)*"*" + (n - (i*2+1))//2*" ")
