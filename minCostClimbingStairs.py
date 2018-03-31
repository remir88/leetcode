class Solution:
    def min(a, b):
        if (a<b):
            return a
        else:
            return b

    def minCostClimbingStairs(self, cost):
        n = len(cost)
        f = [0] * n
        f[0] = cost[0]
        if (n >= 1):
            f[1] = cost[1]
        for i in range(2, n):
            f[i] = cost[i] + min(f[i-1], f[i-2])
        answer = f[n-1]
        if (n >= 1):
            answer = min(f[n-1], f[n-2])
        return answer
        

