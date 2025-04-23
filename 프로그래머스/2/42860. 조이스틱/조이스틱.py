def solution(name):
    answer = 0
    name_list = list(name)
    
    alphabet_list = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    
    for i in name_list:
        idx = alphabet_list.index(i)
        
        
        if idx == 0:  
            continue
        elif idx <= 13:  
            answer += idx
        else:  
            reverse_index = len(alphabet_list) - idx
            answer += reverse_index
            
    move = len(name_list) - 1
    for i in range(len(name_list)):
        next_idx = i + 1
        while next_idx < len(name_list) and name_list[next_idx] == 'A':
            next_idx += 1
        distance = min(i * 2 + len(name_list) - next_idx,
                       (len(name_list) - next_idx) * 2 + i)
        move = min(move, distance)

    return answer + move
        

