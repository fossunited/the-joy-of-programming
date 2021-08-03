# Thinking in Loops

In the previous lesson, we've seen how to do simple repetitions using for loop. 
In this lesson, we are going to learn how to think in loops, how to approach a problem that requires repetition.

## A Row of Circles

Let's try to make a row of circles, filling the entire width. We'll start with drawing three circles and then generalize to work with any number of circles using a for loop.

The straight-forward approach to draw three circles in a row is to identify the radius and center of each circle.

<img src="/files/row-of-circles-v1.svg" style="width: 50%"/>

```{.python .joy .example}
r = 50
c1 = circle(x=-100, y=0, r=r)
c2 = circle(x=0, y=0, r=r)
c3 = circle(x=100, y=0, r=r)
show(c1, c2, c3)
```

While this simple approach works when the number of circles is small, we end up doing a lot of calculations when the number of circles becomes large. For example, even with 4 circles, the radius becomes 37.5 and the calculations become clumsy.

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

This approach is a lot better than where we started. All the computations are now done by the computer. If you try to change the value of `n` from `3` to `4`, it will divide the space into four parts and draws circles in the first 3 parts. 

We still need to figure out how to make the program draw `n` circles instead of always drawing `3` circles. That's where the `for` loop comes in handy. Instead of drawing circles `c1`, `c2` and `c3`, we'll draw a circle `n` times.

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

Pay attention to what has changed now. We've replaced `x1`, `x2`, `x3` and `c1`, `c2`, `c3` with just `x` and `c`. The value of `x` is updated in every iteration of the loop and a circle is drawn with the current value of `x`.

Try changing the value of n to whatever number you want and see it draw so many circles. 

{{ Exercise("six-donuts-in-a-row-jp") }}

## Generalizing Further

In the previous example, we've seen how to draw a row of circles using a for loop. In this section, we are going to make a series of improvements to it make it more and more generic.

### Reuse with functions

What if we want to draw more than one row of circles, maybe with a different value of `n` in each case?

We could convert our code to draw a row of circles into a function and call it as many times as we want.


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

We could make one small improvement to the above program.

Try to visualize how the value of `x` is computed for the third circle. It is `d` more than the `x` of the second circle. There is an implicit dependency between each iteration. We can't completely understand an iteration independently without understanding all the previous ones. This makes the program a bit hard to understand, especially when we start writing more and more complex programs.

One technique that is usually followed is making each iteration independent of other iterations. We could slightly tweak our program to achieve that.

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

Instead of updating the value of `x` in each iteration after drawing the circle, we are now computing the value `x` before drawing the circle in each iteration using the loop variable `i` and a reference value `xstart` which is initialized before the loop.

As we start writing more and more programs, it is important to focus not only on getting it right but also on making it easy to read, understand and modify. Choosing the right variable names, splitting the program into smaller independent functions, avoiding dependencies whenever possible, etc. are some of the things to keep in mind when writing programs. 

### Returning a shape

It would interesting to return a combined shape instead of just showing it. That will allow us to apply different transformations to that shape.

For that, we have to create a list of shapes and combine them. To do that let's see how to append elements to an existing list.

```{.python .joy .example}
numbers = []

numbers.append(1)
print(numbers)

numbers.append(2)
print(numbers)
```

The `.append` is a function that is available for lists, that adds the given argument to the list.

We are going to use the `append` to create a list of shapes and return a combined shape from our function. The name of the function is changed to `make_row` as we are only making a row in the function and not drawing it.

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

In the above example, we constructing a list of shapes as we iterator through the loop and combine them into a single shape using the `combine` function.

### Separation of Concerns

While the previous approach made it possible to operate on the combined shape, it only draws circles. If we want to change the shape, we need to change the code deep inside the `make_row` function.

The issue is that the `make_row` function is doing two things: figuring out _where_ to draw the shapes and also _what_ to draw for each shape. Since both of them are in the same function, we need to navigate through the `where`, even if we just wanted to change `what` to draw. This issue could be eliminated by moving `what` to draw into a new function.


```{.python .joy .example}
def make_row(y, n):
    width = 300
    d = 300/n
    r = d/2

    xstart = -width/2 + d/2
    shapes = []

    for i in range(n):
        x = xstart + i * d
        shape = make_shape(x, y, d)
        shapes.append(shape)

    return combine(shapes)

def make_shape(x, y, w):
    # return  circle(x=x, y=y, r=w/2)
    return ellipse(x=x, y=y, w=w, h=w/2)

shape = make_row(y=0, n=4)
shape2 = shape | rotate(90)
show(shape, shape2)
```

Instead of creating a circle/ellipse shape, the `make_row` function now delegates that work to a new function `make_shape`. This allows us to make changes only to the `make_shape` function when we need to change the shape. We'll never have to worry about touching the code in `make_row` function.

We could do one more small improvement to the above program. Instead of passing `x` and `y` as arguments to the `make_shape` function, we could always draw the shape around the origin and let the `make_row` translate it as required. That simplifies the job of `make_shape` function.

```{.python .joy .example}
def make_row(y, n):
    width = 300
    d = 300/n
    r = d/2

    xstart = -width/2 + d/2
    shapes = []

    for i in range(n):
        x = xstart + i * d
        shape = make_shape(d) | translate(x=x, y=y)
        shapes.append(shape)

    return combine(shapes)

def make_shape(width):
    # return  circle(r=width/2)
    return ellipse(w=width, h=width/2)

shape = make_row(y=0, n=4)
shape2 = shape | rotate(90)
show(shape, shape2)
```

### More Generalization

In the previous example, we made it easy to change the code from drawing circles to drawing different shapes like ellipses in a row. What if we want to draw a row of circles and another row of ellipses?

Of course, we could make a copy of the `make_row` function that draws ellipses instead of circles, but that is not fun.

Can we generalize the `make_row` function to support drawing any shape in a row?

How about passing the function to make the shape as an argument to the `make_row` function. Yes, we can pass as arguments, just like we pass numbers and strings.

With this, the `make_row` function doesn't know what shape it is going to draw until it calls the function passed to it. 

```{.python .joy .example}
def make_row(y, n, shape_maker):
    width = 300
    d = 300/n
    r = d/2

    xstart = -width/2 + d/2
    shapes = []

    for i in range(n):
        x = xstart + i * d
        shape = shape_maker(d) | translate(x=x, y=y)
        shapes.append(shape)

    return combine(shapes)

def make_circle(width):
    return circle(r=width/2)

def make_ellipse(width):
    return ellipse(w=width, h=width/2)

shape1 = make_row(y=50, n=4, shape_maker=make_circle)
shape2 = make_row(y=-50, n=6, shape_maker=make_ellipse)
show(shape1, shape2)
```

Passing function as an argument may look strange, but it is a very useful technique. In this example, we made the `make_row`, in a way that we can plug in any new shape by passing a function to draw that shape at the time of calling `make_row`.

### Parameterizing Further

We've seen how to make more than one row and also how to make each row using a different shape.

What if we want to make each element of the row depend on its position?

<img src="/files/row-of-parameterized-shapes.svg" style="width: 50%"/>

For this, the function drawing the shape needs to know the position and possibly the total number of items in the row. We could change the way our `make_row` function calls the `shape_maker`. Earlier, we were calling it with just one argument `width`, now we'll pass two additional arguments `index` and `count`.

```{.python .joy .example}
def make_row(y, n, shape_maker):
    width = 300
    d = 300/n
    r = d/2

    xstart = -width/2 + d/2
    shapes = []

    for i in range(n):
        x = xstart + i * d
        shape = shape_maker(d, i, n) | translate(x=x, y=y)
        shapes.append(shape)

    return combine(shapes)

def make_circles(width, index, count):
    return concentric_circles(max_radius=width/2, n=index+1)

def concentric_circles(max_radius, n):
    step = max_radius / n
    r = max_radius
    shapes = []
    for i in range(n):
        c = circle(r=r)
        shapes.append(c)
        r = r - step
    return combine(shapes)

def make_ellipses(width, index, count):
    n = index+1
    return ellipse(w=width, h=width/2) | repeat(n, rotate(180/n))

def make_colors(width, index, count):
    # pick the red component of the color from the current position in the row
    red = 255*index/(count-1)
    fill = color(r=red, g=0, b=0)
    return circle(r=width/2, fill=fill, stroke="none")

shape1 = make_row(y=100, n=4, shape_maker=make_circles)
shape2 = make_row(y=0, n=4, shape_maker=make_ellipses)
shape3 = make_row(y=-100, n=10, shape_maker=make_colors)
show(shape1, shape2, shape3)
```

In the above example, we've made three rows of shapes. The first one uses the position in the row to determine the number of concentric circles to draw, the second one uses the position to find out the number of times to repeat the ellipse around and the last one uses the position and count to compute the fill color of the shape.

### Summary

Let's quickly summarize all steps we've taken to reach the final version.

* Started with a very simple implementation of drawing 3 circles in a row
* Improved it by making the computer do the calculations
* Converted that into a for loop so that it can draw n circles for any number n
* Moved the code to draw a row of shapes into a function to be able to two rows for circles
* Made the function return a combined shape, instead of showing one shape at a time, to allow us to apply transformations it
* Generalized it further to draw a row of circles and a row of ellipses by passing the function to create individual shape as an argument to the `make_row` function
* Extended it further to allow each shape in the row be different based on the current position in the row and the number of shapes in the row as an argument to the function creating the shape

As you can notice, we started with a 5-line program and ended up with close to a 50-line program. Each improvement made the program more flexible, but at the same time increased the complexity, making it more difficult to understand. 

This is typical software evolution. We start with a very simple approach, then the requirements change and we end up generalizing the program to support the new requirements while continuing to support the previous ones.

The art of software development is a fine balance between making it simple and making it flexible. 

## Exercises

Now, it is time for some exercises.

{{ Exercise("row-of-eyes-jp") }}
{{ Exercise("row-of-red-eyes-jp") }}
{{ Exercise("row-of-squares-jp") }}
{{ Exercise("row-of-growing-circles-jp") }}
