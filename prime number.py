lower=int(input("Enter lower range: "))
upper=int(input("Enter upper range: "))
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
# The above code is a simple program to find prime numbers in a given range. It takes two inputs from the user: the lower and upper range. It then iterates through each number in that range and checks if it is prime by dividing it by all numbers less than itself. If it finds a divisor, it breaks out of the loop; otherwise, it prints the number as prime.
# The code is efficient and works well for small ranges, but it can be optimized further for larger ranges by using the Sieve of Eratosthenes algorithm or other advanced techniques.