# 1. Factorial of a Number

# Problem:
# Given a number n, find its factorial using recursion.
# Factorial is defined as
# n! = n × (n-1) × (n-2) × … × 1, with 0! = 1.

# Example:
# Input: 5 → Output: 120
# Hint:
# Base case: when n == 0, return 1.
# Recursive case: return n * factorial(n - 1).

class Solution:
    def factorial(n):
        if n == 0:
            return 1
        return n * Solution.factorial(n - 1)
    
if __name__ == "__main__":
    print(Solution.factorial(492))
