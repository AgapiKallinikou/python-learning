def poly_area2(xy):
    n = len(xy)
    if n < 3:
        return None
    area = tri_area(xy[0], xy[1], xy[2])
    for i in range(3,n):
        area += tri_area(xy[0], xy[i-1], xy[i])
    return area
