from ti_system import *
from ti_draw import *
x1=0
y1=0
x2=0
y2=0
draw_line(0,0,0,0)
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
          draw_line(x1,y1,x2,y2)
          x1=0
          y1=0
          x2=0
          y2=0
