m1 =int(input("enter subject 1 marks:"))
m2= int(input('enter subject 2 marks:'))
m3= int(input("enter subject 3 marks:"))
avg=(m1+m2+m3)/3
if avg>=80:
    grade="A"
elif avg>=70:
    grade="B"
else:
    grade="F"
print("avg:",avg)
print("grade:",grade)