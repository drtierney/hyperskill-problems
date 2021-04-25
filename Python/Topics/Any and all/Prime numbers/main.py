prime_numbers = [num for num in range(2, 1000) if all(num % i != 0 for i in range(2, num - 1))]
