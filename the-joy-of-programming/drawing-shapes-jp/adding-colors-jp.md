# Adding Colors

So far, we've drawn different shapes, but all of them were just
black and white. Wouldn't it be fun to add some colors to our sketches?

In this lesson we'll learn how to specify the fill color, the stroke color
and the stoke width.

## The Fill Color

The optional argument `fill` can be used to specify the color to fill
the shape with.

```
c = circle(fill="pink")
show(c)
```

Notice that the value `"pink"` is put in quotes. That is because we are
specifying the value of the color as a string.

There are many colors with standard names. These include _black_, _white_,
_gray_, _red_, _blue_, _green_, _yellow_, _maroon_, _purple_, _pink_ and
[many more](https://en.wikipedia.org/wiki/Web_colors).

<!-- We can also specify color using the red, blue and green (RGB) componnets
of the color and it is even possible to specify transparency. We'll see
them in the latter sections of this lesson. -->

We can also specify the fill as `"none"`, if we don't want to fill
anything, which the default behavior.

One important thing to remember when using `fill` is that the order of
drawing shapes matter.

```
c1 = circle(fill="pink")
c2 = circle(x=50, fill="purple")
show(c1, c2)
```

As you can see the rectangle is being drawn on top of the circle.
Change the `show(c1, c2)` to `show(c2, c1)` and see what happens.

## The Stroke Color

The stroke color specifies the color used to draw the outline of a shape.
It can be specified for a shape by using the optional argument `stroke`.

```
r = rectangle(stroke="blue")
show(r)
```

We can also use _stoke_ and _fill_ together.

```
r = rectangle(stroke="red", fill="yellow")
show(r)
```

We can specify stroke as `none` to skip drawing the outline.

```
c1 = circle(r=150, fill="green", stroke="none")
c2 = circle(r=100, fill="blue", stroke="none")
c3 = circle(r=50, fill="red", stroke="none")
show(c1, c2, c3)
```

## The Stroke Width

The width of the outline can be specified using the optional argument
`stroke_width`.

```
c1 = circle(r=25, stroke_width=1)
c2 = circle(r=50, stroke_width=2)
c3 = circle(r=75, stroke_width=3)
c4 = circle(r=100, stroke_width=4)
c5 = circle(r=125, stroke_width=5)
show(c1, c2, c3, c4, c5)
```

{{ Exercise("red-black-squares-jp") }}

{{ Exercise("three-overlapping-squares-jp") }}
