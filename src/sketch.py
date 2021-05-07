import json
from time import sleep

def sendmsg(msgtype, function, args):
  """Sends a message to the frontend.

  The frontend will receive the specified message whenever
  this function is called. The frontend can decide to some
  action on each of these messages.
  """
  msg = dict(msgtype=msgtype, function=function, args=args)
  print("--MSG--", json.dumps(msg))

def _draw(func, **kwargs):
  sendmsg(msgtype="draw", function=func, args=kwargs)

def circle(x, y, d):
    """Draws a circle of diameter d with center (x, y).
    """
    _draw("circle", x=x, y=y, d=d)

def line(x1, y1, x2, y2):
    """Draws a line from point (x1, y1) to point (x2, y2).
    """
    _draw("line", x1=x1, y1=y1, x2=x2, y2=y2)

def rect(x, y, w, h):
    """Draws a rectangle on the canvas.

    Parameters
    ----------
    x: x coordinate of the top-left corner of the rectangle
    y: y coordinate of the top-left corner of the rectangle
    w: width of the rectangle
    h: height of the rectangle
    """
    _draw("rect", x=x, y=y, w=w, h=h)

def clear():
    _draw("clear")

# clear the canvas on start
clear()