class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        c=set()
        for i in A:
            if (i - B) in c or (i + B) in c:
                return 1
            c.add(i)
        return 0
