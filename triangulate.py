import math
import triangle as tr
import matplotlib.pyplot as plt


def distance(P1, P2, x0, y0):
    x1, y1 = P1
    x2, y2 = P2

    num = abs((y2 - y1) * x0 - (x2 - x1) * y0 + x2 * y1 - y2 * x1)
    den = math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)

    return num / den


pts = [[0, 0], [0, 1], [1, 0]]

A = dict(vertices=pts)


B = tr.triangulate(A, 'qa0.001')

pts = B['vertices']
print(len(pts))
#  print(pts)
segs = tr.convex_hull(pts)

print(segs)

x = []
y = []

for pt in segs:
    u, v = pt
    ux, uy = pts[u]
    vx, vy = pts[v]
    x.append(ux)
    x.append(vx)
    y.append(uy)
    y.append(vy)

for pt in pts:
    if distance((0, 1), (1, 0), *pt) < 0.0002:
        x.append(pt[0])
        y.append(pt[1])


plt.plot(x, y, 'o-')

#  tr.compare(plt, A, B)
#  tr.plot(plt.axes(), vertices=pts, segments=segs)
plt.show()
