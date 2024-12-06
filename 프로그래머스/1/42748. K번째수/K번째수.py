def solution(array, commands):

    selected_element = [] 

    for command in commands:
        newArray = array[command[0] - 1:command[1]]
        newArray.sort()
        selected_element.append(newArray[command[2] - 1])
    
    return selected_element