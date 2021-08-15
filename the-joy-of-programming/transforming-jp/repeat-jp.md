# Repeat

Repeat is a higher order transformation that takes a transformation and
applies it repeatedly to a shape and combines all the resulting shapes.

The following example repeatedly translates a circle 5 times.

```{.python .joy .example}
shape = circle(r=50) | repeat(5, translate(x=25))
show(shape)
```

Repeating rotate transformations creates very interesting patterns.

For example, the following rotates an ellipse three times.

```{.python .joy .example}
shape = ellipse() | repeat(3, rotate(60))
show(shape)
```

We could any shape and rotate repeated to created really amazing shapes.

```{.python .joy .example}
shape = rectangle(w=200, h=200) | repeat(9, rotate(10))
show(shape)
```

Or take a shape away from the origin and apply repeated rotation
to create interesting patterns.

```{.python .joy .example}
shape = circle(x=50, y=0, r=50) | repeat(6, rotate(60))
show(shape)
```

Or this one:

```{.python .joy .example}
shape = circle(x=125, y=0, r=10) | repeat(36, rotate(10))
show(shape)
```

It is lot more fun to repeat multiple transformations together.

```{.python .joy .example}
shape = rectangle(w=250, h=250) | repeat(60, rotate(10)|scale(0.9))
show(shape)
```

It gets really interesting if we tweak the angle of rotation and scale factor a bit.

```{.python .joy .example}
shape = rectangle(w=250, h=250) | repeat(60, rotate(5)|scale(0.92))
show(shape)
```

And how about a spiral?

```{.python .joy .example}
shape = circle(x=100, y=0, r=50) | repeat(36*4, rotate(10)|scale(0.97))
show(shape)
```

The above example, takes a circle scales it down while rotating to
create a spiral. We are using 10 degrees for each rotation and repeating
36*4 times to create a spiral with 4 revolutions.


```{.python .joy .example}
s = rectangle(x=100, y=0, w=25, h=25)
s = circle(x=140, y=0, r=10)
s1 = s | repeat(20, scale(0.85))
s2 = s1 | repeat(36, rotate(10))
show(s2)
```

## Exercises

Here are some interesting challenges for you.

{{ Exercise("repeat-rotate-square-jp") }}
{{ Exercise("repeat-rotate-line-jp") }}
{{ Exercise("repeat-half-rotate-line-jp") }}
{{ Exercise("repeat-cycle-ellipse-jp") }}
