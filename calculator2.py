### make a calculater using for and if loop
print("calculater!!!....")
a =int(input("how many number you have to perfome the operation!!!..: "))
print("Pleace select the right choosie....")
c =input("A for add,B for mul,C for sub and D for div..")
sum =0
mul =1
sub =0
div =1
if c=='A' or c=='B' or c=='C'or c=='D':
    for i in range(1,a+1):
        b =int(input("enter a number.."))
        if c=='A':
            sum =sum+b
        elif c=='B':
            mul =mul*b
        elif c=='C':
            if sub==0:
                sub =b-sub
            else:
                sub=sub-b
        elif c=='D':
            if div==1:
                div =b/div
            else:   
                div =div/b
        else:
            print("not find any operation...")
    if c=='A':        
        print(sum)
    elif c=='B':
        print(mul)
    elif c=='C':
        print(sub)
    elif c=='D':
        print(div)
    else:
        print(" ")
    print("Done")
else:
    print("somthing want wrong!...")   
