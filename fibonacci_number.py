# 5. Fibonacci Number

# Problem:
# Find the nth Fibonacci number using recursion.
# Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, ...

# Example:
# Input: n = 6 → Output: 8

# Hint:
# Base case:

# if n == 0 → return 0

# if n == 1 → return 1
# Recursive case: return fib(n-1) + fib(n-2).
class Solution:
    def fibonacci(self, n):
        # Base cases
        if n == 0:
            return 0
        elif n == 1:
            return 1
        # Recursive case
        else:
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)


if __name__ == "__main__":
    sol = Solution()
    n = 6
    print(sol.fibonacci(n))  # Output: 8
