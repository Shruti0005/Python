#Check whether a number is prime.
def prime(num):
    if num == 1:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    return True    
              
number = int(input("Give number to check prime: "))
result = prime(number)

if result:
    print("Prime")
else:
    print("Not Prime")
