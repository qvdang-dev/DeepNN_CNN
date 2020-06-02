import argparse
import cv2

from slidingBox import sliding_on_Image

def command_parsing():     
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the image")
    
    args = vars(ap.parse_args())
    # load the image and define the window width and height
    image = cv2.imread(args["image"])
    (boxWidth, boxHight) = (28, 28)
    
    return image, boxWidth, boxHight

def sliding_image(image, w, h):
    sliding_on_Image(image, w, h)

