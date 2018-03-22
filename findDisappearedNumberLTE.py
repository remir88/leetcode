class Solution:
    def findDisappearedNumbers(self, nums):
        answer = list(range(1, len(nums)+1))
        for num in nums:
            if (num in answer):
                answer.remove(num)
        return answer

