S=input()
new_S=""
count=1
for i in range(1,len(S)):
    if S[i]==S[i-1]:
        count+=1
    else:
        new_S+=S[i-1]+str(count)
        count=1
new_S+=S[-1]+str(count)
print(new_S)
