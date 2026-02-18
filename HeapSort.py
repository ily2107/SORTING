import sys
import time
import numpy as np
sys.stdin=open("input_1.inp","r")
sys.stdout=open("output.out","w")
n=int(input())
a=np.array(list(map(float,input().split())))
def heapify(a,n,idx):
    largest=idx
    l=2*idx+1
    r=2*idx+2
    if l<n and a[l]>a[largest]:
        largest=l
    if r<n and a[r]>a[largest]:
        largest=r
    if largest!=idx:
        a[idx],a[largest]=a[largest],a[idx]
        heapify(a,n,largest)
def heapsort(a):
    for i in range(n//2-1,-1,-1): 
        heapify(a,n,i)
    for i in range(n-1,0,-1):
        a[0],a[i]=a[i],a[0]
        heapify(a,i,0)
start=time.perf_counter()
heapsort(a)
end=time.perf_counter()
print(round((end-start)*1000,6))
