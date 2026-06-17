
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multi(a,b):
    return a*b

def division(a,b):
    if(b == 0):
        return "Division by Zero is not Possible"
    else:
        return a/b

print("=== CALCULATOR ===")

a = float(input("Enter First Number:"))
b = float(input("Enter Second Number:"))

print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
c = int(input("Choose any operation(1/2/3/4):"))
if c>4:
    print("Invalid Operation ")


match c:
    case "1":
        print("Result:",add(a,b))
    case "2":
        print("Result:",sub(a,b))
    case "3":
        print("Result:",multi(a,b))
    case "4":
        print("Result:",division(a,b))
        




