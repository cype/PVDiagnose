import math


#pre: give a list
#post: returns the average of the list
def average(alist):
    aver = 0
    for n in alist:
        aver += n
    return aver / len(alist)


#pre: give the list
#post: returns the variance of the list
def variance(alist):
    summe = 0
    aver = average(alist)
    for n in alist:
        summe += (n - aver)**2
    return math.sqrt(summe/(len(alist)-1))
