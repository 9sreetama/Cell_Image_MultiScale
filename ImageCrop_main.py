# #############################################################################
# This program read images from a specified input folder, then stacks the images
# as 3/2 channel (RGB), then segment the cells and crop them into new images in the 
# output folder. The cell crops are saved in 3 different scales 
# (parameter size = 40,80,120) which is updated in chop_nuclei function().
# 
# #############################################################################

# ------------------------------
# Import Libraries
# ------------------------------
import re
import glob, os
from PIL import Image
import numpy as np
from skimage import feature
from skimage import io
import ImageCrop_funcs

# --------------------------------------
# stack_crop_img(input_path, output_path)
# ---------------------------------------
def RGB_crop_img(input_path, output_path):
"""
Read the image files from folder and stack each of 
color channels to create an RGB image. 
Then crop the RGB images and save into output dir

INPUT - directory path for reach images. Note that the images have to be named 
identically except for the Channel number (e.g Channel1-60-E-12.BMP & 
Channel2-60-E-12.BMP for two channel image)

OUTPUT - Output directory path for stacked and cropped to be written
"""

num_images = len(glob.glob1(input_path,"*.BMP"))
print('DBG: Num Files in Folder:', num_images)

rgbArray = np.zeros((640, 640,3), 'uint8')
for filename,idx in zip(glob.glob(input_path + '*.BMP'), range(50)):
    print('DBG: filename, idx:', filename, idx)
    base=os.path.basename(filename)
    filename_save, file_extension = os.path.splitext(base)
    # Stack Images from Channel1 and Channel2
    if ( "Channel1" in os.path.splitext(base)[0]):
        rgbArray[...,0] = np.array(Image.open(filename))
        filename2 = filename.replace('Channel1', 'Channel2')
        rgbArray[...,1] = np.array(Image.open(filename2))
        # print('DBG: img_channel1 size:', img_channel1.size)
        #img = Image.fromarray(rgbArray)
        #print('DBG: img size:', img.size)
        arr = ImageCrop_funcs.chop_nuclei(rgbArray)
        filename_save = filename_save.replace('Channel1-', 'NEG_')
        print(filename_save)
        # Save Image to output folder
        ImageCrop_funcs.save_chopped(arr,output_path,prefix=filename_save, ext=".png", save_as="img") 
     
def main():
    # ------------------------------
    # Set File Paths
    # ------------------------------
    input_path = "img_input/Test/NEG/"
    output_path = "img_crops/Test_Scale3/"
    RGB_crop_img(input_path, output_path)
         
if __name__ == "__main__":
    main()