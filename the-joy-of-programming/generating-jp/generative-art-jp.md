# Generative Art

Just like how too much order is boring, too much randomness is also not very interesting. Things get really interesting when we create things that in good order, with a pinch of randomness.

## Random Bars

Instead of creating lines completely in random, lets create vertical lines of random height starting from the bottom of the canvas.

Notice that we are drawing lines just like in one of the exercises in the previous lesson, but only the height is random and everything else is fixed.

```{.python .joy .example}
def bar(x, h):
    return line(x1=x, y1=-150, x2=x, y2=-150+h)

for x in range(-150, 150):
    h = random(300)
    b = bar(x=x, h=h)
    show(b)
```

The `bar` function create a new veritical line at speifcied height and x location. We are using that to draw 300 bars one for each x coordinate, with random height.

While, the previous example is draw the bars at random, it doesn't create a new shape that could be used elsewhere, like applying a transformation.

In the following example, we'll see how to combine all the bars into a single shape. For this we are going to create a list of shapes first and then combine them using the `combine` function.

For creating a list of shapes, we start with an empty list and start appending one bar at a time in a loop.


```{.python .joy .example}
def bar(x, h):
    return line(x1=x, y1=-150, x2=x, y2=-150+h)

bars = []
for x in range(-150, 150):
    h = random(300)
    b = bar(x=x, h=random(h))
    bars.append(b)

shape = combine(bars)
show(shape)
```

The technique of creating a list of shapes and then combining them into a single shape is quite useful and we are going to use this quite a lot from now on.

## Random Concentric Circles

Let's look at another example now. This time were going to draw circles with a random radius, while keeping the center fixed.

```{.python .joy .example}
def random_concentric_circles(n, r):
    shapes = []
    for i in range(n):
        r1 = random(0, r)
        c = circle(r=r1)
        shapes.append(c)
    return combine(shapes)

shape = random_concentric_circles(n=10, r=100)
show(shape)
```

The `random_concentric_circles` function takes two arguments `n`, the number of circles and `r`, the maximum radius. It creates `n` circles, with each one of them having a radius between `0` and `r`, picked at random.

## Making Grids

It is a lot of fun to make a grid of shapes, each slightly different.

Lets start with creating a 4x4 grid of circles.


```{.python .joy .example}
n = 4
d = 300/n
r = d/2

for i in range(n):
    for j in range(n):
        y = -(i*d+d/2-150)
        x = j*d+d/2-150
        c = circle(x=x, y=y, r=r)
        show(c)
```

This may look a bit tricky. We are using a nested loop here. The i goes over the rows and `j` goes over the columns. Each (i, j) represents once cell and for cell we are comuting the `x` and `y` coordinates of the center.

Let's convert that into a useful function.

```{.python .joy .example}
def simple_grid(n):
    d = 300/n
    r = d/2

    shapes = []
    for i in range(n):
        for j in range(n):
            y = -(i*d+d/2-150)
            x = j*d+d/2-150
            c = circle(x=x, y=y, r=r)
            shapes.append(c)
    return combine(shapes)

shape = simple_grid(4)
show(shape)
```

This is neat, but that only works for circles. What if we want draw a grid of ellipses or a new shape? Let's see how to generalize the `simple_grid` to support drawing any shape in a grid.

For doing this, we need to make the `simple_grid` take a function `shape_maker` as an argument which when given center and the `d`, the width or height of the cell as argument, creates the shape. The `simple_grid` function call that function multiple times in the loop to create that shape.

```{.python .joy .example}
def simple_grid(n, shape_maker):
    d = 300/n
    r = d/2

    shapes = []
    for i in range(n):
        for j in range(n):
            y = -(i*d+d/2-150)
            x = j*d+d/2-150
            c = shape_maker(x=x, y=y, d=d)
            shapes.append(c)
    return combine(shapes)

def make_ellipse(x, y, d):
    return ellipse(x=x, y=y, w=d, h=d/2)

shape = simple_grid(4, make_ellipse)
show(shape)
```

# Random Concentric Circles in a Grid

