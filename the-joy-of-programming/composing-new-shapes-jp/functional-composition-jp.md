# Functional Composition

<!-- FIELDS index_=2 index_label=6.2 -->

In this lesson, we are going to look at a new way of composing shapes, by using functions.

We'll start with defining two functions `beside` and `below`.
The `beside` functions take shapes and put them one next to each other and the `below` function takes two shapes and puts one below the other.

We'll see simple functions like these can be combined to create a lot more complicated patterns.

## The `beside` function

The _beside_ function takes two shapes and puts the first one in the left half and the second one in the right half.

<img src="/files/beside.svg" style="width: 50%"/>

Let's see what does it take to keep two shapes one beside the other. First, we need to squeeze both the shapes so that each one takes only half the width to be able to place both of them beside each other. Once the width is fixed, we need to move the shapes to the left and right respectively, and merge them.

<img src="/files/beside-details.svg" style="width: 50%"/>

Here is how it looks when we write that in code.

```{.python .joy .example}
def beside(a, b):
    a1 = a | scale(x=0.5) | translate(x=-75)
    b1 = b | scale(x=0.5) | translate(x=75)
    return a1 + b1

a = circle(r=100, fill="red")
b = rectangle(w=200, h=200, fill="blue")
shape = beside(a, b)
show(shape)
```

## The `below` function

The _below_ function takes two shapes and puts the first one in the top half and the second one in the bottom half.

<img src="/files/below.svg" style="width: 50%"/>

Just like we scaled and translated the shapes in the x-direction for `beside`, we need to do the same in the `y` direction for `below`.

<img src="/files/below-details.svg" style="width: 50%"/>


```{.python .joy .example}
def below(a, b):
    a1 = a | scale(y=0.5) | translate(y=75)
    b1 = b | scale(y=0.5) | translate(y=-75)
    return a1 + b1

a = circle(r=100, fill="red")
b = rectangle(w=200, h=200, fill="blue")
shape = below(a, b)
show(shape)
```

## Composing Functions

Now, let's see how to create interesting patterns by combining just these two functions `beside` and `below`.

### Example: Grid

Let's write a function `grid` that takes four shapes and puts them on a 2x2 grid.

It turns out that it is very easy to do it. We just need to put the first two and the last two beside each other and put the resulting shapes one below the other.

```text
def grid(a, b, c, d):
    return below(
        beside(a, b),
        beside(c, d))
```

Let's put all the code together.


```{.python .joy .example}
def beside(a, b):
    a1 = a | scale(x=0.5) | translate(x=-75)
    b1 = b | scale(x=0.5) | translate(x=75)
    return a1 + b1

def below(a, b):
    a1 = a | scale(y=0.5) | translate(y=75)
    b1 = b | scale(y=0.5) | translate(y=-75)
    return a1 + b1

def grid(a, b, c, d):
    return below(
        beside(a, b),
        beside(c, d))

a = circle()
b = rectangle()
c = ellipse()
d = line()
shape = grid(a, b, c, d)
show(shape)
```

{{ Exercise("functions-cycle-jp") }}
{{ Exercise("functions-repeat4-jp") }}
{{ Exercise("functions-repeat16-jp") }}
{{ Exercise("functions-repeat64-jp") }}

### Example: Right Split

Let's try something more interesting. How about writing a program to make the following pattern.

<img src="/files/right-split.svg" style="width: 50%"/>

Let's examine the pattern. The following figure shows the pattern in 3 levels.

<img src="/files/right-split-details.svg" style="width: 50%"/>

The level-1 pattern is the shape and a blank put beside each other. The level-2 pattern is made of the shape and two level-1 patterns and the level-3 pattern is made of the shape and two level-2 patterns.

That looks like an interesting pattern. Isn't it? Now, let's put that in code.

First, we need a blank shape. We can cheat by creating a circle with no stroke. There will be a shape, but it won't appear.

```text
blank = circle(fill="none")
```

To make a level-1 split, we need to put the shape and a blank together.

```text
split1 = beside(shape, blank)
```

To make a level-2 split, we need to take the split1, put one below the other, and put it beside the original shape.

```text
split2 = beside(shape, below(split1, split1))
```

And that goes on.

Let's combine all of this and see.

```{.python .joy .example}
def beside(a, b):
    a1 = a | scale(x=0.5) | translate(x=-75)
    b1 = b | scale(x=0.5) | translate(x=75)
    return a1 + b1

def below(a, b):
    a1 = a | scale(y=0.5) | translate(y=75)
    b1 = b | scale(y=0.5) | translate(y=-75)
    return a1 + b1

shape = circle(fill="gray")
blank = circle(stroke="none")
split1 = beside(shape, blank)
split2 = beside(shape, below(split1, split1))
split3 = beside(shape, below(split2, split2))
split4 = beside(shape, below(split3, split3))
show(split4)
```

The circle has become an ellipse because it got stretched when be put beside the other shapes. We could fix it by putting it below a blank shape.

```{.python .joy .example}
def beside(a, b):
    a1 = a | scale(x=0.5) | translate(x=-75)
    b1 = b | scale(x=0.5) | translate(x=75)
    return a1 + b1

def below(a, b):
    a1 = a | scale(y=0.5) | translate(y=75)
    b1 = b | scale(y=0.5) | translate(y=-75)
    return a1 + b1

shape = circle(fill="gray")
blank = circle(stroke="none")
split1 = beside(shape, blank)
split2 = beside(shape, below(split1, split1))
split3 = beside(shape, below(split2, split2))
split4 = beside(shape, below(split3, split3))

final = below(blank, split4)
show(final)
```

{{ Exercise("functions-top-split-jp") }}
