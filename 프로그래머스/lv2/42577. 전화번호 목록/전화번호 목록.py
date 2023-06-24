def solution(phone_book):
    dict={phone_book[i]:1 for i in range(len(phone_book))}
    for nums in phone_book: 
        arr = "" 
        for num in nums: 
            arr += num
            if arr in dict and arr != nums: #누적된 arr와 dict안의 숫자와 같은지(앞에서 부터 더했으니) 확인, 그리고 자기자신인건 확인하지 않는다.
                return False 
    return True

############################
##문제에선 hash를 이용하라고 했지만 hash보단 아래가 더 빠르고 효율적임

def solution(phone_book):
    answer = True
    phone_book.sort() #문자열을 정렬할땐 숫자 크기대로 정렬되지 않고, 숫자의 유니코드 순대로 정렬된다
    for i in range(len(phone_book)-1): 
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]: #그러므로 옆에 있는 문자열과만 비교하면 된다
            answer = False
            break
    return answer
