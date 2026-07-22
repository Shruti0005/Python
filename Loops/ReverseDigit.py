#Reverse an integer (e.g., 12345 → 54321).
def reverse(num):
    res = 0
    while num > 0:
        rem = num % 10
        res = res * 10 + rem
        num //= 10
    return res

number = int(input("Enter number: "))
print(f"Reverse number: {reverse(number)}")
