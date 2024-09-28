def solution(wallet, bill):
    answer = 0
    
    wallet.sort()
    bill.sort()
    wallet_max = max(wallet)
    wallet_min = min(wallet)
    bill_max = max(bill)
    bill_min = min(bill)


    while bill_max > wallet_max or bill_min > wallet_min:
        max_index = bill.index(bill_max)
        bill[max_index] = bill_max // 2  
        bill_max = max(bill)
        bill_min = min(bill)
        answer += 1 

    return answer
