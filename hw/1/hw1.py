import numpy as np

class Num:
    def __init__(self):
        self.n, self.mean, self.m2 = 0, 0, 0
        self.lo, self.hi = 10 ^ 32, -1 * 10 ^ 32

    def __mean__(self):
        return self.mean

    def __std__(self):
        return 0 if self.n<2 else (np.sqrt(self.m2/(self.n-1)))

    def __add__(self, other):
        if other < self.lo:
            self.lo = other
        if other > self.hi:
            self.hi = other
        self.n += 1
        diff = other - self.mean
        self.mean += diff/self.n
        self.m2 += diff*(other - self.mean)

    def __sub__(self,other):
        if self.n < 2:
            self.n, self.mean, self.m2 = 0, 0, 0
        else:
            self.n -= 1
            diff = other - self.mean
            self.mean -= diff / self.n
            self.m2 -= diff * (other - self.mean)

# class Sym:
#
# class Some:


def main():
    rand01 = np.random.randint(low=1, high=200, size=100)
    result = Num()
    meanlist01,meanlist02 = [], []
    sdlist01,sdlist02 = [], []
    for x in range(0,100):
        Num.__add__(result, rand01[x])
        if (x+1)%10 == 0:
            meanlist01.append(np.round(result.mean, 2))
            sdlist01.append(np.round(Num.__std__(result), 2))

    rand02 = rand01[::-1]
    meanlist02.append(np.round(result.mean,2))
    sdlist02.append(np.round(Num.__std__(result),2))
    for x in range(0,100):
        Num.__sub__(result, rand02[x])
        if (x+1) % 10 == 0 and x != 99:
            meanlist02.append(np.round(result.mean,2))
            sdlist02.append(np.round(Num.__std__(result),2))
    print("Generating random integers......")
    print(rand01)
    # print(rand02)
    print("1st time mean: ",meanlist01)
    print("1st time sd: ",sdlist01)
    print("2nd time mean: ",meanlist02[::-1])
    print("2nd time sd: ",sdlist02[::-1])

if __name__ == "__main__":
    main()
