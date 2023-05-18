import turtle

def petal(t, radius, angle):
    for i in range(2):
        t.circle(radius, angle)
        t.left(100 - angle)

def flower(t,n,radius,angle):
    for i in range(n):
        petal(t, radius, angle)
        t.left(360 / n)

