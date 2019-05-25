def transall(num, lines):  # 整体移调,生成新list 
 
    newlines = copy.deepcopy(lines) 
    for i in range(len(newlines)): 
        for j in range(len(newlines[i])): 
            for k in range(len(newlines[i][j])): 
                if newlines[i][j][k] == 0: 
                    pass 
                else: 
                    newlines[i][j][k] += num 
 
    return newlines 
 
def transposition(num, part, lines):  # 单个移调，生成新的list，part格式为一个list，如[1,1] 
 
    newlines = copy.deepcopy(lines) 
    for i in range(len(newlines[part[0]][part[1]])): 
        if newlines[part[0]][part[1]][i] == 0: 
            pass 
        else: 
            newlines[part[0]][part[1]][i] += num 
 
    return newlines
