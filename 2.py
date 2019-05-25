def extend(num, lines):  # 整体延长,生成新list 
 
    newlines = copy.deepcopy(lines) 
    for i in range(len(newlines)): 
        for j in range(len(newlines[i])): 
            for k in range(len(newlines[i][j])): 
                newlines[i][j][k] *= num 
 
    return newlines
