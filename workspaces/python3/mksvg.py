import svgwrite
from svgwrite import *
from math import pi, sin
from sortedcontainers import SortedDict
import numpy as np
#this will work with svgwrite

height=30
width=90

lightest=0xaa # light grey
darkest=0x05 # dark greay
lighting_angle = 0.25 * pi # above the horizontal

def grayscale(val):
    return f"rgb('{val:x}', '{val:x}', '{val:x}')"

def gradient(height):
    color_range = lightest - darkest
    color_offset = darkest
    colors = SortedDict()
    for theta in np.linspace(0, pi, height):

        # where between lightest and darkes does this point fall?
        ratio = sin(theta + lighting_angle)
        color_ratio = int(ratio * color_range)

        # if darker than darkest, just stay darkest
        if color_ratio < 0:
            color_ratio = 0
        print(color_ratio)

        colors[theta] = grayscale(color_offset + color_ratio)
    return colors

svg_doc = svgwrite.Drawing(filename = "test-svgwrite.svg",
                                size = (width, height))


def add_nut(offset):
    (_, top_plane, front_plane, bottom_plane, _) = gradient(5).values()
    print(top_plane, front_plane, bottom_plane)

    svg_doc.add(svg_doc.rect(insert = (offset, 0),
        size = ("10px", "9px"),
        fill = top_plane))

    svg_doc.add(svg_doc.rect(insert = (offset, 9),
        size = ("10px", "12px"),
        fill = front_plane))


    svg_doc.add(svg_doc.rect(insert = (offset, 21),
        size = ("10px", "9px"),
        fill = bottom_plane))

add_nut(5)

print(svg_doc.tostring())
svg_doc.save()

val = 123456
f"0x{val:x}"
'0x1e240'

