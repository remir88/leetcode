class Solution:
	def judgeCircle(self, moves):
		x = 0
		y = 0
		for letter in moves:
			if (letter == 'U'):
				y = y + 1
			elif (letter == 'D'):
				y = y - 1
			elif (letter == 'L'):
				x = x - 1
			elif (letter == 'R'):
				x = x + 1
		answer = (x==0 and y==0)
		return(answer)
		
