n = int(input())
for i in range(n):
    if i < n//2+1:
        space = (n - (i*2+1))//2
        star = (i*2+1)

        print(space*" " + star*"*" + space*" ")
    else:
        space = (i-n//2)
        star = (i*2+1)
        print(space*" " + star*"*" + space*" ")
