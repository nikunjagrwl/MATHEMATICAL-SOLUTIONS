n=int(input())
x=list(map(int,input().strip().split()))[:n]
x1=x2=[]

def med(n,x):
    x.sort()
    if n%2==0:
        a=int(n/2)
        b=int(n/2-1)
        med=(x[a]+x[b])/2
    else:
        med=x[(int((n+1)/2))-1]    
    return med

def quartiles(n,x):
    x.sort()
    if n%2==1:
        q2=med(n,x)
        q1=med(n//2,x[:n//2])
        q3=med(n//2,x[(n//2+1):n])
    else:
        q2=med(n,x)
        q1=med(n//2,x[:n//2])
        q3=med(n//2,x[(n//2):n])

    if (q1-(q1//1))==0.0:
        print(int(q1))
        
    else:
         print(q1)
     
    if (q2-(q2//1))==0.0:  
        print(int(q2))   
    else:
         print(q2)


    if (q3-(q3//1))==0.0:  
        print(int(q3))   
    else:
         print(q3) 

    

        
        
quartiles(n,x)     
