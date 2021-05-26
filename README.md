# The Joy of Programming

This repostory contains the course contents and notes for the Joy of Programming course.

The Joy of programming course is offered on [Mon School][], an initative of FOSS United.

[Mon School]: https://mon.school/

## Overview

_The Joy of Programming_ is a course to introduce the ideas of programming to beginners.

This course introduces the foundational ideas of programming using creative coding as a medium. The students will learn programming by writing programs to create various sketches. Python programming language is used for this course.

This course uses a [livecoding environment][livecode] that allows drawing skeches in the browser. The same envionment is integrated into the course notes so that the examples in the code can be tried out in the browser.

[livecode]: https://github.com/fossunited/livecode

## Tools

These notes are written in markdown and are built using [mkdocs for matetial][1].

[1]: https://squidfunk.github.io/mkdocs-material/

## Build Instructions

To build the docs:

```
$ make
```

It generated the output in `site/` directory.

To serve the docs:

```
$ make serve
```

and open the url http://localhost:8888/

## License

The contents of this repository are licensed under [CC BY-NC-SA 3.0][2].

[2]: https://creativecommons.org/licenses/by-nc-sa/3.0/