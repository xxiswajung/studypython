def solution(dirs):
    comm = {'U':(0, 1), 'D':(0, -1), 'L':(-1, 0), 'R':(1, 0)} #dictionary
    road = set()
    x, y = (0,0)
    
    for k in dirs:
        xx, yy = x + comm[k][0], y + comm[k][1]
        if -5<=xx<=5 and -5<=yy<=5:
            road.add(((x, y), (xx, yy)))
            road.add(((xx, yy), (x, y)))
            x, y = xx, yy

    return len(road) // 2