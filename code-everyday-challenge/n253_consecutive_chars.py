

def get_longest_consecutive_chars(string):
    """
    Given a string, return the longest consecutive character sequence.
    """
    longest_consecutive_chars = ''
    current_consecutive_chars = ''

    for char in string:
        if char not in current_consecutive_chars:
            current_consecutive_chars += char
        else:
            current_consecutive_chars = char

        if len(current_consecutive_chars) > len(longest_consecutive_chars):
            longest_consecutive_chars = current_consecutive_chars

    return longest_consecutive_chars


def main(s):
    max_so_far  = 0
    prev = None
    c = 1
    for char in s:
        curr = char
        if curr== prev:
            c +=1
        else:
            c = 1
        prev = curr
        max_so_far = max(max_so_far, c)
    return max_so_far





if  __name__ == "__main__":
    s = "abbcccddddeeeeedcba"
    # s = 'leetcode'
    print(main(s))