import numpy

__author__ = 'phizaz'

class DTW:

    @staticmethod
    def predict(training_with_label, instance):
        data = instance['data']

        min_dist = float('Inf')
        min_pos = -1

        for j, candidate in enumerate(training_with_label):
            dist = DTW.dist(data, candidate['data'])

            if dist < min_dist:
                min_dist = dist
                min_pos = j

        prediction = training_with_label[min_pos]['label']
        return prediction

    @staticmethod
    def predict_list(training_with_label, testing_with_label):

        correctness = 0
        for i, each in enumerate(testing_with_label):
            prediction = DTW.predict(training_with_label, each)

            if prediction == each['label']:
                correctness += 1

        accuracy = correctness / len(testing_with_label) * 100

        return accuracy, correctness

    @staticmethod
    def pair_dist(a, b):
        return (a - b) ** 2

    @staticmethod
    def euclid_dist(A, B):
        return sum([DTW.pair_dist(A[i], B[i]) for i in range(len(A))])

    @staticmethod
    def dist(A, B):
        return DTW.dist_adv(A, B, [1, 1, 1], [ [-1, 0], [0, -1], [-1, -1] ])

    @staticmethod
    def dist_adv(A, B, weights, directions):
        if len(weights) != len(directions):
            print('lengths are not equal')
            return

        shift_row = abs(min(map(lambda x: x[0], directions)))
        # print('shifted_row:', shift_row)
        shift_col = abs(min(map(lambda x: x[1], directions)))
        # print('shifted_col:', shift_col)

        lenA = len(A)
        lenB = len(B)

        INF = 100000000
        dp = [ [ INF for i in range(lenB + shift_col)] for i in range(lenA + shift_row)]

        for i in range(0, lenA):
            aa = i + shift_row
            a = A[i]
            for j in range(0, lenB):
                bb = j + shift_col
                b = B[j]

                pair_dist = DTW.pair_dist(a, b)

                if i == 0 and j == 0:
                    this = pair_dist
                else:
                    candidates = [pair_dist * weight + dp[aa + directions[k][0]][bb + directions[k][1]] for k, weight in enumerate(weights) ]
                    this = min(candidates)

                dp[aa][bb] = this

        return dp[lenA + shift_row - 1][lenB + shift_col - 1]