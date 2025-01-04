def solution(numbers, target):
    result = 0
    
    def dfs(index, current_sum):
        nonlocal result
        
        if index == len(numbers):
            if current_sum == target:
                result += 1
            return 
        
        #재귀호출
        dfs(index+1, current_sum +numbers[index])
        dfs(index+1, current_sum -numbers[index])
    

    dfs(0,0)
    return result 
