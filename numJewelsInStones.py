class Solution:
	def numJewelsInStones(self, J, S):
		totalJewels = 0
		jewels = {}
		for letter in J:
			jewels[letter] = 1
		for letter in S:
			if (letter in jewels):
				totalJewels = totalJewels + 1
		return(totalJewels)

				
