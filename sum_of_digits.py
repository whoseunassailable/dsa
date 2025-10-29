# 2. Sum of Digits

# Problem:
# Find the sum of digits of a number using recursion.

# Example:
# Input: 1234 → Output: 10 (1+2+3+4)

# Hint:
# Base case: when n == 0, return 0.
# Recursive case: return (n % 10) + sumOfDigits(n / 10).

class Solution:
    def sumOfDigits(n):
        if n == 0 : 
            return 0
        else :
            return int(n % 10) + Solution.sumOfDigits(n // 10)

if __name__ == "__main__":
    print(Solution.sumOfDigits(3425))