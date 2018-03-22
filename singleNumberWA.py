class Solution:
    def singleNumber(self, nums):
        answer = 0
        for num in nums:
            answer += num
        answer -= len(nums)*(len(nums)-1) // 2
        return answer

