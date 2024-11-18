N,m=map(int,input().split())
arr=list(map(int,input().split()))
div=[]
not_div=[]
for i in range(N):
    if arr[i]%m != 0:
        not_div.append(arr[i])
    if arr[i]%m == 0:
        div.append(arr[i])
sum_div=sum(div)
sum_not_div=sum(not_div)
print(sum_div-sum_not_div)
