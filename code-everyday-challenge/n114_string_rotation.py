
# https://www.geeksforgeeks.org/a-program-to-check-if-strings-are-rotations-of-each-other/


def are_rotations(s1, s2):
    size1 = len(s1)
    size2 = len(s2)

    tmp = ''

    if size1 != size2:
        return 0


    tmp = s1+s2

        # Now check if str2 is a substring of temp
    # string.count returns the number of occurrences of
    # the second string in temp

    if tmp.count(s2) > 0:
        return 1
    else:
        return 0



if __name__ == "__main__":
    s1 = 'AACD'
    s2= 'ACDA'

    print(are_rotations(s1, s2))

