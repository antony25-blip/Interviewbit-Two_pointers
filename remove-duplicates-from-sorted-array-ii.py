class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        i=1
        for j in range(2,len(A)):
            if A[j]!=A[i-1]:
                i+=1
                A[i]=A[j]
        return i+1
