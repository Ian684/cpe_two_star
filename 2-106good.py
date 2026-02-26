import sys
from math import sqrt

def get_closest_on_segment(xm, ym, p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    dx, dy = x2 - x1, y2 - y1
    dpx, dpy = xm - x1, ym - y1
    mag_sq = dx*dx + dy*dy
    if mag_sq == 0:
        dist = sqrt((xm-x1)**2 + (ym-y1)**2)
        return [x1, y1], dist
    t = (dpx * dx + dpy * dy) / mag_sq
    if t < 0:
        closest = [x1, y1]
    elif t > 1:
        closest = [x2, y2]
    else:
        closest = [x1 + t * dx, y1 + t * dy]
    dist = sqrt((xm - closest[0])**2 + (ym - closest[1])**2)
    return closest, dist
input_data = sys.stdin.read().split()
if input_data:
    it = iter(input_data)
    try:
        while True:
            xm = float(next(it))
            ym = float(next(it))
            n = int(next(it))
            
            points = []
            for _ in range(n + 1):
                points.append((float(next(it)), float(next(it))))
            
            min_dist = float('inf')
            ans = [0.0, 0.0]
            
            for i in range(n):
                p_closest, d = get_closest_on_segment(xm, ym, points[i], points[i+1])
                if d < min_dist:
                    min_dist = d
                    ans = p_closest
            
            print(f"{ans[0]:.4f}")
            print(f"{ans[1]:.4f}")
    except EOFError:
        break
