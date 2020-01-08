# Cell_Image_MultiScale

This program read images from a specified input folder, then stacks the images as 3/2 channel (RGB), 
then segment the cells and crop them into new images in the output folder. 
The cell crops are saved in 3 different scales (parameter size = 40,80,120) which is updated in chop_nuclei function().
