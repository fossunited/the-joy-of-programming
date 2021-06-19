# More Shapes

## The Rectangle and The Ellipse

Let's look at how to draw rectangle and ellipse shapes. As you could have
guessed, there are two new functions `rectangle` and `ellipse`.

```{.joy .example #rectangle}
s1 = rectangle()
s2 = ellipse()
show(s1, s2)
```

We could create a rectangle or an ellipse with different width and height
by specifying the parameters `w` and `h` respectively.

```{.joy .example #rectangle-wh}
s1 = rectangle(w=100, h=50)
s2 = ellipse(w=200, h=100)
show(s1, s2)
```

Both the rectangle and the ellipse are centered around the origin by
default. Just like with the `circle`, we can specify the center of the
shape by specifying parameters `x` and `y`.

```{.joy .example #rectangle-xy}
s1 = rectangle(x=0, y=-50, w=150, h=100)
s2 = ellipse(x=0, y=50, w=150, h=100)
show(s1, s2)
```

{{ Exercise("draw-a-square-jp") }}

{{ Exercise("two-concentric-squares-jp") }}

{{ Exercise("two-rectangles-jp") }}

{{ Exercise("two-ellipses-jp") }}

{{ Exercise("the-eye-jp") }}
