# https://practice.geeksforgeeks.org/problems/implement-atoi/1/?track=md-string&batchId=144#

# https://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-is-a-number-float


def atoi(self,string):
    # Code here
    res = 0
    try:
        
        return int(string)
    except Exception as e:
        pass
        
    
    
    if string.isnumeric() is False:
    
        if any(char.isdigit() for char in string):
            return -1
    else:
        return int(string)
    
    
    # Iterate through all characters of
    #  input string and update result
    for i in range(len(string)):
        res = res * 10 + (ord(string[i]) - ord('0'))
    
    return res




if  __name__ == "__main__":
    s= '21a'
    # s= '123'
    s = 'asdd'
    s = '-12'

    print(int(s))