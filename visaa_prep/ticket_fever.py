T=int(input())
for _ in range(T):
    N,M=map(int,input().split())

    if N>M:
        res=N-M
    if N<=M:
        res=0
    
    print(res)
