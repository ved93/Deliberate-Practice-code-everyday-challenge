
import sys

def main(a):
    s= 0
    for i in range(len(a)):
        mn = a[i]
        s+=mn
        for j in range(i+1,len(a)):
            if a[j] < mn:
                mn = a[j]
            s+=mn
    print(s)


if __name__ == '__main__':
    print(main([3,1,2,3]))