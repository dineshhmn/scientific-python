import time
from numpy import random as rd

def sorter_bubble_iter(x):
    n = len(x)
    if n == 0:
        return None
    elif n == 1:
        return x
    else:
        while n > 0:
            for i in range(1,n):
                if int(x[i-1]) >= int(x[i]):
                    x[i-1], x[i] = x[i], x[i-1]
            n-=1
        return x

def sel_sort(x):
    n = len(x)
    if n == 0:
        return None
    elif n == 1:
        return x
    else:
        for i in range(n):
            low = 0
            for j in range(1,n):
                if int(x[j-1]) <= int(x[j]):
                    low = j
            x[n-1], x[low] = x[low], x[n-1]
        return x

def ins_sort(x):
    n = len(x)
    if n == 0:
        return None
    elif n == 1:
        return x
    else:
        for i in range(n):
            low = 0
            for j in range(1,i):
                if int(x[j-1]) <= int(x[j]):
                    low = j
            x[n-1], x[low] = x[low], x[n-1]
        return x

def _comp(x1, x2):
    ret_val = []
    left = 0
    right = 0
    while (left < len(x1) and right < len(x2)):
        if x1[left] < x2[right]:
            ret_val.append(x1[left])
            left+=1
        else:
            ret_val.append(x2[right])
            right +=1
    ret_val.extend(x1[left:])
    ret_val.extend(x2[right:])
    return ret_val

def merge_sort(x):
    n = len(x)
    if n == 1:
        return x
    split = int(n/2)
    return _comp(merge_sort(x[:split]), merge_sort(x[split:]))

def quick_sort(x):
    if len(x) <= 1:
        return x
    piv = x[-1]
    lt = []
    rt = []
    for j in range(len(x)-1):
        if x[j] < piv:
            lt.append(x[j])
        else:
            rt.append(x[j])
    return [*quick_sort(lt),piv,*quick_sort(rt)]

if __name__ == "__main__":
    a =  rd.randint(1,200,7000)
    x = list(a)
    print(x[:100])
    t1 = time.perf_counter_ns()
    print(sorter_bubble_iter(x)[:100])
    t2 =  time.perf_counter_ns()
    print(int((t2-t1)/1000000), "Milliseconds")
    print(sel_sort(x)[:100])
    t3 =  time.perf_counter_ns()
    print(int((t3-t2)/1000000), "Milliseconds")
    print(ins_sort(x)[:100])
    t4 = time.perf_counter_ns()
    print(int((t4-t3)/1000000), "Milliseconds")
    t5 = time.perf_counter_ns()
    print(merge_sort(x)[:100])
    print(int((t5-t4)/100), "Microseconds")
    t6 = time.perf_counter_ns()
    print(quick_sort(x))
    print(int((t6-t5)/1000000), "Milliseconds")