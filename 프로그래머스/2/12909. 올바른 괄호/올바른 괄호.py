
def solution(s):
    answer = True
    
    list_s = list(s)
    stack = []
    for i in list_s:
        if i == '(':
            stack.append(i)
        else: 
            if stack:  
                stack.pop()
            else:      
                answer = False
                break
    
    if len(stack) != 0:
        answer = False 
        
        
        

    return answer