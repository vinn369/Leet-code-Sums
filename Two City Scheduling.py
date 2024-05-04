class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x:x[0]-x[1])
        total_c=0
        n=len(costs)//2
        for i in range(n):
            total_c+=costs[i][0]
        for i in range(n,len(costs)):
            total_c+=costs[i][1]
        return total_c
