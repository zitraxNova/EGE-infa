import turtle as t
t.screensize(1000,1000)
k = 10
t.tracer(0)
t.down()
t.right(30)
for i in range(3):
    t.rt(150)
    t.fd(6 * k)
    t.rt(30)
    t.fd(12 * k)
for x in range(-100, 100):
    for y in range(-100, 100):
        t.goto(x * k, y * k)
        t.dot(4, 'magenta')

t.done()

# ?????