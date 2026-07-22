#Calculate the sum of digits of a number.
def sum_digit(num):
    total = 0
    while num > 0:
        rem = num % 10
        total += rem
        num //= 10
    return total

number = int(input("Enter number: "))
print(f"Summation of digit: {sum_digit(number)}")
