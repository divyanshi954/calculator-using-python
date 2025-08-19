print("\t CALCULATOR")
choice = int(input("\t ENTER 1 FOR ADDITION\n\t ENTER 2 FOR SUBTRACTION\n\t ENTER 3 FOR MULTIPLICATION\n\t ENTER 4 FOR DIVISION\n\t ENTER 5 FOR MODULUS\n"))
x = int(input("enter number 1 : "))
y = int(input("enter number 2 : "))

def calculate(a,b):
    if choice == 1:
        result = a+b
        return result
    elif choice == 2:
        result = a-b
        return result
    elif choice == 3:
        result = a*b
        return result
    elif choice == 4:
        result = a/b
        return result
    elif choice == 5:
        result = a%b
        return result

    else:
            #print("you have entered wrong choice")
            #result = None
        return("you have entered wrong choice")
    

answer = calculate(x,y)
print("the final answer is :", answer)     