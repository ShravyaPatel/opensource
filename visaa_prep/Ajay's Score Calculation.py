T=int(input())
for i in range(T):
    X,N=map(int,input().split())

    each_case_points=X/10

    total_points=N*each_case_points
    print(int((total_points)))
