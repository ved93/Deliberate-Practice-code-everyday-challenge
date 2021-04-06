# How do you print duplicate characters from a string?

from collections import defaultdict

def main(s):
    d=defaultdict(int)

    for c in s:
        if c in d:
            print(c)
        d[c] = d[c] + 1








if __name__ == "__main__":
    s= 'edhbhvehdbejdnasddwde'
    print(main(s))