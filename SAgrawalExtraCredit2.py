def largest_factor(n):
    i = 2
    while i * i < n:
         while n % i == 0:
             n = n/ i
         i = i + 1
    if (n > 1):
        return n
    return i     
         

print(largest_factor(600851475143))