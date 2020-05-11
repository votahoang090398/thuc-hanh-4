n=int(input("Nhập n="))

 

i=0

tong=0

s=0
while i<n:
    while s<=i:
        if s%i==0:

           tong +=i
        s+=1
        
    if tong>s:
        print(tong)


    
    i +=1

# Tổng


