import sys
import time
import numpy as np
sys.stdin=open("input_1.inp","r")
sys.stdout=open("output.out","w")
n=int(input())
a=np.array(list(map(float,input().split())))
b=[0]*n
def combine(a,l,mid,r):
    i,j=l,mid+1
    k=0
    while i<=mid and j<=r:
        if a[i]<a[j]: 
            tmp=a[i]
            i+=1
        else: 
            tmp=a[j]
            j+=1
        b[k]=tmp
        k+=1
    while i<=mid: 
        b[k]=a[i]
        k+=1
        i+=1
    while j<=r: 
        b[k]=a[j]
        k+=1
        j+=1
    for i in range(k): 
        a[l+i]=b[i]
def mergesort(a,l,r):
    if l>=r: 
        return
    mid=(l+r)//2
    mergesort(a,l,mid)
    mergesort(a,mid+1,r)
    combine(a,l,mid,r)
start=time.perf_counter()
mergesort(a,0,n-1)
end=time.perf_counter()
print(round((end-start)*1000,6))
