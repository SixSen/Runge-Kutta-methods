# 四阶经典龙格-库塔法
def f(ex, ey):
    return 3*ey/(1 + ex)


x0 = 0
xm = 1
y0 = 1
h = 0.2
N = 10
n = 1


while n < N and x0 < xm:
    x1 = x0 + h
    k1 = f(x0, y0)
    k2 = f(x0 + h/2, y0 + (h/2)*k1)
    k3 = f(x0+h/2, y0 + (h/2)*k2)
    k4 = f(x1, y0 + h*k3)
    y1 = y0 + h/6 * (k1 + 2*k2 + 2*k3 + k4)
    print("x{0}={1:0.1f}\t\t y{0}={2:0.6f}".format(n, x1, y1))
    n = n + 1
    x0 = x1
    y0 = y1
