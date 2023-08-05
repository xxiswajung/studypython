from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer=[]
    for x in course:
        arr=[]
        for order in orders:
            com=combinations(sorted(order),x)
            arr+=com #리스트에 리스트를 누적해서 더하는 것 이므로 append 사용 불가
        counter=Counter(arr)
        if len(counter)!=0 and max(counter.values())>=2 : #len(counter)!=0 은 조합된 단어보다 course가 작을 경우, 숫자가 세어지지 않아 counter가 비어짐
            answer+=[''.join(f) for f in counter if counter[f]==max(counter.values())]
            #리스트에 리스트를 누적해서 더하는 것 이므로 append 사용 불가
    return sorted(answer)
