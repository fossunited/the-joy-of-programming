# Positioning Shapes

We've seen how to draw circles of different sizes. However, the circles were always centered at the origin.

In this lesson we are going to focus on how to specify the center of the circle to position it at different places on the canvas.

## The Canvas

When we write a program to show some shapes, those shapes are displayed in a small box and that is called the canvas. It is of size 300x300 pixels and the point (0, 0) is at the center of the canvas.

You may be wondering what is _pixels_. Just like we measure length of physical objects in centimeters and inches, we measure things shown on the screen in pixels. Pixels are the dots that make up the screen. Our canvas is a square with 300 pixels length.

TODO: place canvas image

## Positining the Circle

We can specify the center of the circle using the `x` and `y` parameters.

```{.joy .example}
c = circle(x=50, y=0)
show(c)
```

Let us try to draw two circles next to each other.

```{.joy .example}
c1 = circle(x=-50, y=0, r=50)
c2 = circle(x=50, y=0, r=50)
show(c1, c2)
```

Wasn't that simple? Let's try some exercises now.

{{ Exercise("three-circles-in-a-row-jp") }}
{{ Exercise("three-circles-in-a-column-jp") }}
{{ Exercise("grid-of-circles-jp") }}
{{ Exercise("four-circles-jp") }}
{{ Exercise("three-bottom-circles-jp") }}
{{ Exercise("three-bottom-circles-large-jp") }}
