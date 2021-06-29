# Translate

Transformations are applied to shapes to make them move, rotate,
streach or squeeze.

The translate transformation moves the given shape by specified amount
in x and y directions.

```{.python .joy .example}
shape = circle(r=50) | translate(x=100, y=0)
show(shape)
```

The transformations are applied using the `|` operator. Just like the
`+` and `/` operators perform addition, division etc., the `|` operator
when used between a shape and transformation, applies the transformation to the shape.

The `translate` function create a transformation to move the given shape
by the specified `x` and `y` values.

The same program could be written as the following:

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

We could turn that into a reuseable function.

```{.python .joy .example}
def three_in_a_row(shape, width):
    left = shape | translate(x=-width, y=0)
    right = shape | translate(x=width, y=0)
    return left + shape + right

shape = three_in_a_row(circle(r=50), width=100)
show(shape)
```

Once we have the function, we could apply it to any shape.

```{.python .joy .example}
def three_in_a_row(shape, width):
    left = shape | translate(x=-width, y=0)
    right = shape | translate(x=width, y=0)
    return left + shape + right

shape = circle(r=50) + ellipse(w=100, h=50) + ellipse(w=50, h=100)
row = three_in_a_row(shape, width=100)
show(row)
```

{{ Exercise("translate-grid-jp") }}