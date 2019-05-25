f1 = open("mergedL.txt")  # tone文件 
f2 = open("timeL.txt")  # time文件 
f3 = open("mergedR.txt") 
f4 = open("timeR.txt") 
 
def getlinesfloat(afile):  # 按行输入 
    line = afile.readlines() 
    for i in range(len(line)): 
        line[i] = list(line[i].split("    "))  # 按空四个格的特征进行切分  
        for j in range(len(line[i])): 
            line[i][j] = list(map(float, line[i][j].split()))  # 获得小节 
        line[i].pop()  # 去除最后的“/n” 
