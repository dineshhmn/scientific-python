import math

def fact(n):
    if n == 0 or n == 1:
        return n
    elif n < 0:
        sign = n % 2
        if sign:
            n1 = -1 * n
            return (math.pow(-1,sign)*(n1*fact(n1-1)))
        else:
            sign = 2
            n1 = -1 * n
            return (math.pow(-1,sign) * (n1*fact(n1-1)))
    else:
        return n * fact(n-1)

def fibn(n):
    if n < 2:
        return n
    else:
        ctr,a,b = 1,1,1
        while ctr < n:
            a,b = b,a + b
            ctr+=1
    return x

def fibb_rec(n):
    if n < 2:
        return n
    else:
        return fibb_rec(n-1) + fibb_rec(n-2)

if __name__ == "__main__":
    # print(fact(10))
    # print(fact(-10))
    # print(fact(0))
    # print(fact(1))
    # print(fact(2))
    # print(fact(11))
    # print(fact(-11))
    print(fibn(5))
    print(fibb_rec(6))

