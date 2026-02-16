class Solution:
    # @param A : list of integers
    # @param B : list of integers
    def merge(self, A, B):
        i=0
        j=0
        k=0
        s=[]
        while i<len(A)and j<len(B):
            if A[i]>B[j]:
                s.append(B[j])
                j+=1
            else:
                s.append(A[i])
                i+=1
        if i<len(A):
            while i<len(A):
                s.append(A[i])
                i+=1
        elif j<len(B):
            while j<len(B):
                s.append(B[j])
                j+=1
        A[:]=s[:]
