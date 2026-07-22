#Find the factorial of a given number (e.g., 5! = 120).
def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i
    return fact

number = int(input("Enter number: "))
print(f"Factorial: {factorial(number)}")
