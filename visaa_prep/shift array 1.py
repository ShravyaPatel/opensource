N=int(input())
arr=list(map(int,input().strip().split()))
arr=arr[1:]+arr[0:1]
res=" ".join(map(str,arr))
print(res)
