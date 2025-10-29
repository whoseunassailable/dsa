# 🟢 4. Print Numbers 1 to n and n to 1

# Problem:
# Print numbers from 1 to n and from n to 1 using recursion.

# Example:
# Input: n = 5
# Output (1 to n): 1 2 3 4 5
# Output (n to 1): 5 4 3 2 1

# Hint:
# For 1 → n: print before recursive call.
# For n → 1: print after recursive call.

class Solution:
    def print1ToN(n, starting_int):
        if starting_int > n:
            return ""
        else:
            return f"{starting_int} {Solution.print1ToN(n, starting_int + 1)}"
    
    def printNTo1(n):
        if n == 0:
            return ""
        else:
            return f"{n} {Solution.printNTo1(n - 1)}"
        
if __name__ == "__main__":
    print(Solution.print1ToN(5, 1))
    print(Solution.printNTo1(5))