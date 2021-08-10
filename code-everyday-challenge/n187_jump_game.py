

# https://leetcode.com/problems/jump-game/discuss/1179976/Straightforward-Python-DP-(Accepted)-and-Recursive-and-Mem.-(TLE)-Solns.-with-Explanation!

# https://leetcode.com/problems/jump-game/discuss/516529/My-Python-TLE-solution-using-recursion-7275-passed.

#https://stackoverflow.com/questions/60565076/jump-game-in-recursion

# https://practice.geeksforgeeks.org/problems/jump-game/1/?track=md-arrays&batchId=144#

def reach_end(nums):

    m=0
    for j in range(len(nums)-1,-1,-1):
        if nums[j]>=m:
            print(j ,'value  ',nums[j], '   ',m)
            m=1
        else:
            m+=1
    if m==1:
        return True
    return False


def canJump( nums):
	"""
	:type nums: List[int]
	:rtype: bool
	"""

	if not nums: return False
	first = nums[0]

	if first == 0 and len(nums) == 1:return True
	for x in range(first, 0, -1):
		if x >= len(nums):
			return True
		ans = canJump(nums[x:])
		if ans:
			return ans
		else:
			continue

	return False



if  __name__ == "__main__":
    a = [1, 2, 2, 0, 3, 0]
    # a =  [1, 0, 2]
    # a = [1,0]
    # a = [12,14,8,32,23,3,25,14,22,3,4,14,3,27,1,0,17,10,16,6,20,9,28,22,8,27,4,2,7,11,10,9,0,10,20,11,5,3,18,22,32,28,1,2,12,23,1,17,1,29,11,2,11,15,7,8,8,2,2,9,14,13,8,27,0,31,25,9,13,13,21,7,14,14,23,6,28,6,6,8,12,17,2,12,7,18,23,10,24,14,1,30,28,24,22,29,7,22,23]
    # print(reach_end(a))
    print(canJump(a))