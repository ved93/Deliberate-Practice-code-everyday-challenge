

# You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.

# You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).

# For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).
 
# https://leetcode.com/problems/random-pick-with-weight/
# https://leetcode.com/problems/random-pick-with-weight/discuss/671921/Python-3-simple-solution

# randin(1, 20):  returns random int between 1 and 20, includes both sides
# 1, 2, 3, 4, 5:  5 times out of 20,  will return index 0
# 6, 7, .... 15, 10 times out of 20,  will return index 1...

# https://leetcode.com/problems/random-pick-with-weight/discuss/671439/Python-Smart-O(1)-solution-with-detailed-explanation
# https://eli.thegreenplace.net/2010/01/22/weighted-random-generation-in-python
# https://leetcode.com/problems/random-pick-with-weight/discuss/671733/Python-sol-by-dice-roll-w-Visualization

import random

def pick_index(a):
    total_weight = sum(a)
    pick_num = random.randint(0, total_weight - 1)
    print(pick_num)
    for i in range(len(a)):
        if pick_num < a[i]:
            print(i)
            return i
        else:
            pick_num -= a[i]



print(pick_index([1,3, 8]))
# print(random.uniform(0,1))