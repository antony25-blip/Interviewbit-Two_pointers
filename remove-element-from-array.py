class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        S=[]
        for i in range(len(A)):
            if A[i]!=B:
                S.append(A[i])
        for i in range(len(S)):
            A[i]=S[i]
        return len(S)
