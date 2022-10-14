command = str(input(">>>"))
if command == "add":
    num1 = int(input("Enter first number: - "))
    num2 = int(input("Enter second number: - "))
    sum = num1 + num2
    print("Your sum: - ", end=" ")
    print(sum)

if command == "subtract":
    num1 = int(input("Enter first number: - "))
    num2 = int(input("Enter second number: - "))
    difference = num1 - num2
    print("Your difference: - ", end=" ")
    print(difference)

if command == "multiply":
    num1 = int(input("Enter first number: - "))
    num2 = int(input("Enter second number: - "))
    product = num1 * num2
    print("Your product: - ", end=" ")
    print(product)

if command == "divide":
    num1 = int(input("Enter first number: - "))
    num2 = int(input("Enter second number: - "))
    quotient = num1 / num2
    print("Your quotient: - ", end=" ")
    print(quotient)
quit()
