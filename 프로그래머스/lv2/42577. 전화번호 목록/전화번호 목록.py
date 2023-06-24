def solution(phone_book):
    dict={phone_book[i]:1 for i in range(len(phone_book))}
    for nums in phone_book: 
        arr = "" 
        for num in nums: 
            arr += num
            if arr in dict and arr != nums:       
                return False 
    return True