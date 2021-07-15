# Hello, world!
<!-- FIELDS index_=2 index_label=1.2 -->

It is a tradition of programmers to write the first program to display the message _Hello, world!_.

Let's write our first program in Python to display that message.

```{.python .joy .example}
print("Hello, world!")
```

Click on the run button to execute the program. You should be able see the output below after you that.

The `print` is a function that takes a value as input and displays it on the screen. We've passed a text value `"Hello, world!"` as input to the `print` function.

The text values are called _strings_ in Python. Strings are enclosed either in double quotes of single quotes.

If you don't put quotes, then Python will complain. For example `print(hello)` will not work, but `print("hello")` will.

## Comments

While we write programs for the computer to perform some action, it is also equallly important to pay attention to make the program easy to understand for other people or even yourself.

Every programming language provides a way to write _comments_ in the code. Comments are notes that we write in the program, which are ignored by the computer, but they help people to understand what the program does or why the program was writen in that particular way.

In Python, comments start with `#` character. Everything from `#`  to the end of the line is considered as comment and is ignored by the computer.

The following example, the first two lines are comments.

```{.python .joy .example}
# Program to print Hello, world!
# Click on the "Run" button to execute this program

print("Hello, world!")
```

{{ Exercise("print-joy-jp") }}

## Hello, Joy!

Traditionally, programming is learnt by writing programs to manipulate numbers and text. To make this course more interesting, we'll be writing programs to create drawings. To make that possible, we have created a library called _[Joy](https://github.com/fossunited/joy)_, which is already included in the course environment.

Let's get a taste of _Joy_. The following is a simple example program written using _Joy_.

```{.python .joy .example}
# program to draw a circle
c = circle()
show(c)
```

When you run the program you'll see a circle at the center of a canvas.

The function `circle` is provide by the `Joy` library. It has many other functions for various shapes and doing some operations on them, which you'll see in the upcoming lessons.

{{ Exercise("draw-rectangle-jp") }}


