# Adding Colors

So far, we've drawn different shapes, but all of them were just
_black_ and _white_. Wouldn't it be fun to add some colors to our sketches?

In this lesson we'll learn how to specify the fill color, the stroke color
and the stoke width.

## The Fill Color

The optional argument `fill` can be used to specify the color to fill
the shape with.

```{.joy .example}
c = circle(fill="pink")
show(c)
```

Notice that the value `"pink"` is put in quotes. That is because we are
specifying the value of the color as a string.

There are many colors with standard names. These include _black_, _white_,
_gray_, _red_, _blue_, _green_, _yellow_, _maroon_, _purple_, _pink_ and
[many more](https://en.wikipedia.org/wiki/Web_colors).

We can also specify the fill as `"none"`, if we don't want to fill
anything, which the default behavior.

One important thing to remember when using `fill` is that the order of
drawing shapes matter.

```{.joy .example}
c1 = circle(fill="pink")
c2 = circle(x=50, fill="purple")
show(c1, c2)
```

As you can see the purple circle is being drawn on top of the pink circle.
The shapes are drawn in the order they are passed to the `show` function.
Can you try to make the pink circle come on top of the purple circle?

## The Stroke Color

The stroke color specifies the color used to draw the outline of a shape.
It can be specified for a shape by using the optional argument `stroke`.

```{.joy .example}
r = rectangle(stroke="blue")
show(r)
```

We can also use _stoke_ and _fill_ together.

```{.joy .example}
r = rectangle(stroke="red", fill="yellow")
show(r)
```

We can specify stroke as `none` to skip drawing the outline.

```{.joy .example}
c1 = circle(r=150, fill="green", stroke="none")
c2 = circle(r=100, fill="blue", stroke="none")
c3 = circle(r=50, fill="red", stroke="none")
show(c1, c2, c3)
```

## The Stroke Width

The width of the outline can be specified using the optional argument
`stroke_width`.

```{.joy .example}
c1 = circle(r=25, stroke_width=1)
c2 = circle(r=50, stroke_width=2)
c3 = circle(r=75, stroke_width=3)
c4 = circle(r=100, stroke_width=4)
c5 = circle(r=125, stroke_width=5)
show(c1, c2, c3, c4, c5)
```

{{ Exercise("red-black-squares-jp") }}

{{ Exercise("three-overlapping-squares-jp") }}

## Web Colors

The standard colors are very often not sufficient for creative minds.
People who is need finer control over the colors specify the color
using their RGB values standing for the red, the green and the blue
components of a color. A common way to specify that is using a
hexadecimal format, like `#138808`. It has 6 characters after the `#`
symbol, 2 characters each for red, green and blue respectively.

Don't worry about how to create colors using that. We usually don't. We
just pick a color code by [searching for color picker](https://duckduckgo.com/?q=color+picker)
or from a one of the many websites on the web.

Now that we know how grab wonderful colors from the web, let's see how to
use them in our programs. How about creating a circle filled with _PeachPuff_ with a
_Tomato_ outline? Yes, _PeachPuff_ and _Tomato_ are the names of two standard colors.

```{.joy .example}
c = circle(fill="PeachPuff", stroke="Tomato", stroke_width=10)
show(c)
```

Now, try's use their hexadecimal color codes instead of their names. The
[wikipedia page about web colors](https://en.wikipedia.org/wiki/Web_colors)
has many colors like these.

```{.joy .example}
c = circle(fill="#FFDAB9", stroke="#FF6347", stroke_width=10)
show(c)
```

As you could notice, both the examples above get exactly the same result.

One thing to remember is that when you writing color names or the hexadecimal color codes
the case of the letters doesn't matter. Using `#FFDAB9` or `#ffdab9` have
the same effect and `"Tomato"` or `tomato` will the same too.

Also, remember that you need to put quotes around the color name of the
color code like `"Tomato"` or `"#FF6347"` because they are represented as
strings in our programs.

## Making Flags

Let's have some fun creating flags of various countries.

The flag of Germany looks like the following:

{{ Image("image-flag-of-germany-jp") }}

It is made of three colors _black_, _red_ and _gold_ colors. Let's see how to write code
to draw that flag.

```{.joy .example}
r1 = rectangle(x=0, y=100, w=300, h=100, fill="black", stroke="none")
r2 = rectangle(x=0, y=0, w=300, h=100, fill="red", stroke="none")
r3 = rectangle(x=0, y=-100, w=300, h=100, fill="gold", stroke="none")
show(r1, r2, r3)
```


{{ Exercise("flag-of-italy-jp") }}
{{ Exercise("flag-of-the-netherlands-jp") }}

### More Flags

Can you search the web for flags of various countries and create sketches
for them? Their wikipedia pages usually have the color codes.

You could try creating the flag of [Russia][] or [France][] or even [Japan][]. Why stop at three? Can do you 10 flags?

[Russia]: https://en.wikipedia.org/wiki/Flag_of_Russia
[France]: https://en.wikipedia.org/wiki/Flag_of_France
[Japan]: https://en.wikipedia.org/wiki/Flag_of_Japan
