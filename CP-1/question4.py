# 4. Climbing Stairs
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Example 1:
# Input: n = 2
# Output: 2
# Example 2:
# Input: n = 3
# Output: 3
# Constraints:
# 1 <= n <= 45

def climbStairs(n: int) -> int:
    if n <= 2:
        return n
    prev1, prev2 = 2, 1 
    for _ in range(3, n + 1):
        prev1, prev2 = prev1 + prev2, prev1
    return prev1

print(climbStairs(3)) #3 