
N= [120,230,450,774,1400]
I= [140,0,413,890,1300]
C= [110,200,0,670,1180]
j=int(input("Enter the units:"))
v=int(input("Enter number of hours:"))
x=j*v
print("{",'"Output":',"[",sep="\n")
def dis(f,x,c):
    y=[]
    r=[]
    s=0
    l=[10,20,40,80,160]
    z=["Large","XLarge","2XLarge","4XLarge","8XLarge"]
    print("{",'"region":',sep="\n",end="")
    print('"',c,'",',sep="")
    for i in range(len(l)-1,-1,-1):
        if(l[i]<=x and f[i]!=0):
            t=(x//l[i])
            x=x%l[i]
            s=s+t*f[i]
            y.append(t)
            r.append(z[i])
    print('"total_cost":','"$',s,'",',sep="")
    print('"machines":[')
    for i in range(len(y)):
           print("(",r[i],",",y[i],")",sep="")
    print("]","},",sep="\n")

dis(N,x,"New York")
dis(I,x,"India")
dis(C,x,"China")
