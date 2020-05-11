Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = input("Nhập câu của bạn: ")

d={"DIGITS":0, "LETTERS":0}
for c in s:
 if c.isdigit():#đếm số chữ số
 d["DIGITS"]+=1
 elif c.isalpha():#đếm số chữ cái
 d["LETTERS"]+=1
 else:
 pass
print ("Số chữ cái là:", d["LETTERS"])
print ("Số chữ số là:", d["DIGITS"])