# Drawing Lines

We've seen how to draw simple shapes in the previous lesson. In this lesson we'll understand the coordinate system a bit and look at how to draw lines by specifying the start and end points.

Remember that the canvas is of size (300, 300) with the origin at the center.

We can use the `Line` function to create a line. By default, it creates a horizontal line of length 200 center around the origin. 
```{.python .joy .example #circle-with-center}
z = Line()
show(z)
```

We can also specify the `start` and `end` points when creating a line. For that we first need to creat points. The following example creates two points `p1` and `p2` and draws a line between them.

```{.python .joy .example #circle-with-center}
p1 = Point(x=0, y=0)
p2 = Point(x=100, y=100)

z = Line(start=p1, end=p2)
show(z)
```
As you can see a point is created by calling `Point` with `x` and `y` arguments.

### Example: Triangle

Let's try to draw a simple triangle.

```{.python .joy .example #circle-with-center}
p1 = Point(x=-100, y=0)
p2 = Point(x=100, y=0)
p3 = Point(x=0, y=100)

z1 = Line(start=p1, end=p2)
z2 = Line(start=p2, end=p3)
z3 = Line(start=p3, end=p1)

show(z1, z2, z3)
```

Let us looks an example of drawing lines along with other shapes.

### Example: Diagonals of a Rectangle

Let's draw a rectangle and both of it's diagonals. First we need to
find all the points so that we can specify the points to draw the lines.

```{python .joy .example #rect-diagonals}
p1 = Point(x=100, y=50)
p2 = Point(x=-100, y=50)
p3 = Point(x=-100, y=-50)
p4 = Point(x=100, y=-50)

s1 = Rectangle(width=200, height=100)
s2 = Line(start=p1, end=p3)
s3 = Line(start=p2, end=p4)
show(s1, s2, s3)
```

As you can notice, we've created all the points first and the created the
shapes. While it is possible to specify the points direcly when creating
the line, organizing code like this makes the program to easy to understand
and make changes.

The empty line seperating the points and shapes also very important. It
helps to see that the code has two part. The first part we are defining
the points and in the second part we are drawing the shapes. Remember
that clarity of the program is as important as correctness.

{{ Exercise("square-in-a-circle-jp") }}
