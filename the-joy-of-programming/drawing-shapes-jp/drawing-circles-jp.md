# Drawing Circles

In this lesson, we'll learn how to write programs to draw circles on the
canvas.

{{ YouTubeVideo("oS-E_7XnQFo") }}

## Simple Circle

We'll start by drawing a circle. This involves two steps, creating a
circle and showing it.

```{.python .joy .example #one-circle}
c = circle()
show(c)
```

The first line creates a circle shape and the second line shows it.

Just like the `print` function is used to display numbers and strings,
the `show` function is used to display shapes.

## Controlling the Size

The size of the circle is controlled by its radius. By default, the
radius of the circle will be 100, but we can specify a different value
for the radius. The is done by setting the parameter `r`.

```{.python .joy .example #circle-with-radius}
c = circle(r=50)
show(c)
```

Try making the circle bigger by changing the value of parameter `r`.

!!! note "Named and positional arguments"

    You may have noticed that we are using the `circle` and
    the `show` functions very differently.

    We are calling the `show` function as `show(c)`, but the `circle`
    function as `circle(r=50)` and not as `circle(50)`.

    In Python, it is possible to pass arguments by name (like r=50, x=10 etc)
    and by position (like in `print(1, 2, 3)`).

    It is too early for us to get into those details. For now, just understand
    that both these ways are acceptable.

## More Circles

We can also create more than one circle. The following example draws
two concentric circles with radius `50` and `100`.

```{.python .joy .example #two-circles}
c1 = circle(r=50)
show(c1)

c2 = circle(r=100)
show(c2)
```

Just like `print`, the `show` function also supports taking multiple
arguments and we can use that to show multiple shapes at once.

```{.joy .example #two-circles}
c1 = circle(r=50)
c2 = circle(r=100)
show(c1, c2)
```

{{ Exercise("three-concentric-circles-jp") }}
