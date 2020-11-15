

# https://www.lintcode.com/problem/maximum-possible-value/note/227991
# https://github.com/jiadaizhao/LintCode
# https://leetcode.com/discuss/interview-question/576522/microsoft-interview-question 




from collections import Counter


def solution(S):
    if len(list(Counter(S).keys())) <= 1:
        return True

    for i in S:
        if i =='b':
            if 'a' in S[i:]:
                return False


    return True





print(solution('abba'))