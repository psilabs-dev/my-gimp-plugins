#!/usr/bin/env python

import os
import sys
sys.path.append(os.path.dirname(__file__))
from common import *

def add_double_outline(
		image, layer, 
		outline_color, grow_px, feather_px,
		outline_color_2, grow_px_2, feather_px_2,
):
	# first outline
	new_layer = add_new_layer_beneath(image, layer)
	create_selection(image, layer, grow_px=grow_px, feather_px=feather_px)
	fill_selection(new_layer, color=outline_color)
	pdb.gimp_selection_none(image)
	pdb.gimp_image_set_active_layer(image, layer)

	# second outline
	new_layer_2 = add_new_layer_beneath(image, new_layer)
	create_selection(image, new_layer, grow_px=grow_px_2, feather_px=feather_px_2)
	fill_selection(new_layer_2, color=outline_color_2)
	pdb.gimp_selection_none(image)
	pdb.gimp_image_set_active_layer(image, layer)
	
	return new_layer

register(
	"add_double_outline",	
	"Add outline Template",   
	"Function for adding two outlines below a layer.",
	"psilabs", 
	"psilabs", 
	"2023",
	"<Image>/Plugins/Add Double Outline", 
	"*", 
	[
		(PF_COLOUR, "outline_color", "Outline Color 1", (0, 0, 0)),
		(PF_INT, "grow_px", "Grow Size 1", 5),
		(PF_INT, "feather_px", "Feather Size 1", 0),
		(PF_COLOUR, "outline_color_2", "Outline Color 2", (0, 0, 0)),
		(PF_INT, "grow_px_2", "Grow Size 2", 5),
		(PF_INT, "feather_px_2", "Feather Size 2", 0),
	],
	[],
	add_double_outline)

main()