class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        count0=0
        count1=0
        count2=0
        i=0
        j=0
        k=0
        l=len(A)
        for i in range(len(A)):
            if A[i]==0:
                count0+=1
            elif A[i]==1:
                count1+=1
            elif A[i]==2:
                count2+=1

        for j in range(count0):
            A[k]=0
            k+=1
        for j in range(count1):
            A[k]=1
            k+=1
        for j in range(count2):
            A[k]=2
            k+=1
        return A
Time taken: 76 min.
Score:
179
/
325
Python (python-2.7)
123456789101112131415161718192021222324252627282930
class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        count0=0
        count1=0
        count2=0
        i=0
        j=0
        k=0
…            A[k]=0
            k+=1
        for j in range(count1):
            A[k]=1
            k+=1
        for j in range(count2):
            A[k]=2
            k+=1
        return A

All Problems
167/749
