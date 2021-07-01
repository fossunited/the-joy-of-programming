# Repeating Shapes

We could use the for loop to draw a lot of circles.

Let's try to draw ten circles.

```{.python .joy .example}
x, y = 0, 0
r = 50

for i in range(10):
    c = circle(x, y, r)
    show(c)
```

Why do we see only one circle? The program is actually drawing 10 circles, but it is drawing them at the same place again and again.

Let's make it do something different every time it draws a circle. The circle function takes three arguments x, y and d. We could try changing one of them in the loop so that it gets a different value in every iteration.

```{.python .joy .example}
x, y = 0, 0
r = 50

for i in range(10):
    c = circle(x, y, r)
    show(c)
    x = x + 10
```

Do you see 10 circles now?

What happens when you change the value of `y` or `r` instead of `x`? What
if you change more than one value at a time?

### Example: Concentric Circles

Now, let's write a program to draw concentric circles.

```{.python .joy .example}
x, y = 0, 0
r = 100
n = 10

# the difference in the radius of two consequetive circles
step = r/n

# we start with drawing the outer circle first and then keep on drawing
# the next smaller circle and  so on
for i in range(n):
    c = circle(x=x, y=y, r=r)
    show(c)
    r = r-step
```

As you can see that draws one concentric circle. Wouldn't it be good it turn that into a function so that we can use it more than once?

```{.python .joy .example}
def concentric_circles(x, y, r, n):
    # we start with drawing the outer circle first
    # and start moving inside, drawing circles one by one
    step = r/n
    for i in range(n):
        c = circle(x=x, y=y, r=r)
        show(c)
        r = r-step

w, h = 300, 300
r = 100
n = 10

# concentric circles at the center of the canvas
concentric_circles(0, 0, r, n)

# concentric circles at each corner
concentric_circles(w/2, h/2, r, n)
concentric_circles(w/2, -h/2, r, n)
concentric_circles(-w/2, h/2, r, n)
concentric_circles(-w/2, -h/2, r, n)
```

One thing important to notice here is that the body of the `concentric_circles` function is indented by four spaces. The body of the function contains a _for loop_ and it's body is further indented by four spaces. So, there are two levels of indentation for the code inside the for loop.

Try playing with changing the values of `r` and `n` and see what you get. You can try removing the concentric circles in the center. You'll be surprised with how many wonerful patterns that you can create.

As you can see we can start with simple concepts like circle, build more concepts like concentric circles using the simple concepts and use all of these together to make non-trivial skeches.

This is the basic pattern that is followed in software development. If you really want to understand how complex software is made, pay attention to how to solve larger problems by writing simple functions and combining them. Try to use this approach whenever you are solving exercises. It not only makes the problem easy to solve, but also makes it lot more fun.

{{ Exercise("six-circles-in-a-line-jp") }}
{{ Exercise("six-donuts-in-a-line-jp") }}
{{ Exercise("six-concentric-circles-in-a-line-jp") }}
