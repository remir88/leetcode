class Solution:
	def hammingDistance(self, x, y):
		xor = x ^ y
		answer = 0
		while (xor >= 1):
			if (xor % 2 == 1):
				answer = answer + 1
			xor = xor // 2
		return answer
		
			
