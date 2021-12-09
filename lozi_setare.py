n = int(input())
if n%2!=0:
    for i in range(n):
        if i < n//2+1:
            space = (n - (i*2+1))//2
            star = (i*2+1)
            print((space*" " + star*"*" + space*" ")*2)
        else:
            space = (i-n//2)
            star = (n-2*(i-n//2))
            print((space*" " + star*"*" + space*" ")*2)
