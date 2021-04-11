

# https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/

# https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/?currentPage=1&orderBy=most_votes&query=&tag=python




def longest_substring(s):
    # create a window with left and right
    # keep a hash of elements already added
    left = 0
    right = 0
    seen = {} # keeps track of seen elements

    max_count = 0

    for i, character in enumerate(s):
        if character not in seen or seen[character] < left: # notice this logic
            seen[character] = i
            right = i
            if (right - left + 1) > max_count: # update the largest count
                max_count = (right - left + 1)
        else:
            # we move start to one element after we found the character
            left = seen[character] + 1
            seen[character] = i # update index of last time we saw the character

    return max_count

            
def longest_substring_new(s):
    used = {}
    max_length = start = 0
    for i, c in enumerate(s):
        if c in used and start <= used[c]:
            start = used[c] + 1
        else:
            max_length = max(max_length, i - start + 1)
            
        used[c] = i

    
    return max_length
    



if __name__ == "__main__":
    s= 'azcbobobegghakl'
    print(longest_substring_new(s))