# Calculator Using python

print("enter first number")
a=int(input())
print("enter second number")
b=int(input())
print("enter your choise to calculate like :+ - * /")
c=input()

if a==45 and b==3 and c == '*':
  print("555")
elif a==56 and b==9 and c=='+':
  print("77")
elif a==56 and b==6 and c=='/':
  print("4")
elif a>0 and b>0 and c=='+':
    print(a+b)
elif a>0 and b>0 and c=='-':
    print(a-b)
elif a>0 and b>0 and c=='*':
    print(a*b)
elif a>0 and b>0 and c=='/':
    print(a/b)
else :
    print("enter valid choise")
