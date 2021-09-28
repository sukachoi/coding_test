import sys

sys.stdin=open("input.txt", "rt")
n=int(input())
print(n)
num_list = list(map(int, input().split()))
print(num_list)
dic={}
a=[0]*(n+1)
for i in num_list:
    sum=0   
    for j in str(i):
        sum+=int(j)  
    dic[i]=sum
    a.append(sum)
    #a.insert(i, sum)
    

    

print(max(dic.values()))
print(max(dic, key=dic.get))
print("{}".format(max(dic,key=dic.get)))
#[k for k,v in di.items() if max(di.values()) == v]최대값 모두 출력
#리스트컴프리헨션


def digit_sum(x):
    sum=0
    while x>0:
        sum+=x%10
        x=x//10
    return sum
"""
"""다른 코드
def digit_sum(x):
    sum=0
    for j in str(x):
            sum+=int(j) 
        return sum

"""
"""
max=-2147000000
for x in num_list:
    dig_s=digit_sum(x)
    if dig_s>max:
        max=dig_s
        result=x 
print(result)        
    




