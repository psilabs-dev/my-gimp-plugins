#!/usr/bin/env python

import os
import sys
sys.path.append(os.path.dirname(__file__))
from common import *

def add_outline(image, layer, outline_color, grow_px, feather_px):
	return add_outline_to_layer(image, layer, outline_color, grow_px, feather_px)

register(
	"add_outline",	
	"Add outline Template",   
	"Function for adding one outline below a layer.",
	"psilabs", 
	"psilabs", 
	"2023",
	"<Image>/Plugins/Add Outline", 
	"*", 
	[
		(PF_COLOUR, "outline_color", "Outline Color", (0, 0, 0)),
		(PF_INT, "grow_px", "Grow Size", 5),
		(PF_INT, "feather_px", "Feather Size", 0),
	],
	[],
	add_outline)

main()