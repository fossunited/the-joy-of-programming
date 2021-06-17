# Positioning Shapes


We've seen how to draw different shapes and working with points and lines in the previous lessons. In this lesson we are going to focus on how to specify position of a shape on the canvas.

Most of the the shapes support specifying the center point when creating the shape. By default, the center is the origin, but we can specify a different point.

```{.python .joy .example #two-circles-in-a-row}
p1 = Point(x=0, y=0)
c1 = Circle(center=p1, radius=50)

p2 = Point(x=100, y=0)
c2 = Circle(center=p2, radius=50)

show(c1, c2)
```

In the above example, we have drawn a circle with (0, 0) as the center and another circle with (100, 0) as the circle.

We can specify the center for Ellipse and Rectangle as well.

```{.python .joy .example #rect-with-center}
p = Point(x=0, y=50)

s1 = Rectangle(center=p, width=200, height=100)
s2 = Ellipse(center=p, width=200, height=100)

show(s1, s2)
```

Wasn't that simple? Let's try some exercises now.

{{ Exercise("three-circles-in-a-row-jp") }}
{{ Exercise("three-circles-in-a-column-jp") }}
{{ Exercise("grid-of-circles-jp") }}
{{ Exercise("four-circles-jp") }}

