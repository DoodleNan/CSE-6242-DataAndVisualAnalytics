from util import entropy, information_gain, partition_classes
import random 

class DecisionTree(object):
    max_depth = 100
    def __init__(self):
        self.tree = {}

    def learn(self, X, y):
        # TODO: train decision tree and store it in self.tree
        self.tree = self.build_tree(X, y, 1)
    def build_tree(self, X, y, depth):
        # max_depth
        if depth >= self.max_depth:
            return self.majority(y)
        # all data are in the same categroy
        if y.count(y[0]) == len(y):
            return y[0]
        # leaf feature node
        if len(X[0]) <= 1:
            return self.majority(y)
        feature, value = self.selectSplitFeature(X, y)
        leftX, rightX, lefty, righty = self.splitData(X, y, feature, value)
        if len(leftX) == 0 or len(rightX) == 0:
            return self.majority(y)
        else:
            tree = {}
            tree[feature] = [value, self.build_tree(leftX, lefty, depth+1),
            self.build_tree(rightX, righty, depth+1)]
            return tree
    def classify(self, record):
        # TODO: return predicted label for a single record using self.tree
        current = self.tree
        while isinstance(current, dict):
            feature = list(current.keys())[0]
            if record[feature] <= current[feature][0]:
                current = current[feature][1]
            else:
                current = current[feature][2]
        return current

    def selectSplitFeature(self, X, y):
        infoGain = -1
        feature = -1
        value = -1
        # all features
        for index in range(len(X[0])):
            # all values of this feature
            splitFeatures = [X[i][index] for i in range(len(X))]
            for split_point in splitFeatures:
                left, right = partition_classes(splitFeatures, y, split_point)
                cur = []
                cur.append(left)
                cur.append(right)
                temp = information_gain(y, cur)
                # find max infoGain
                if temp > infoGain:
                    feature = index
                    value = split_point
                    infoGain = temp
        return feature, value

    def splitData(self, X, y, feature, value):
        leftX = []
        lefty = []
        rightX = []
        righty = []
        for i in range(len(X)):
            if X[i][feature] <= value:
                leftX.append(X[i])
                lefty.append(y[i])
            else:
                rightX.append(X[i])
                righty.append(y[i])
        left_reduce = []
        right_reduce = []
        for row in leftX:
            left_reduce.append(row[:feature] + row[feature + 1:])
        for row in rightX:
            right_reduce.append(row[:feature] + row[feature + 1:])
        return left_reduce, right_reduce, lefty, righty

    def majority(self, labels):
        count_0 = 0
        count_1 = 0
        for label in labels:
            if label == 0:
                count_0 += 1
            else:
                count_1 += 1
        if count_0 >= count_1:
            return 0
        else:
            return 1

    










