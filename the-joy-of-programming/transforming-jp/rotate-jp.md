# Rotate

The rotate transformation rotates a shape around the origin by the specified angle in degrees.

The following example, rotates a line by 30 degrees anticlockwise.

```{.python .joy .example}
shape = line() | rotate(30)
show(shape)
```

Rotation is a great transformation that generates wonderful shapes very
easily.

```{.python .joy .example}
s1 = ellipse()
s2 = s1 | rotate(45)
s3 = s1 | rotate(90)
s4 = s1 | rotate(135)
show(s1, s2, s3, s4)
```

In the above example, we are taking an ellipse and rotating it by 45, 90
and 135 degrees respectively.

Another useful technique is to create a shape away from the origin and then rotate it.

```{.python .joy .example}
s1 = circle(x=100, y=0, r=10)
s2 = s1 | rotate(45)
s3 = s1 | rotate(90)
show(s1, s2, s3)
```

Instead of starting with primitive shapes, we could start with a compound
shape and apply multiple rotations to create surprising patterns.

```{.python .joy .example}
s1 = circle(x=50, y=0, r=50) + circle(x=75, y=0, r=25)
s2 = s1 | rotate(90)
s3 = s1 | rotate(180)
s4 = s1 | rotate(270)
show(s1, s2, s3, s4)
```

{{ Exercise("rotate-three-ellipses-jp") }}
{{ Exercise("rotate-three-circles-jp") }}
{{ Exercise("rotate-four-lines-jp") }}
