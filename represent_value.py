import sys
sys.stdin=open("input.txt", "r")

n =int(input())
a=list(map(int, input().split()))
avg=round(sum(a)/n)
print(avg)
min=21700000
for idx, x in enumerate(a):
    temp=abs(x-avg)
    if temp < min:
        min = temp
        score=x
        idx+=1
    elif temp==min:
        if x > score:
            score = x
            idx+=1


print(avg, idx)


