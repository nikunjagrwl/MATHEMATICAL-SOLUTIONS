n=int(input())
x=list(map(int,input().strip().split()))[:n]
w=list(map(int,input().strip().split()))[:n]

def weighted_mean(n,x,w):
    summ=sum=0
    for i in range(n):
        summ+=w[i]
        sum+=(x[i]*w[i])
    return round((sum/summ),1)    
print(weighted_mean(n,x,w))