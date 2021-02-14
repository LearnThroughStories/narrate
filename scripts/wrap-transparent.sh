#!/bin/sh 

# Requires imagemagick to be installed
# The cover images (00.jpg) are half pages. This script extends
# the canvas by creating a .png file with a transparent background
# and the given image stuck to the right.
convert               \
      $1       \
     -background none \
     -gravity east  \
     -extent 1024x787  \
      $2
