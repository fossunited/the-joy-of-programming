"""
start.py
~~~~~~~~

This script is the main entry point. This will be
executed whenever the run button is pressed, after
saving the code in the editor as main.py.

This executes the main.py after adding all the variables
and functions defined in the sketch.py to the executing
environment.
"""

from joy import *

def show_bg():
    def hline(y, **kwargs):
        return Line(start=Point(x=-150, y=y), end=Point(x=150, y=y), stroke="#ddd", **kwargs)

    def vline(x, **kwargs):
        return Line(start=Point(x=x, y=-150), end=Point(x=x, y=150), stroke="#ddd", **kwargs)

    markers = [
        hline(50), hline(100), hline(150),
        hline(-50), hline(-100), hline(-150),
        vline(50), vline(100), vline(150),
        vline(-50), vline(-100), vline(-150),
        hline(0, stroke_width=2), vline(0, stroke_width=2)
    ]
    shape = Group(markers)
    sendmsg("shape", shape=shape._svg())

BG_SHOWN = False

def show(*shapes):
    global BG_SHOWN
    if not BG_SHOWN:
        show_bg()
        BG_SHOWN = True

    for s in shapes:
        if not isinstance(s, Shape):
            print(f"show: {s} is not a shape")

    shapes = [s for s in shapes if isinstance(s, Shape)]
    shape = Group(shapes) | Scale(sx=1, sy=-1)
    sendmsg("shape", shape=shape._svg())

env = dict(globals())

import json
def sendmsg(msgtype, **kwargs):
  """Sends a message to the frontend.

  The frontend will receive the specified message whenever
  this function is called. The frontend can decide to some
  action on each of these messages.
  """
  msg = dict(msgtype=msgtype, **kwargs)
  print("--MSG--", json.dumps(msg))

code = open("main.py").read()
exec(code, env)
