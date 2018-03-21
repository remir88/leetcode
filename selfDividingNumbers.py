class Solution:
	def selfDividingNumbers(self, left, right):
		answer = []
		for numbers in range(left, right+1):
			number = numbers
			fit = True
			while (number != 0):
				bit = number % 10
				number = number // 10
				if ((bit==0) or (numbers%bit!=0)):
					fit = False
					break
			if (fit):
				answer.append(numbers)
		return answer

		
