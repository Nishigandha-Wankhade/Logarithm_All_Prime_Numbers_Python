"""
-----------------------------------------------------------------------
Sum of logarithms of all Prime numbers between 2 and n.
September 25, 2024 
Nishigandha Wankhade 
-----------------------------------------------------------------------
"""
import math

# function to find number is prime number or not
def prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

# function to Sum logarithm of prime numbers
def log_sum_prime(num):
    sum = 0 
    count = 0
    temp = 2   # first prime number
    while temp < num + 1:
       
        if prime(temp):
            sum += math.log(temp)
            count +=1
        temp += 1

    # Calculate the ratio of sum to number
    ratio = sum / num

    print(f"\n\n\t\t Total sum of logarithms of prime numbers between 2 and {num}= {int(sum)} ") #math.ceil() can used to roundup the sum into interger
    print(f"\n\n\t\t Ratio of the sum of logs / {num} = {ratio}")
    print(f"\n\n\t\t Number of Primes found = {count}")

            
    
# calling function log_sum_prime()
ans = 'y'
while ans == 'y' or ans == 'Y':
    num = int(input("\n\t\t Enter any number [500, 5000, 50000, etc]:"))
    log_sum_prime(num)

    ans = input("\n\t\t Do you want to continue [y / n]?\t")
