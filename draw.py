from ti_system import *
from ti_draw import *

class line:
  def __init__(self, x1, y1, x2, y2, name):
    self.x1=x1
    self.y1=y1
    self.x2=x2
    self.y2=y2
    self.name=name
  def draw(self):
    draw_line(self.x1,self.y1,self.x2,self.y2)
class rect:
  def __init__(self, x, y, width, height, name):
    self.x=x
    self.y=y
    self.width=width
    self.height=height
    self.name=name
  def draw(self):
    draw_rect(self.x,self.y,self.width,self.height)
#Define the clases later used to keep track of the shapes
#Draw the Canvas
def draw_canvas(lines, rectangles):
  for instance in lines:
    instance.draw()
  for instance in rectangles:
    instance.draw()

lines=[]
rectangles=[]
x1=0
y1=0
x2=0
y2=0
draw_line(0,0,0,0) #Initiate canvas
while get_key() != "esc":
  if get_key() == "a":
    while get_key() != "esc":
      draw_text(2,214,"Drawing Line")
      if get_key()== "center":
        if x1==0:
          print("First pos")
          x1=get_mouse()[0]
          y1=get_mouse()[1]
          draw_rect(x1,y1,1,1)
        else:
          print("Sec pos")
          x2=get_mouse()[0]
          y2=get_mouse()[1]
          name = "line" + str(len(lines) + 1)
          instance=line(x1,y1,x2,y2,name)
          lines.append(instance)
          x1=0
          y1=0
          x2=0
          y2=0
          clear()
          draw_canvas(lines, rectangles)
  if get_key() == "b":
    while get_key() != "esc":
      draw_text(2,214,"Drawing rectangle")
      if get_key()== "center":
        if x1==0:
          print("First pos")
          x1=get_mouse()[0]
          y1=get_mouse()[1]
          draw_rect(x1,y1,1,1)
        else:
          print("Sec pos")
          x2=get_mouse()[0]
          y2=get_mouse()[1]
          width=x1-x2
          height=y1-y2
          name = "rect" + str(len(lines) + 1)
          instance=line(x1,y1,width,height,name)
          rectangles.append(instance)
          x1=0
          y1=0
          x2=0
          y2=0
          width=0
          height=0
          clear()
          draw_canvas(lines, rectangles)
