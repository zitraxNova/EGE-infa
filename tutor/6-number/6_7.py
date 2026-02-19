import turtle as t
t.screensize(1000,1000)
k = 10
t.tracer(0)
t.down()
for i in range(3):
    t.fd(27*k)
    t.rt(90)
    t.fd(12*k)
    t.rt(90)
t.up()
t.fd(4*k)
t.rt(90)
t.fd(6*k)
t.lt(90)
t.down()
for i in range(4):
    t.fd(83*k)
    t.rt(90)
    t.fd(77*k)
    t.rt(90)
t.up()
for x in range(-100, 100):
    for y in range(-100, 100):
        t.goto(x * k, y * k)
        t.dot(4, 'magenta')

t.done()

# 6748