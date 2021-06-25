# Combining Shapes

In the previous lessons, we've seen how to create many shapes and show
all of them. In this lesson we are going to see how to combine multiple
shapes into a single shape and how to use variables to capture the
relations between the shapes used to make a compound shape.

## Combining two Shapes

The `+` operator is used to join two shapes together.

``` {.python .example}
shape = circle(r=100) + rectangle(w=200, h=200)
show(shape)
```

In the above example, the shape is a compund shape by joining a circle
and a rectangle.

Now, let's try to create a donut by adding two circles.

``` {.python .example}
donut = circle(r=100) + circle(r=50)
show(donut)
```

The above example creates a donut shape using two circles, with the outer
circle of radius 100 and the inner circle of radius 50, exactly half of
the outer circle.

However, there is small issue with the above program. If we want to make
the donut bigger, we need to change the radius of the both the circles
while making sure that the radius inner circle is half of the outer circle.

Wouldn't it be better if change the number just once and the rest of it
is taken care automatically? In the next example, we'll see how to achieve
that using variables.

```{.python .joy .example}
r = 100
donut = circle(r=r) + circle(r=r/2)
show(donut)
```

The result of this program is exactly same as the previous program, but
now we can change the size of the donut a lot easier. We just need to
change just one number and everything else already captured in the program.

{{ Exercise("eye-with-variables-jp") }}

{{ Exercise("donut-again-jp") }}
