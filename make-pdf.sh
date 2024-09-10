#!/bin/bash


#https://legacy.imagemagick.org/discourse-server/viewtopic.php?t=33309
convert wordslist/*.png -gravity Center -extent 1600x2262 -density 76.1905 -units pixelspercentimeter wordslist/ce1-wordslist.pdf