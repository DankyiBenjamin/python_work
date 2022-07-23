T = int(input(" "))
num_of_T =1
while (num_of_T<= T):
    print("Case #%d:" % num_of_T, end=" ")
    num_of_T +=1
    N, M= input().split()
    N = int(N)
    M = int(M)
   
    C =list(map(int, input().split()))
    total = 0
# for loop to get total N
    for Ci in C:
        total +=Ci
        
    
    remainder = total % M
    print(remainder)