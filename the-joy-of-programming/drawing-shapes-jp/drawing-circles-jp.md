# Drawing Circles

In this lesson, we'll learn how to write programs to draw circles on the
canvas.

## Simple Circle

We'll start with drawing a circle. This involves two steps, creating a
circle and showing it.

```{.joy .example #one-circle}
c = circle()
show(c)
```

The first line creates a circle shape and the secone line shows it.

## Controlling the Size

The size of the circle is controlled by its radius. By default, the
radius of the circle will be 100, but we can specify a different value
for the radius. The is done by setting the parameter `r`.

```{.joy .example #circle-with-radius}
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
    that both these ways are acceptible.

## More Circles

We can also create more than one circle. The following example draws
two conentric circles with radius `50` and `100`.

```{.joy .example #two-circles}
c1 = circle(r=50)
c2 = circle(r=100)
show(c1, c2)
```

The `show` function supports showing multiple shapes together.

{{ Exercise("three-concentric-circles-jp") }}
