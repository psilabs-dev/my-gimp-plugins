#!/usr/bin/env python

import os
import sys
sys.path.append(os.path.dirname(__file__))
from common import *
from glob import glob

def batch_convert_xcf_to_png(input_dir, output_dir):
    for filename in glob(os.path.join(input_dir, "*.xcf")):
        convert_xcf_to_png(filename, output_dir)

register(
    "convert_xcf_to_png",
    "Batch convert XCF to PNG",
    "Convert all XCF files in an input directory to PNG format in an output directory",
    "psilabs",
    "psilabs",
    "2023",
    "XCF to PNG",
    "",  # No image type needed
    [
        (PF_DIRNAME, "input_dir", "Input directory", ""),
        (PF_DIRNAME, "output_dir", "Output directory", ""),
    ],
    [],
    batch_convert_xcf_to_png,
    menu="<Image>/Converter"
)

main()
