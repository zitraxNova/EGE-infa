import turtle as t
t.screensize(1000, 1000)
k = 10
t.tracer(0)
t.down()
for i in range(2):
    t.fd(28 * k)
    t.rt(90)
    t.fd(18 * k)
    t.rt(90)
t.up()
t.fd(14 * k)
t.rt(90)
t.fd(10 * k)
t.lt(90)
t.down()
for i in range(2):
    t.fd(30 * k)
    t.rt(90)
    t.fd(7 * k)
    t.rt(90)
t.up()
for x in range(-100, 100):
    for y in range(-100, 100):
        t.goto(x * k, y * k)
        t.dot(4, 'magenta')
t.done()
# 679