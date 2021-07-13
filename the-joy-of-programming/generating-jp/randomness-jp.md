# Randomness

All the sketches that we have created so far are quite structured. But too much order like that gets boring. They feel a bit artificial and we don't get a natural feel.

Most things in the nature has an element of randomness to it. Every branch of a tree doesn't have a fixed number of leaves. That variation, that randomness is pleasing.

In this lesson, we'll see how to generate random numbers and usem to create shapes of random size and position.

## Random Numbers

The Joy library has a function `random` to generate random numbers.

It can be used in three different ways:

* `random()` - returns a random number between `0` and `1`
* `random(n)` - returns a random number between `0` and `n`
* `random(a, b)` - returns a random number between `a` and `b`

Let's try it out:

```{.python .joy .example}
print(random())
print(random(10))
print(random(5, 10))
```

You may have a run it multiple times to get a sense of the spread of the values.

Sometimes, we want to work with just integers and we could use the `round` or the `int` function to convert the floating-point number to an integer.

The `round` function round off the value to the nearest integer while the `int` function trucates the decimal part.

```{.python .joy .example}
print("round(2.3) -> ", round(2.3))
print("int(2.3) -> ", int(2.3))
print("round(2.7) -> ", round(2.7))
print("int(2.7) -> ", int(2.7))
```

If the decimal value is less than 0.5 then both `round` and `int` return the same result and different numbers when the decimal part is greater than or equal to 0.5.

## Random Circles

Let's draw circle at random.

```{.python .joy .example}

def random_circle():
    x = random(-150, 150)
    y = random(-150, 150)
    r = random(50)
    return circle(x=x, y=y, r=r)

for i in range(20):
    c = random_circle()
    show(c)
```

The `random_circle` function doesn't take any arguments, but returns a circle at random x and y coordinates and the radius. We are calling the `random_circle()` function a loop to draw 20 circles.

## Random Colors

It would be fun to add generate colors also at random. The `joy` library has a function `color` to make a color from the RGB values.

The function takes three values for red, green and blue components of the color. Each value can have any value in the range 0 to 255.

```{.python .joy .example}
red = color(r=255, g=0, b=0)
c = circle(fill=red, stroke="none")
show(c)
```

You can check the [wikipedia page for web colors](https://en.wikipedia.org/wiki/Web_colors) for the RGB values for standard colors.

We can also specify an optional argument `a` to specify the alpha value for transparency. The alpha of 0 means it is completely transparent and alpha of 1 means completely opaque. We can try various alpha values to generate interesting patterns.

```{.python .joy .example}
fill_red = color(r=255, g=0, b=0, a=0.5)
fill_green = color(r=0, g=255, b=0, a=0.5)

c1 = circle(x=-50, y=0, r=100, fill=fill_red)
c2 = circle(x=50, y=0, r=100, fill=fill_green)
show(c1, c2)
```

Let's try the above example with random colors.

```{.python .joy .example}
def random_color():
    r = random(255)
    g = random(255)
    b = random(255)
    return color(r=r, g=g, b=b)

c1 = circle(x=-50, y=0, r=100, fill=random_color())
c2 = circle(x=50, y=0, r=100, fill=random_color())
show(c1, c2)
```

In the above example, the `random_color` function returns a random color. So, we get two circles with random colors.

It would be interesting to add transparency to our colors. In the following example, we are going to set the alpha value to 0.5 to make the color transparent.

```{.python .joy .example}
def random_color():
    r = random(255)
    g = random(255)
    b = random(255)
    return color(r=r, g=g, b=b, a=0.5)

c1 = circle(x=-50, y=0, r=100, fill=random_color())
c2 = circle(x=50, y=0, r=100, fill=random_color())
show(c1, c2)
```

Random colors with transparency is an interesting technique and we'll use that a lot in the comming lessons.

## Exercises

{{ Exercise("random-lines-jp") }}
{{ Exercise("random-colored-lines-jp") }}
{{ Exercise("random-colored-lines-with-transparency-jp") }}
{{ Exercise("random-colored-circles-jp") }}