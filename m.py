def revers(lines):  # 倒置函数，把倒置的line存到新的list里面 
 
    newlines = copy.deepcopy(lines) 
    for i in newlines: 
        i.reverse()  # 对声部进行处理 
        for j in i: 
            j.reverse()  # 对小节进行处理 
    newlines.reverse()  # 对整体进行处理 
 
    return newlines 
 
 
def partialreverse(part, lines):  # 倒置一部分 
 
    newlines = copy.deepcopy(lines) 
    newlines[part[0]][part[1]].reverse() 
 
    return newlines
