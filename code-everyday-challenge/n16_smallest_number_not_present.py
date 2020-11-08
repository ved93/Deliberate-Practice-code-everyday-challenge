
# codility interview quest

def get_smallest_positive_integer(number_list):
    if all(number < 0 for number in number_list) or 1 not in number_list:
        #checks if numbers in list are all negative integers or if 1 is not in list
        return 1
    else:
        try:
            #get the smallest number in missing integers
            number_list = sorted(number_list) # remove if list is already sorted by default
            return min(x for x in range(number_list[0], number_list[-1] + 1) if x not in number_list and x != 0)
        except:
            #if there is no missing number in list get largest number + 1
            return max(number_list) + 1


# print(get_smallest_positive_integer(number_list))



def solution(A):
    A = set(A)
    ans = 1
    while ans in A:
       ans += 1
    return ans







if __name__ == "__main__":
    # A = list(map(int,input().split()))
    A =  [-1,-3] #[1, 2, 3]
    print(solution(A))