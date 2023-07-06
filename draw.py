from ti_system import *
from ti_draw import *

draw_line(0,0,0,0)
while get_key() != "esc":
	if get_key()== "center":
		if not x1==0:
			x1=get_mouse()[0]
			y1=get_mouse()[1]
		else:
			x2=get_mouse()[0]
			y2=get_mouse()[1]
			draw_line(x1,y1,x2,y2)
			x1=0
			y1=0
			x2=0
			y2=0
