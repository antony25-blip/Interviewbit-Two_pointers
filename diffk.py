class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        i=0
        j=1
        while i<len(A)-1 and j<len(A) and i!=j:
            if A[j]-A[i]==B:
                return 1
            elif A[j]-A[i]<B:
                j+=1
            else:
                i+=1
                if i==j:
                    j+=1          
        return 0
