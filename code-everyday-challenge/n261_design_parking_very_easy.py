

# https://leetcode.com/problems/design-parking-system/
# https://leetcode.com/problems/design-parking-system/discuss/876927/C%2B%2B-Python-Explained-oror-Easy-Understanding-oror

# https://leetcode.com/problems/design-parking-system/discuss/1128843/Python-fast-and-efficient-(97)
# https://leetcode.com/problems/design-parking-system/discuss/955808/Simple-and-fast-solution-(96.55)


class ParkingSystem():
    __slots__ = ['space']

    def __init__(self, big,medium, small):
        self.space= {
            1 : 'big',
            2 : 'medium',
            3 : 'small'
        }

    def addCar(self, carType):
        if self.space[carType] > 0:
            self.space[carType] -= 1

            return True
        else:
            return False