# Thinking in Loops

In the previous lesson, we've seen how to do simple repeatitions using for loop. 
In this lesson, we are going to understand how to think in loops, how to approach a 
problem that requires repetition.

## A Row of Circles

Lets try to make a row of circles. We'll start with drawing three circles and then generalize to work with any number of circles using a for loop.

The straight-forward approach to draw three circles as row is to identify the radius and center of each circle.

<img src="/files/row-of-circles-v1.svg" style="width: 50%"/>

```{.python .joy .example}
r = 50
c1 = circle(x=-100, y=0, r=r)
c2 = circle(x=0, y=0, r=r)
c3 = circle(x=100, y=0, r=r)
show(c1, c2, c3)
```

While this approach is simple when the number of circles is small, we end up doing a lot of calculations when the number of circles is large. For example, even with 4 circles, the radius becomes 37.5 and the calculations becomes clumsy.

The first step is to make our job easy is to let the computer do the calculations.

<img src="/files/row-of-circles-v2.svg" style="width: 50%"/>


```{.python .joy .example}
n = 3
width = 300

d = width/n
r = d/2

left = -width/2

x1 = left + r
x2 = x1 + d
x3 = x2 + d

c1 = circle(x=x1, y=0, r=r)
c2 = circle(x=x2, y=0, r=r)
c3 = circle(x=x3, y=0, r=r)
show(c1, c2, c3)
```

This is a lot better approach than where we started. All the computations are now done by the computer. If you try change the value of `n` from `3` to `4`, it will divide the space into four parts and draws circles in the first 3 parts. 

We still need to figure out how to make the program draw `n` circles instead of always drawing `3` circles. That's where the `for` loop comes handy. Instead of drawing circles `c1`, `c2` and `c3`, we'll create and draw a circle `n` times.


```{.python .joy .example}
n = 3
width = 300

d = width/n
r = d/2

left = -width/2
x = left + r

for i in range(n):
    c = circle(x=x, y=0, r=r)
    show(c)
    x = x + d
```

Pay attention to what has changed now. We've replaced `x1`, `x2`, `x3` and `c1`, `c2`, `c3` with just `x` and `c`. The value of `x` is updated in the every iteration of the loop and the a circle `c` is drawn with the current value of `x`.

Try changing the value of n to whatever number you want and see it draw so many circles. 

{{ Exercise("six-donuts-in-a-row-jp") }}

## Generalizing Further

In the previous example, we've seen how to draw a row of circles using a for loop. In this section, we are going to make simple improvements to that make it more generic.

### Avoding dependencies between iterations

Try to visualize how the value of `x` is computed for the third circle. It is `d` more than the `x` of the sceond circle. There is an implicit dependency between each iteration. We can't completely understand an iteration independently without understanding all the previous ones. This makes the program hard to understand, especially when we start writing more and more complex programs.

One technique that is usuaully followed is making each iteration independent of other iterations. We could slightly tweak our program to achieve that.

```{.python .joy .example}
n = 3
width = 300

d = width/n
r = d/2

left = -width/2
xstart = left + r

for i in range(n):
    x = xstart + i * d
    c = circle(x=x, y=0, r=r)
    show(c)
```

Instead of updating the value of `x` in each iteration after drawing the circle, we are not computing the value `x` before drawing the circle in each iteration using the loop variable `i`. Also, we are taking the value of `xstart` as a reference to compute `x`. The `x` value for the first circle would be same as `xstart`, the second circle would be `xstart + d`, the third circle would be `xstart + 2*d` and so on. 

### Reuse with functions

What if we want to draw more than one row of circles, may be with a different value of `n` in each case?

We could convert our code to draw a row of cicles in to a function and call it as many times as we want.


```{.python .joy .example}
def draw_row(y, n):
    width = 300
    d = 300/n
    r = d/2

    left = -width/2
    x = left + r

    for i in range(n):
        c = circle(x=x, y=y, r=r)
        show(c)
        x = x + d

draw_row(y=100, n=3)
draw_row(y=0, n=5)
draw_row(y=-75, n=7)
```

Instead of incrementing the value of x in the loop, we could do something slightly different.

```{.python .joy .example}
def draw_row(y, n):
    width = 300
    d = 300/n
    r = d/2

    left = -width/2
    xstart = left + r
    
    for i in range(n):
        x = xstart + i * d
        c = circle(x=x, y=y, r=r)
        show(c)

draw_row(y=100, n=3)
draw_row(y=0, n=5)
draw_row(y=-75, n=7)
```

Instead of incrementing the value of `x` everytime in the loop, this computes the value of `x` using the loop variable `i` and reference value `xstart`.

### Returning a shape

It would interesting to return a combined shape instead of just showing it. That will allow us to apply different transformations to that shape.

For that we have to create a list of shapes and combine them. To do that let's see how to append elements to an existing list.

```{.python .joy .example}
numbers = []

numbers.append(1)
print(numbers)

numbers.append(2)
print(numbers)
```

The `.append` is a function that is available for lists, that adds the given argument to the list.

We are going to use this return a combine shape from our function. The name of the function is changed to `make_row` as we are only making a row in the function and not drawing it.

```{.python .joy .example}
def make_row(y, n):
    width = 300
    d = 300/n
    r = d/2

    xstart = -width/2 + r
    shapes = []

    for i in range(n):
        x = xstart + i * d
        c = circle(x=x, y=y, r=r)
        shapes.append(c)

    return combine(shapes)

shape = make_row(y=0, n=4)
shape2 = shape | rotate(90)
show(shape, shape2)
```

### Seperation of Concerns

While the previous approach made it possible to operate on the combine shape, it only only draws circles. If we want to change the shape, we need change the code deep inside the `make_row` function.

The issue is that the `make_row` function is doing two things: figuring out _where_ to draw the shapes and also _what_ to draw for each shape. Since both of them are in the same function, we need to navigate through the `where`, even if we just wanted to change `what` to draw. This issue could be eliminated by moving `what` to draw into a new function.


```{.python .joy .example}
def make_row(y, n):
    w = 300/n
    xstart = -150 + w/2
    shapes = []

    for i in range(n):
        x = xstart + i * w
        shape = make_shape(x, y, w)
        shapes.append(shape)

    return combine(shapes)

def make_shape(x, y, w):
    # return  circle(x=x, y=y, r=w/2)
    return ellipse(x=x, y=y, w=w, h=w/2)

shape = make_row(y=0, n=4)
shape2 = shape | rotate(90)
show(shape, shape2)
```

Instead of creating a circle shape, it delegates that work to a new function `make_shape`. This allows us to make changes only to the `make_shape` function when we need to change the shape. We'll never have to worry about touching the `make_row`.

### Simplifying further

Instead of passing x and y all the time, we could always draw the shape around the origin and translate it when required. That will make the job of `make_shape` simpler.

```{.python .joy .example}
def make_row(n):
    w = 300/n
    xstart = -150 + w/2
    shapes = []

    for i in range(n):
        x = xstart + i * w
        shape = make_shape(w) | translate(x=x)
        shapes.append(shape)

    return combine(shapes)

def make_shape(w):
    # return  circle(r=w/2)
    return ellipse(w=w, h=w/2)

shape = make_row(n=4)
show(shape)
```

We could do one more interesting thing here. Instead of the `make_row` function expecting that there will be a `make_shape` function, we could pass the function that is need to call to make the shape as an argument to it.

```{.python .joy .example}
def make_row(n, shape_maker):
    w = 300/n
    xstart = -150 + w/2
    shapes = []

    for i in range(n):
        x = xstart + i * w
        shape = shape_maker(w) | translate(x=x)
        shapes.append(shape)

    return combine(shapes)

def make_ellipse(w):
    return ellipse(w=w, h=w/2)

shape = make_row(4, make_ellipse)
show(shape)
```

Functions are like any other values and we could pass as arguments to other functions. The `make_row` function is called with `make_ellipse` as the value for parameter `shape_maker`, so whenever `shape_maker` is called, it calls the `make_ellipse` function.

### Parameterizing

So far, we are only drawing the same shape repeatedly. What if we want to show a slightly different shape based on where it is drawn. We could change the number shapes in each cell or the color or something else.

The following example draws a row of shapes with each shape having one more ellipse than it's previous.

```{.python .joy .example}
def parameterized_row(n):
    w = 300/n
    xstart = -150 + w/2
    shapes = []

    for i in range(n):
        x = xstart + i * w
        shape = make_shape(w, i, n) | translate(x=x)
        shapes.append(shape)

    return combine(shapes)

def make_shape(w, i, n):
    # repeat 1 time for the first one (i=0)
    # repeat 2 times for the second one (i=1) and so on
    count = i+1

    # we are using 180 insted of 360 because the ellpise is symmetrical.
    # Rotating it by 180 degrees gives the same shape.
    angle = 180/count
    return ellipse(w=w, h=w/2) | repeat(count, rotate(angle))

shape = make_row(n=4)
show(shape)
```

The `make_shape` function takes two additional arguments now. The `i`, which is the position or index of the curent shape and `n`, the total number of shapes in the row.


We could even apply the same technique to make shapes with different color in each step.


```{.python .joy .example}
def make_row(n):
    w = 300/n
    xstart = -150 + w/2
    shapes = []

    for i in range(n):
        x = xstart + i * w
        shape = make_shape(w, i, n) | translate(x=x)
        shapes.append(shape)

    return combine(shapes)

def make_shape(w, i, n):
    # We want n shades of red, including black
    # Leaving black, we have n-1 shades
    # Remembe that each color component has a value from 0 to 255.
    step = 255/(n-1)
    r = i * step # the red component
    fill = color(r=r, g=0, b=0)
    return circle(r=w/2, fill=fill)

shape = make_row(n=10)
show(shape)
```

### Summary

Let's quickly summarize what all steps we've taken to reach the final version.

* Started with a function `draw_row(y, n)` to draw n shapes
* Renamed the function `make_row` and made it return a combine shape instead of showing it. This allowed us to apply transformations on the combined shape.
* We've delegated the actual creation of shape to a new function `make_shape` so that can modify just that little function while keeping the `make_row` intact.
* We've simplified it further by taking away the `x` and `y` arguments from all the functions and used `translate` to position the shapes. This simplified the `make_shape` function quite a bit.
* Finally, we've parameterized the `make_shape` function by passing the arguments `i` and `n` to allow it create different shape based on the current position and total number of shapes being drawn.

This is the process that goes on to make any great software. Start with something simple, generalize it make it flexible to allow making changes to a small portion of the code while keep the most part intact.

## Excercies

Now, it is time for some exercises.

{{ Exercise("row-of-eyes-jp") }}
{{ Exercise("row-of-red-eyes-jp") }}
{{ Exercise("row-of-squares-jp") }}
{{ Exercise("row-of-growing-circles-jp") }}


{{ Exercise("six-concentric-circles-in-a-line-jp") }}
