import random
width = 4
height = 3


paths = []
x = 0
while len(paths) < 35:
    path = []
    while path.count('r') < width or path.count('d') < height:
        ran = random.random()
        if path.count('r') == width:
            path.append('d')
        elif path.count('d') == height:
            path.append('r')
        elif ran < (.75):
            path.append('r')
        else:
            path.append('d')
    x += 1

    pathStr = ''.join(path)
    if pathStr not in paths:
        paths.append(pathStr)

#print(paths)
print(x)
    
