A = [1,2,0,3,4,0,7,0]
n = len(A)
B = [0]*n
j = 0

count = 0
for i in range(n):
    if A[i]!=0:
        B[j]=A[i]
        j += 1
    else:
        count += 1


while count>0:
    B[j] = 0
    count = count-1
    j = j+1

for i in range(n):
    A[i]=B[i]

for i in range(n):
    print(A[i],end=" ")        
