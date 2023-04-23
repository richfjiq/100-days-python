#Write your code below this line 👇
def prime_checker(number):
    is_prime = True

    # if (number <= 1):
    #     is_prime = False
    # else:
    #     for n in range(1, number + 1):
    #         if n == 1 and number % n == 0:
    #             is_prime = True
    #         elif n != 1 and n != number and number % n == 0:
    #             is_prime = False
    #             break
    #         elif n == number and number % n == 0:
    #             is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
