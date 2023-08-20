def test(h,al,de,status):
    p = 0
    r = 0
    if h > de:
        if de > (3 -al):
            p = (3-al)
            r = h-(3-al)
            status = True
        else:
            p = de
            r = h-de
            status = True
    else:
        if h > (3-al):
            p = (3-al)
            r = h - (3-al)
        else:
            p = h
            r = 0
    return p,r,status
x ,y,status = test(7,1,2,False)
print(x,'---',y,status)
            
