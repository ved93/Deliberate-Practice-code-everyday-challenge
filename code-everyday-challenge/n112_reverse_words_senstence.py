

def reverse_words(s):
    print(s)
    if len(s) <= 1:
        return s[0]

        
    return s[-1]+' ' +reverse_words(s[:-1]) +' ' 




if __name__ == "__main__":
    s = "main esa kyun hun"
    s= s.split()
    tmp = []
    print(reverse_words(s))