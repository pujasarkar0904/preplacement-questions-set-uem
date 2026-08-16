n=int(input("enter a num: "))
temp=n
sum=0
reverse = 0
while temp>0:
        digit = temp%10
        sum = sum +digit
        reverse=reverse*10+digit
        temp = temp//10
print("sum:",sum)
print("reverse:",reverse)