from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer=[]
    for x in course:
        arr=[]
        for order in orders:
            com=combinations(sorted(order),x)
            arr+=com
        counter=Counter(arr)
        if len(counter)!=0 and max(counter.values())>=2 :
            answer+=[''.join(f) for f in counter if counter[f]==max(counter.values())]
    return sorted(answer)