#!/usr/bin/env python

import os
import sys
sys.path.append(os.path.dirname(__file__))
from common import *

def add_outline_to_image(image_path, output_image_path, outline_color):
    # add outlines to image based on various colors defined in color map.
    
    # operate on image
    image, layer = load_and_get_active_layer(image_path)
    add_outline_to_layer(image, layer, outline_color, 5, 30)
    merged = pdb.gimp_image_merge_visible_layers(image, CLIP_TO_IMAGE)

    # resolve image
    pdb.gimp_file_save(image, merged, output_image_path, output_image_path)
    pdb.gimp_image_delete(image)

def create_outlined_images(input_dir, output_dir, outline_color):
    # Walk through the directory structure
    if not os.path.exists(input_dir):
        return
    
    for file in list(filter(
        lambda filename: os.path.splitext(filename)>=2 and os.path.splitext(filename)[1]==".png", os.listdir(input_dir)
    )):
        image_file_path = os.path.join(input_dir, file)
        output_file_path = os.path.join(output_dir, file)
        add_outline_to_image(image_file_path, output_file_path, outline_color)

    pass

register(
    "create_outlined_images",
    "Create Outlined Images",
    "Add an outline to each image in a given directory and save it as a new image in the output directory.",
	"psilabs",
	"psilabs",
	"2023",
    "Create Outlined Images from a Directory",
    "",      # Leave this empty; this function doesn't operate on an opened image
    [
        (PF_DIRNAME, "input_dir", "Input Directory", ""),
        (PF_DIRNAME, "output_dir", "Output Directory", ""),
        (PF_COLOUR, "outline_color", "Outline Color", (0, 0, 0)),
    ],
    [],
    create_outlined_images, 
    menu="<Image>/Converter"
)

main()
