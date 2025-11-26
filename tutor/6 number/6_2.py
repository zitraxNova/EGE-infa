import turtle as t
t.screensize(1000,1000)
k = 10
t.tracer(0)
t.down()
for i in range(9):
    t.fd(22*k)
    t.rt(90)
    t.fd(6*k)
    t.rt(90)
t.up()
t.fd(1*k)
t.rt(90)
t.fd(5*k)
t.lt(90)
t.down()
for i in range(9):
    t.fd(53*k)
    t.rt(90)
    t.fd(75*k)
    t.rt(90)
t.up()
for x in range(-100, 100):
    for y in range(-100, 100):
        t.goto(x * k, y * k)
        t.dot(4, 'magenta')

t.done()

# 44