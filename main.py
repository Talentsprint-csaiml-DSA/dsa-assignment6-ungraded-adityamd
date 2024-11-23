def soln(boxes, ind, lt, wd, ht):
    if ind == len(boxes):
        return 0
    mx = -1
    for i in range(ind, len(boxes)):
        tmp = -1
        if lt > boxes[ind][0] and wd > boxes[ind][1] and ht > boxes[ind][2] or lt == -1:
            tmp = 1 + soln(boxes, ind+1, boxes[ind][0], boxes[ind][1], boxes[ind][2])
        tmp1 = soln(boxes, ind+1, lt, wd, ht)
        if tmp > mx:
            if tmp > tmp1:
                mx = tmp
            else:
                mx = tmp1
        else:
            if mx < tmp1:
                mx = tmp1
    
    return mx

def longest_box_sequence(boxes):
    boxes = sorted(boxes, key = lambda x: x[0]*x[1]*x[2], reverse=True)
    return soln(boxes, 0, -1, -1, -1)    
