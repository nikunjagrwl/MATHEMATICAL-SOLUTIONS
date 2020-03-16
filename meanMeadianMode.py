import collections
n=int(input())
x=list(map(int,input().strip().split()))[:n] 
def avg(n,x):
    sum=0
    for i in range(n):
        sum+=x[i]
    return sum/n     

def med(n,x):
    x.sort()
    if n%2==0:
        a=int(n/2)
        b=int(n/2-1)
        med=(x[a]+x[b])/2
    else:
        med=x[(int((n+1)/2))-1]    
    return med

def mode(n,x):
    data = collections.Counter(x)
    data_list = dict(data)
    max_value = max(list(data.values()))
    mode_val = [num for num, freq in data_list.items() if freq == max_value]
    if len(mode_val) == len(x):
     print(min(x))
    else:
     print(min(mode_val))



      
a=avg(n,x)    
dfg=med(n,x)

print(a)
print(dfg) 
mode(n,x)
