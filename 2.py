def randomapart(lines): 
 
    len1 = len(lines) 
    part = [] 
    randomnunm1 = random.randrange(len1) 
    part.append(randomnunm1) 
    len2 = len(lines[randomnunm1]) 
    randomnunm2 = random.randrange(len2) 
    part.append(randomnunm2) 
 
    return part
