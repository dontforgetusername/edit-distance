import numpy as np
import matplotlib.pylab as pl

LEFT = 'left'
UP = 'up'
DIAG = 'diag'

def editDistance(s1, s2):
    m = len(s1) #row
    n = len(s2) #col
    ED = [[0 for i in range(n + 1)] for j in range(m + 1)]
    p = [[[] for i in range(n + 1)] for j in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if j == 0:
                ED[i][j] = i
                p[i][j].append(UP)
            elif i == 0:
                ED[i][j] = j
                p[i][j].append(LEFT)
            elif s1[i - 1] == s2[j - 1]:
                ED[i][j] = ED[i - 1][j - 1]
                p[i][j] = DIAG
            else:
                insertion = ED[i][j - 1] + 1
                deletion = ED[i - 1][j] + 1
                substitution = ED[i - 1][j - 1] + 2
                ED[i][j] = min(insertion, deletion, substitution)
                if ED[i][j] == insertion:
                    p[i][j].append(LEFT)
                if ED[i][j] == deletion:
                    p[i][j].append(UP)
                if ED[i][j] == substitution:
                    p[i][j].append(DIAG)

    #distance of the first i characters (s1) and first j chars (s2) (p has the same index value) is ED[i+1][j+1]
                
    return ED, p

def backtrace(s1, s2, ED, p):
    i, j = len(s1), len(s2)
    path = [(i, j)]
    while (i != 0 or j != 0):
        if DIAG in p[i][j] and i != 0 and j != 0:
            i, j = i - 1, j - 1
            path.append((i, j))
        elif LEFT in p[i][j] and j != 0:
            j = j - 1
            path.append((i, j))
        elif UP in p[i][j] and i != 0:
            i = i - 1
            path.append((i, j))
    path.reverse()
    return path

def alignment(s1, s2, p, path):
    align_s1 = ''
    align_s2 = ''
    for index in range(len(path)):
        if index != 0:
            (i, j) = path[index]
            if DIAG in p[i][j]:   #substitute or same character at s1[i-1], s2[j-1]
                align_s1 += s1[i - 1]
                align_s2 += s2[j - 1]
            elif LEFT in p[i][j]:   #insert j - 1 char of s2 to s1
                align_s1 += '*'
                align_s2 += s2[j - 1]
            elif UP in p[i][j]:   #delete s1 at i - 1 position
                align_s1 += s1[i - 1]
                align_s2 += '*'



    return align_s1, align_s2



def draw(s1, s2):
    rows = len(s1) + 1
    cols = len(s2) + 1

    characters1 = ['#']
    for c in s1:
        characters1.append(c)
    characters2 = ['#']
    for c in s2:
        characters2.append(c)

    ED, p = editDistance(s1, s2)
    path = backtrace(s1, s2, ED, p)
    align_s1, align_s2 = alignment(s1, s2, p, path)
    colors = [['w' for i in range(cols)] for j in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if (i, j) in path:
                colors[i][j] = '#1ac3f5'

    pl.figure()
    pl.table(cellText=ED, cellColours=colors, loc=(0,0), cellLoc='center', rowLabels=characters1, colLabels=characters2)

    pl.annotate(align_s1 + '\n' + align_s2, (0,0), (0, -20), xycoords='axes fraction', textcoords='offset points', va='top')


    

    
    pl.show()
    



draw("intention", "execution")