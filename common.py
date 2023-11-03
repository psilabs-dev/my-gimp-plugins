from gimpfu import *
import os

def add_new_layer_beneath(image, layer, layer_name=None):
	# Get the layer position.
	position = pdb.gimp_image_get_item_position(image, layer)
	parent_layer = layer.parent
	
	if image.base_type is RGB:
		type = RGBA_IMAGE
	else:
		type = GRAYA_IMAGE

	if layer_name is None:
		layer_name = "Outline for %s" % (layer.name)
		
	# Add a new layer below the selected one
	new_layer = gimp.Layer(image, layer_name, image.width, image.height, type, 100, NORMAL_MODE)
	pdb.gimp_image_insert_layer(image, new_layer, parent_layer, position+1)
	return new_layer

def create_selection(image, layer, grow_px=None, feather_px=None):
	# create selection from the layer's alpha channel.

	if grow_px is None:
		grow_px = 5
	if feather_px is None:
		feather_px = 0

	pdb.gimp_selection_layer_alpha(layer)
	pdb.gimp_selection_grow(image, grow_px)
	
	if feather_px is not None and feather_px > 0:
		pdb.gimp_selection_feather(image, feather_px)

	return

def fill_selection(layer, color=None):
	if color is None: # choose foreground color by default.
		color = pdb.gimp_palette_get_foreground()
	
	fg = pdb.gimp_palette_get_foreground() # cache foreground
	pdb.gimp_palette_set_foreground(color)
	pdb.gimp_bucket_fill(layer, 0, 0, 100, 0, 0, 1, 1)
	pdb.gimp_palette_set_foreground(fg)

	return

def add_outline_to_layer(image, layer, outline_color, grow_px, feather_px):
	# adds outline to selected layer by alpha channel with color
	# grow and feather refer to fill selection

	new_layer = add_new_layer_beneath(image, layer)
	create_selection(image, layer, grow_px=grow_px, feather_px=feather_px)
	fill_selection(new_layer, color=outline_color)
	pdb.gimp_selection_none(image)
	pdb.gimp_image_set_active_layer(image, layer)
	
	return new_layer

def load_and_get_active_layer(image_path):
	image = pdb.gimp_file_load(image_path, image_path)
	active_layer = pdb.gimp_image_get_active_layer(image)
	return (image, active_layer)

def convert_xcf_to_png(filename, output_dir):
	img = pdb.gimp_file_load(filename, filename)
	new_name = os.path.join(output_dir, os.path.splitext(os.path.basename(filename))[0] + ".png")
	layer = pdb.gimp_image_merge_visible_layers(img, CLIP_TO_IMAGE)
	pdb.gimp_file_save(img, layer, new_name, new_name)
	pdb.gimp_image_delete(img)