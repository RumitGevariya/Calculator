#make a calculater

a =int(input("Enter a frist nu: "))
b =int(input("Enter a second nu: "))
choise =int(input("please select a 1 for a add and 2 for a sub 3 for a mul and 4 for a div "))
if choise==1:
    add =a+b
    print("result: ",add)
elif choise==2:
    sub =a-b
    print("result: ",sub)
elif choise==3:
    mul =a*b
    print("result: ",mul)
elif choise==4:
    div =a/b
    print("result: ",div)
else:
    print("plese select a right option")
