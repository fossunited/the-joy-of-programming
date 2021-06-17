# Drawing Simple Shapes


Let's see some of the basic shapes available. Let's start with drawing
a circle.

```{.joy .example #one-circle}
c = circle()
show(c)
```

By default, the radius of the circle is 100, but we can specify a
different value for radius. The is done by setting the parameter `r`.

```{.joy .example #circle-with-radius}
c = circle(r=50)
show(c)
```

We can also create more than one circle.

```{.joy .example #two-circles}
c1 = circle(r=100)
c2 = circle(r=50)
show(c1, c2)
```

The `show` function supports showing multiple shapes together.

We could also try creating a rectangle or an ellipse.

```{.joy .example #rectangle-ellipse}
s1 = rectangle()
s2 = ellipse()
show(s1, s2)
```

We can specify the `width` and `height` of a rectangle.

```{.joy .example #rectangle-ellipse-2}
s1 = Rectangle(width=250, height=200)
s2 = Ellipse(width=100, height=200)
show(s1, s2)
```

{{ Exercise("draw-a-square-jp") }}

{{ Exercise("two-concentric-squares-jp") }}

{{ Exercise("two-rectangles-jp") }}

{{ Exercise("two-ellipses-jp") }}

{{ Exercise("the-eye-jp") }}

{{ Exercise("three-concentric-circles-jp") }}



