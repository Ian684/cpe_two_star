import sys
from math import sqrt

def get_intersection(p1, p2, p3, p4):
    a1 = p2[1] - p1[1]
    b1 = p1[0] - p2[0]
    c1 = a1 * p1[0] + b1 * p1[1]
    
    a2 = p4[1] - p3[1]
    b2 = p3[0] - p4[0]
    c2 = a2 * p3[0] + b2 * p3[1]
    
    det = a1 * b2 - a2 * b1
    return [(b2 * c1 - b1 * c2) / det, (a1 * c2 - a2 * c1) / det]
def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    ptr = 0
    while ptr < len(data):
        d = float(data[ptr])
        n = int(data[ptr+1])
        ptr += 2
        
        if d == 0 and n == 0:
            break
            
        points = []
        for _ in range(n):
            points.append([float(data[ptr]), float(data[ptr+1])])
            ptr += 2
        shifted_lines = []
        for i in range(n):
            p1 = points[i]
            p2 = points[(i + 1) % n]
            
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            L = sqrt(dx**2 + dy**2)
            
            offset_x = (dy / L) * d
            offset_y = (-dx / L) * d
            
            line_p1 = [p1[0] + offset_x, p1[1] + offset_y]
            line_p2 = [p2[0] + offset_x, p2[1] + offset_y]
            shifted_lines.append((line_p1, line_p2))
        new_vertices = []
        for i in range(n):
            l1 = shifted_lines[(i - 1) % n]
            l2 = shifted_lines[i]
            v = get_intersection(l1[0], l1[1], l2[0], l2[1])
            new_vertices.append(v)
        area = 0.0
        for i in range(n):
            v1 = new_vertices[i]
            v2 = new_vertices[(i + 1) % n]
            area += v1[0] * v2[1]
            area -= v2[0] * v1[1]
        print(f"{abs(area) * 0.5:.3f}")
if __name__ == "__main__":
    solve()
