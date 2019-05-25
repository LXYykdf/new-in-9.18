def pri(out):   # 将三维数组格式改为给定目标格式的函数 
     
    lines_new = [] 
    for lines in out: 
        blank3=[] 
        for xj in lines: 
            xja = list(map(str,xj)) 
            a = ' '.join(xja) 
            blank1 = [[]] 
            blank1[0] = a 
            blank3.append(blank1) 
        string = '' 
        for k in range(len(blank3)): 
            if k == len(blank3)-1: 
                string = string + blank3[k][0] + '    ' + '\n'  # 增加换行 
            else: 
                string = string + blank3[k][0] + '    ' 
        lines_new.append(string) 
 
    return lines_new
