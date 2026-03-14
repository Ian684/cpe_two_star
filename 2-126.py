import math
import sys

def solve(ar1, ar2, ar3):
    pi = math.pi
    r1 = math.sqrt(ar1/pi)
    r2 = math.sqrt(ar2/pi)
    r3 = math.sqrt(ar3/pi)
    
    d12, d13, d23 = r1+r2, r1+r3, r2+r3
    O1 = (0.0, 0.0)
    O2 = (d12, 0.0)
    O3x = (d13**2 - d23**2 + d12**2) / (2*d12)
    O3y = math.sqrt(max(0.0, d13**2 - O3x**2))
    O3 = (O3x, O3y)
    
    centers = [O1, O2, O3]
    radii   = [r1, r2, r3]
    
    def all_inside(cx, cy, R):
        return all(math.sqrt((cx-px)**2+(cy-py)**2) + ri <= R + 1e-9
                   for (px,py), ri in zip(centers, radii))
    
    best_R = float('inf')
    
    # Try MEC determined by each pair of circles
    for i, j in [(0,1),(0,2),(1,2)]:
        x1,y1 = centers[i]; ra = radii[i]
        x2,y2 = centers[j]; rb = radii[j]
        d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        if d + min(ra,rb) <= max(ra,rb) + 1e-12:
            cx, cy, R_try = (x1,y1,ra) if ra >= rb else (x2,y2,rb)
        else:
            R_try = (d + ra + rb) / 2.0
            t = (R_try - ra) / d
            cx = x1 + t*(x2-x1); cy = y1 + t*(y2-y1)
        if all_inside(cx, cy, R_try) and R_try < best_R:
            best_R = R_try
    
    # Try MEC determined by all 3 circles (Soddy outer)
    k1, k2, k3 = 1/r1, 1/r2, 1/r3
    sq = math.sqrt(k1*k2 + k2*k3 + k1*k3)
    k_out = k1 + k2 + k3 - 2*sq
    if k_out < 0:
        R_try = -1.0 / k_out
        A_ox = (d12**2+r1**2-r2**2)/(2*d12); B_ox = (r2-r1)/d12
        A_oy = (d13**2+r1**2-r3**2-2*O3x*A_ox)/(2*O3y)
        B_oy = (2*(r3-r1)-2*O3x*B_ox)/(2*O3y)
        cx = A_ox+B_ox*R_try; cy = A_oy+B_oy*R_try
        if all_inside(cx, cy, R_try) and R_try < best_R:
            best_R = R_try
    
    R = best_R
    Sr = 1.0 / (k1 + k2 + k3 + 2*sq)
    
    # Tangency points A (c1∩c2), B (c1∩c3), C (c2∩c3)
    Ax = O1[0]+r1*(O2[0]-O1[0])/d12; Ay = O1[1]+r1*(O2[1]-O1[1])/d12
    Bx = O1[0]+r1*(O3[0]-O1[0])/d13; By = O1[1]+r1*(O3[1]-O1[1])/d13
    Cx = O2[0]+r2*(O3[0]-O2[0])/d23; Cy = O2[1]+r2*(O3[1]-O2[1])/d23
    An = 0.5*abs((Bx-Ax)*(Cy-Ay) - (Cx-Ax)*(By-Ay))
    
    print(f"{R:.10f} {Sr:.10f} {An:.10f}")

for line in sys.stdin:
    line = line.strip()
    if not line: continue
    parts = line.split()
    if len(parts) == 3:
        solve(float(parts[0]), float(parts[1]), float(parts[2]))
