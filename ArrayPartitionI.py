class Solution:
	def arrayPairSum(self, nums):
		sortednums = nums
		sortednums.sort()
		answer = 0
		for i in range(0, len(sortednums), 2):
			answer = answer + sortednums[i]
		return answer
	
