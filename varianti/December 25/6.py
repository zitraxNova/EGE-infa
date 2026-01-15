import turtle as t
t.screensize(1000,1000)
k = 10
t.tracer(0)
t.down()
for i in range(5):
    t.fd(15 * k)
    t.lt(90)
    t.fd(25 * k)
    t.lt(90)
t.up()
t.fd(4 * k)
t.lt(90)
t.fd(12 * k)
t.lt(90)
t.down()
for i in range(6):
    t.fd(38 * k)
    t.lt(90)
    t.fd(22 * k)
    t.lt(90)
t.up()
for x in range(-100,100):
    for y in range(-100,100):
        t.goto(x * k,y * k)
        t.dot(4, 'magenta')

t.done()

# 36
