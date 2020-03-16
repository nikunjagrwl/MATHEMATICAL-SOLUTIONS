n=int(input())
x=list(map(int,input().strip().split()))[:n]

def sd(n,x):
    sum1=sum2=0
    for i in range(n):
        sum1+=x[i]
    mean=sum1/n
    for i in range(n):
        sum2+=((x[i]-mean)**2)
    a=(sum2/n)**0.5
    return a
print(sd(n,x))