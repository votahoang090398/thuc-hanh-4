ds=input("nhap danh sach:").split()
sochan=[]
sole=[]
for s in ds:
    s=int(s)
    if s%2==0:
        sochan.append(s)
    else:
        sole.append(s)
print("số chẵn",sochan)
print("số lẻ",sole)
