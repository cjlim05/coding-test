def solution(video_len, pos, op_start, op_end, commands):
    
    mm, ss = map(int, video_len.split(":"))
    newVideo = mm*60 + ss
    
    mm, ss = map(int, pos.split(":"))
    newPos = mm*60 + ss
    
    mm, ss = map(int, op_start.split(":"))
    newopStart = mm*60 + ss
    
    mm, ss = map(int, op_end.split(":"))
    newopEnd = mm*60 + ss
    
    if(newopStart< newPos <newopEnd):
        newPos = newopEnd
    
    
    for command in commands:
        if command == 'prev':
            newPos -= 10
            if newPos < 0:  
                newPos = 0
        elif command == 'next':
            newPos += 10
            if newPos >= newVideo:  
                newPos = newVideo

        
        if newopStart <= newPos <= newopEnd:
            newPos = newopEnd
    


    
    mm = newPos // 60  
    ss = newPos % 60
    

    answer = f"{mm:02}:{ss:02}"
    return answer