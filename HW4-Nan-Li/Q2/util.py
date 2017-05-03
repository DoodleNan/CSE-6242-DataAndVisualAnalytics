from scipy import stats
import numpy as np
import math

# This method computes entropy for information gain
def entropy(class_y):
    """Compute the entropy for a list of classes

    Example:
        entropy([0,0,0,1,1,1,1,1,1]) = 0.92
    """
    # TODO: Implement this
    zero = 0
    one = 0
    for label in class_y:
        if label == 0:
            zero = zero + 1
        if label == 1:
            one = one + 1
    # zero = class_y['0'].count
    # one = class_y['1'].count
    pzero = float(zero) / len(class_y)
    pone = float(one) / len(class_y)
    if pone == 1 or pzero == 1:
        return 0
    else:
        return -(pzero * math.log(pzero, 2) + pone * math.log(pone, 2))


def partition_classes(x, y, split_point):
    """Partition the class vector, y, by the split point. 

    Return a list of two lists where the first list contains the labels 
    corresponding to the attribute values less than or equal to split point
    and the second list contains the labels corresponding to the attribute 
    values greater than split point

    Example:
    x = [2,4,6,7,3,7,9]
    y = [1,1,1,0,1,0,0]
    split_point = 5

    output = [[1,1,1], [1,0,0,0]]
    """ 
    # TODO: Implement this
    left = []
    right = []
    for i in range(len(x)):
        if x[i] <= split_point:
            left.append(y[i])
        if x[i] > split_point:
            right.append(y[i])
    return left, right
    
def information_gain(previous_y, current_y):
    """Compute the information gain from partitioning the previous_classes
    into the current_classes.

    Example:
    previous_classes = [0,0,0,1,1,1]
    current_classes = [[0,0], [1,1,1,0]]

    Information gain = 0.45915
    Input:
    -----
        previous_classes: the distribution of original labels (0's and 1's)
        current_classes: the distribution of labels given a particular attr
    """
    # TODO: Implement this
    pre = entropy(previous_y)
    cur = 0
    for row in current_y:
        if len(row) > 0:
            cur = cur + float(len(row))/len(previous_y) * entropy(row)
    return pre - cur






















