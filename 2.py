def inversionall(lines):  # 整体倒影

    newlines = copy.deepcopy(lines)
    for i in range(len(newlines)):
        for j in range(len(newlines[i])):
            x = newlines[i][j][0]
            for k in range(len(newlines[i][j])):
                newlines[i][j][k] = 2 * x - newlines[i][j][k]

    return newlines


def inversionOne(part, lines):  # 部分倒影

    newlines = copy.deepcopy(lines)
    x = newlines[part[0]][part[1]][0]
    for i in range(len(newlines[part[0]][part[1]])):
        newlines[part[0]][part[1]][i] = 2 * x - newlines[part[0]][part[1]][i]

    return newlines
