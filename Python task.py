#calculator
a=float(input("Enter the frst number: "))
b=float(input("Enter the second number: "))
operator=input("Enter the operator: ")
if operator == "+":
    result=a+b
elif operator == "-":
    result=a-b
elif operator == "*":
    result=a*b
elif operator == "/":
    result=a/b
elif operator == "**":
    result=a**b
elif operator == "%":
    result=a%b
else:
    print("invalid")

print(f"Result: {result}")

