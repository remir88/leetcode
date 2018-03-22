class Solution:
    def countBits(self, num):
        answer = [0] * (num+1)
        i = 1
        j = 1 
        while (i <= num):
            answer[i] = 1
            k = j * 2
            while ((j<=num) and (j<k)):
                answer[j] = answer[i]+answer[j-i]
                j += 1
            i = k 
        return answer

        
