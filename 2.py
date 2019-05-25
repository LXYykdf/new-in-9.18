def inversionOne(part, lines):  # 部分倒影 
 
    newlines = copy.deepcopy(lines) 
    x = newlines[part[0]][part[1]][0] 
    for i in range(len(newlines[part[0]][part[1]])): 
        newlines[part[0]][part[1]][i] = 2 * x - newlines[part[0]][part[1]][i] 
 
    return newlines 
 
def inversionOne(part, lines):  # 部分倒影 
 
    newlines = copy.deepcopy(lines) 
    x = newlines[part[0]][part[1]][0] 
    for i in range(len(newlines[part[0]][part[1]])): 
        newlines[part[0]][part[1]][i] = 2 * x - newlines[part[0]][part[1]][i] 
 
    return newlines
