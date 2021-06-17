import cairo
import cairofunctions
import math

w = 545
h = 390
ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h)
cr = cairo.Context(ims)
cf = cairofunctions.Context(cr, w, h)

# Initial Vectors
ORIGIN = cairofunctions.Point(w/2, h/2)
i = cairofunctions.Point(w/22,0)
j = cairofunctions.Point(0,-w/22)

cg = cairofunctions.CoordinateGrid(cr, w, h, ORIGIN, i, j)
ct = cairofunctions.Transform(i,j)

# Paint Screen Black
cr.set_source_rgb(255,255,255)
cr.paint()

cr.set_source_rgba(0.5,0.5,0.5,0.5)
cg.DrawGridLinesX()
cg.DrawGridLinesY()

cr.set_source_rgb(0.2,0.2,0.2)
cg.DrawAxes()
cg.DrawGridMarks(0.2)

# Generate Slope Field.
cr.set_source_rgb(0,0,1)

for y in range(-7, 8):
    for x in range(-11,12):
        try:
            m = x*x/30
            cg.PlotFuncYLim(lambda a:m*(a-x) + y, x-0.25, x+0.25, y-0.25, y+0.25)
        except ZeroDivisionError:
            p1 = ct*cairofunctions.Point(x, y -0.25) + ORIGIN
            p2 = ct*cairofunctions.Point(x, y+0.25) + ORIGIN
            cr.move_to(p1.x, p1.y)
            cr.line_to(p2.x,p2.y)
            cr.stroke()

cr.set_line_width(0.8)
cr.set_source_rgb(1,0.2,0.2)
cg.PlotFunc(lambda x: (x**3)/90, -11, 11)

cr.set_source_rgb(0.2,0.7,0.2)
cg.PlotFunc(lambda x: (x**3)/90 + 1, -11, 11)

cr.set_source_rgb(0.6,0.2,0.6)
cg.PlotFunc(lambda x: (x**3)/90 -1, -11, 11)

# Box at the Corner
p1 = ct*cairofunctions.Point(5,8) + ORIGIN
p2 = ct*cairofunctions.Point(11,8) + ORIGIN
p3 = ct*cairofunctions.Point(11,4) + ORIGIN
p4 = ct*cairofunctions.Point(5,4) + ORIGIN

cr.set_line_width(1)
cf.Polygon(p1,p2,p3,p4)
cr.set_source_rgba(0,0,0,0.3)
cr.fill_preserve()
cr.set_source_rgb(0,0,0)
cr.stroke()

ims.write_to_png("img.png")
