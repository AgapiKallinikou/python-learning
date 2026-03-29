def poly_areal(xy):
    n = len(xy)
    if n < 3:
        return None
    elif n == 3:
        return tri_area(xy[0], xy[1], xy[2])
    else:
        return poly_areal(xy[:n-1]) + tri_area(xy[0], xy[n-2], xy[n-1])

def tri_area(p1, p2, p3):
    return abs(p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1] - p1[0]*p3[1]
               - p2[0]*p1[1] - p3[0]*p2[1])/2
