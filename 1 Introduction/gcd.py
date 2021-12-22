# Find the greatest common denominator of two numbers
# using Euclid's algorithm

def gcd(a, b):
    while (b != 0):
        r = a % b
        a = b
        b = r

    return a

#try out a set of numbers
print(gcd(60, 96))
print(gcd(20, 8))
