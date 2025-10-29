# 3. Power Function

# Problem:
# Compute a^b using recursion.

# Example:
# Input: a = 2, b = 5 → Output: 32
# Hint:
# Base case: if b == 0, return 1.
# Recursive case: return a * power(a, b - 1).

# Extra challenge: Try optimizing it with divide and conquer →
# power(a, b) = power(a, b/2)² (if b even), else a * power(a, b/2)².

class Solution:
    def powerFunction(a, b):
        if b <= 0:
            return 1
        else:
            return a * Solution.powerFunction(2, b -1)
        

if __name__ == "__main__":
    print(Solution.powerFunction(2, 5))