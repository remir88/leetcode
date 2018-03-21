class Solution:
	def isOneRow(self, word):
		rows = ["qwertyuiop","asdfghjkl","zxcvbnm"]
		for row in rows:
			flag = True
			for digit in word:
				if (digit not in row):
					flag = False
					break
			if (flag):
				return True
		return False	

	def findWords(self, words):
		answer = []
		for word in words:
			if (self.isOneRow(word.lower())):
				answer.append(word)
		return answer

