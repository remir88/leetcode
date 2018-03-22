class Solution:
    def findDisappearedNumbers(self, nums):
        isExist = [False] * (len(nums)+1)
        for i in nums:
            isExist[i] = True
        answer = []
        for i in range(1, len(nums)+1):
            if (not isExist[i]):
                answer.append(i)
        return answer

                
