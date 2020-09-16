#faulty calculator
#43 * 3 = 555 , 56+9 = 77 , 56/6 =4

sign = input("Select any one operator +,* ,/ :")
n1 = int(input("Enter first number :"))
n2 = int(input("Enter second number :"))

if n1==56 and n2==9 and sign=="+" or n1==9 and n2==56 and sign=="+":
    print("77")
elif n1==43 and n2==3 and sign=="*" or n1==3 and n2==43 and sign=="*":
    print("555")
elif n1==56 and n2==6 and sign=="/" or n1==6 and n2==56 and sign=="/":
    print("4")
elif sign=="+":
    print(n1+n2)
elif sign=="*":
    print(n1*n2)
elif sign=="/":
    print(n1/n2)
else:
    print("enter valid option")