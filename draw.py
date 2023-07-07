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
    print(self.x1,self.y1)
    draw_line(self.x1,self.y1,self.x2,self.y2)
class rect:
  def __init__(self, x, y, width, height, name):
    self.x=x
    self.y=y
    self.width=width
    self.height=height
    self.name=name
  def draw(self):
    print(self.x,self.y)
    draw_rect(self.x,self.y,self.width,self.height)
class full_rect:
  def __init__(self, x, y, width, height, name):
    self.x=x
    self.y=y
    self.width=width
    self.height=height
    self.name=name
  def draw(self):
    print(self.x,self.y)
    fill_rect(self.x,self.y,self.width,self.height)
#Define the clases later used to keep track of the shapes
#Draw the Canvas
def draw_canvas(lines, rectangles,full_rectangles):
  for instance in lines:
    instance.draw()
  for instance in rectangles:
    instance.draw()
  for instance in full_rectangles:
    instance.draw()

lines=[]
rectangles=[]
full_rectangles=[]
x1=0
y1=0
x2=0
y2=0
draw_line(0,0,0,0) #Initiate canvas
while get_key() != "esc":
  if get_key() == "a":
    draw_text(2,214,"Drawing Line")
    while get_key() != "esc":

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
          draw_canvas(lines, rectangles, full_rectangles)
          draw_text(2,214,"Drawing Line")
    clear()
    draw_canvas(lines,rectangles,full_rectangles)
  if get_key() == "b":
    draw_text(2,214,"Drawing rectangle")
    while get_key() != "esc":
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
          width=x2-x1
          height=y2-y1
          if width>0 or height>0:
            print("Unable to draw shape height or width negative")
          else:
            name = "rect" + str(len(lines) + 1)
            instance=rect(x1,y1,width,height,name)
            rectangles.append(instance)
          x1=0
          y1=0
          x2=0
          y2=0
          width=0
          height=0
          
          clear()
          draw_canvas(lines,rectangles,full_rectangles)
          draw_text(2,214,"Drawing rectangle")
    clear()
    draw_canvas(lines,rectangles)
  if get_key()=="c":
    draw_text(2,214,"Drawing filled rectangle")
    while get_key() != "esc":
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
          width=x2-x1
          height=y2-y1
          if width>0 or height>0:
            print("Unable to draw shape height or width negative")
          else:
            name = "rect" + str(len(lines) + 1)
            instance=full_rect(x1,y1,width,height,name)
            full_rectangles.append(instance)
          x1=0
          y1=0
          x2=0
          y2=0
          width=0
          height=0

          clear()
          draw_canvas(lines,rectangles,full_rectangles)
          draw_text(2,214,"Drawing filled rectangle")
    clear()
    draw_canvas(lines,rectangles,full_rectangles)
