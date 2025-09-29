def solution(board, moves):
    answer = 0
    result = []
    for i in moves: 
        i = i - 1
        for j in range(len(board)):
            if board[j][i] != 0:
                if result and result[-1] == board[j][i]:
                    result.pop()
                    answer += 2
                else:
                    result.append(board[j][i])   
                board[j][i] =0
                break
               
    return answer