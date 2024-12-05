from collections import Counter

def solution(clothes):
    clothes_count = Counter([kind for _, kind in clothes])
    
    combinations = 1
    for count in clothes_count.values():
        combinations *= (count + 1)  

    return combinations - 1
