class Solution:
	def findComplement(self, num):
		binary = bin(num)
		digit = 0
		answer = 0
		for bit in range(len(binary)-1, 1, -1):
			if (binary[bit] == '0'):
				answer = answer + 2**digit
			digit = digit + 1
		return answer
	
			
		
