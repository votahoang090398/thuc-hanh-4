import sys
giaodich = 0

s1=0
s2=0
D=input("tien gui vao:").split()
W=input("tien rut ra:").split()
for c in D:
    c=int(c)
    s1+=c
    pass
for b in W:
    b=int(b)
    s2+=b
    pass
    
giaodich=s1-s2
print("giao dich:",giaodich)

    
