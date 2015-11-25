import numpy

__author__ = 'phizaz'

class DTW:

    @staticmethod
    def pair_dist(a, b):
        return (a - b) ** 2

    @staticmethod
    def euclid_dist(A, B):
        return sum([DTW.pair_dist(A[i], B[i]) for i in range(len(A))])

    @staticmethod
    def dist(A, B):
        lenA = len(A)
        lenB = len(B)
        dp = [ [ float('Inf') for i in range(0, lenB + 1)] for i in range(0, lenA + 1)]

        for i in range(0, lenA):
            iA = i + 1
            a = A[i]
            for j in range(0, lenB):
                iB = j + 1
                b = B[j]

                pair_dist = DTW.pair_dist(a, b)

                if i == 0 and j == 0:
                    this = pair_dist
                else:
                    this = pair_dist + min(
                        dp[iA - 1][iB],
                        dp[iA][iB - 1],
                        dp[iA - 1][iB - 1]
                    )

                dp[iA][iB] = this

        return dp[lenA][lenB]