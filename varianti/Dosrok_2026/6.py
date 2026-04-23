import turtle as t
t.screensize(1000, 1000)
k = 15
t.tracer(0)
t.down()
for i in range(315):
    for j in range(7):
        t.fd(12 * k)
        t.rt(45)
        t.fd(6 * k)
        t.rt(135)
t.up()
for x in range(-100, 100):
    for y in range(-100, 100):
        t.goto(x * k, y * k)
        t.dot(4, 'magenta')
t.done()
# 40