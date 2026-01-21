import turtle as t
t.screensize(1000,1000)
k = 10
t.tracer(0)
t.down()
for i in range(2):
    t.fd(3 * k)
    t.rt(90)
    t.fd(20 * k)
    t.rt(90)
t.up()
t.bk(8 * k)
t.rt(90)
t.fd(9 * k)
t.lt(90)
t.down()
for i in range(2):
    t.fd(16 * k)
    t.rt(90)
    t.fd(8 * k)
    t.rt(90)
t.up()
for x in range(-100, 100):
    for y in range(-100, 100):
        t.goto(x * k, y * k)
        t.dot(4, 'magenta')
t.done()
# 201 
