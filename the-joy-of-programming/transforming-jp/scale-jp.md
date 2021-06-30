# Scale

The scale transformation resizes a shape by scaling it up or down.

The following example, resizes the circle by half.

```{.python .joy .example}
c1 = circle(r=100)
c2 = c1 | scale(0.5)
show(c1, c2)
```

You may notice that the inner circle is looking thinner. That is because
the scale transformation scales even the stroke width.

It is also possible to specify different scaling factor in x and y
directions. The following example, resizes the shape by half vertically
but keeps the same size in the horizontal direction.

```{.python .joy .example}
c1 = circle(r=100)
c2 = c1 | scale(x=1, y=0.5)
show(c1, c2)
```

We could omit the dimension when the scale is 1.
The expressions `scale(x=1, y=0.5)` and `scale(y=0.5)` would mean the same.

If we take a shape not centered around the origin and scale it, even
the distance from the origin gets scaled in the same proportion.

```{.python .joy .example}
c1 = circle(x=50, y=0, r=10)
c2 = c1 | scale(2)
show(c1, c2)
```

## Flipping

We can also apply negative scaling to flip a shape.

Let's try to make a mirror image. The mirror image flips the image vertically.
To flip vertically, the stuff on the right need to move to the left and vice versa.
Which means we need to change the x-coordinates. It may sound counter intutive,
but you need to `scale(x=-1)` to flip it vertically.

Let's start with the original shape.

```{.python .joy .example}
s1 = circle(x=100, y=100, r=50) + line(x1=-25, y1=-25, x2=100, y2=100)
show(s1)
```

Now let's make a mirror image of that by flipping vertically.

```{.python .joy .example}
s1 = circle(x=100, y=100, r=50) + line(x1=-25, y1=-25, x2=100, y2=100)
s2 = s1 | scale(x=-1)
show(s2)
```

How about flipping horizontally?

```{.python .joy .example}
s1 = circle(x=100, y=100, r=50) + line(x1=-25, y1=-25, x2=100, y2=100)
s2 = s1 | scale(y=-1)
show(s2)
```

We could even flip in both directions.

```{.python .joy .example}
s1 = circle(x=100, y=100, r=50) + line(x1=-25, y1=-25, x2=100, y2=100)
s2 = s1 | scale(x=-1, y=-1)
show(s2)
```

{{ Exercise("scale-concentric-circles-jp") }}