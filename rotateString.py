class Solution:
	def rotateString(self, A, B):
		if (len(A) != len(B)):
			return False

		rotate = B
		for i in range(1, len(A)):
			if (A == rotate):
				return True
			rotate = rotate[1:] + rotate[0]

		return False

