import turtle as t
t.screensize(1000, 1000)
k = 10
t.tracer(0)
t.down()
for i in range(13):
    t.fd(17 * k)
    t.lt(90)
    t.fd(15 * k)
    t.lt(90)
t.up()
t.fd(10 * k)
t.lt(90)
t.fd(10 * k)
t.rt(90)
t.down()
for i in range(40):
    t.fd(100 * k)
    t.rt(90)
    t.fd(200 * k)
    t.rt(90)
t.up()
for x in range(-100, 100):
    for y in range(-100, 100):
        t.goto(x * k, y * k)
        t.dot(4, 'magenta')
t.done()
# 30