# Lines and Polygons

In this lesson we'll see how to draw lines and polygons.

## Line

Let's look at how to draw a line.

```{.python .joy .example}
k = line()
show(k)
```

The above example draws a horizontal line connecting points (-100, 0)
and (100, 0).


We can also specify the coordinates of both the start and end points.

```{.python .joy .example}
k = line(x1=0, y1=0, x2=100, y2=100)
show(k)
```

The above example, draws a line from point (0, 0) to point (100, 100)

If we want to draw a triangle, we can do that by drawing three lines.

```{.python .joy .example}
x1, y1 = 0, 0
x2, y2 = 100, 0
x3, y3 = 0, 100

k1 = line(x1, y1, x2, y2)
k2 = line(x2, y2, x3, y3)
k3 = line(x3, y3, x1, y1)
show(k1, k2, k3)
```

## Polygon

As you could have seen in the previous example, it is get cumbersome
to draw polygons using just lines. The `polygon` function is a better
way to create polygons.

The `polygon` function takes a list of points as argument and returns
a polygon shape.

```{.python .joy .example}
p1 = point(x=0, y=0)
p2 = point(x=100, y=0)
p3 = point(x=0, y=100)

shape = polygon([p1, p2, p3])
show(shape)
```