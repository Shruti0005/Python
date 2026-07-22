#Check whether a number is a palindrome.
def palindrome(num):
    temp = num
    res = 0
    while num > 0:
        rem = num % 10
        res = res * 10 + rem
        num //= 10
    return "Palindrome" if temp == res else "Not Palindrome"

number = int(input("Enter number: "))
print(palindrome(number))
