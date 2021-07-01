# Translate

Transformations are applied to shapes to make them move, rotate,
streach or squeeze.

The translate transformation moves the given shape by specified amount
in x and y directions.

The following example, moves a circle at the center towards right by 100
pixels.

```{.python .joy .example}
shape = circle(r=50) | translate(x=100, y=0)
show(shape)
```

The transformations are applied using the `|` operator. Just like the
`+` and `*` operators perform addition, multiplication etc., the `|` operator
when used between a shape and a transformation, applies the transformation
to the shape.

The `translate` function create a transformation to move the given shape
by the specified `x` and `y` values.

The same program could also be written as the following:

```{.python .joy .example}
c = circle(r=50)
right_100 = translate(x=100, y=0)
shape = c | right_100
show(shape)
```

Just like the `circle` function creates a shape, the `translate`
function creates a transformation and we use the `|` operator apply a
transformation to a shape.

Applying a transformation creates a new shape without modifying the
original shape. We could create a shape and apply different transformations.

```{.python .joy .example}
c1 = circle(r=50)
c2 = c1 | translate(x=100, y=0)
c3 = c1 | translate(x=-100, y=0)
show(c1, c2, c3)
```

We could start with slightly more interesting shape and apply the
same transformations.

```{.python .joy .example}
s1 = circle(r=50) + ellipse(w=100, h=50) + ellipse(w=50, h=100)
s2 = s1 | translate(x=100, y=0)
s3 = s1 | translate(x=-100, y=0)
show(s1, s2, s3)
```

{{ Exercise("translate-five-circles-jp") }}
{{ Exercise("translate-grid-jp") }}
{{ Exercise("translate-grid-of-donuts-jp") }}