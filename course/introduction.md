# Introduction to Programming

Welcome to the world of programming!

Programming is the craft of creating things using a computer. These things are sometimes useful and sometimes just fun.

Just like any other craft, programming is also a creative process. You need to think, imagine what you want to create. You need to master the skills. It requires a lot of delebrate practice.

In this course, we are going to use programming to make the computer draw sketches. Like these:

![](assets/images/gallery.png)

You can do a lot more than drawing sketches with a computer. We need to start somewhere and what is more fun than drawing sketches? Also, this approch makes it easier for us to spot our mistake easily as the result is a visual sketch.

Let's keep going!

## What do I need to know?

This course assume no prior programming experiece.

However, it is assumed that you are reasonbly good at doing simple math.

To tell the computer where to draw a shape and how big, you also need to know a bit of coordinate geometry. Don't worry if you don't know much, it will be explained in detail in one of the latter sessions.

## The Live Coding Environment

To make easy to get started we've built a live-coding environment. You just need write your program in the same web browser where you are reading this tutorial.

There will be examples like the one below and it allows run the program right here. Try clicking the Run button to draw the circle with center (100, 200) and diameter 50.

```
circle(100, 200, 50)
```

That is too small isn't it? How about making it slightly bigger? Can you try changing the diameter from 50 to 150 and see if the circle gets bigger?

Congratulations! You have written your first program.


We will understand

Don't worry

## What is happening?

<img src="images/circle.png">

Let's look at the program again:

```
circle(100, 200, 50)
```

The name `circle` that you see in the program is a _function_ to draw a circle and the three numbers that are next to it as the inputs to that function, called the _arguments_.

The circle function needs three arguments. The first argument is the x-coordinate of the center of the circle, indicating how far the center is from the left side of the canvas. The second argument is the y-coordinate of the center of the circle, indicating how far the center is from the top of the canvas.

The circle is towards to the left of the canvas. Try moving the circle to the right of the canvas by changing the first argument.


```
circle(100, 200, 50)
```

You could also try moving the circle vertically by changing the second argument and change the size of the circle using the last argument.

## Programming Languages

Computers are really stupid. They are not smart like people, but they are fast and don't get bored if we ask them to do the same thing again and again.

To explain a computer to do something is very tedious, they don't understand many things, they can't think on their own. So people have created new languages to speak to computers. They are called programming languages. When you write a program in a programming language, some other program converts it into a language that the computer understands.

Writing in a programming language is a lot better than writing the language the computer actually understands. But we need to learn the rules of that programming language.

The programming language that we are going to learn in this course is called Python. You'll see soon that Python is easy to learn and a lot of fun.
