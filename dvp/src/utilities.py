import argparse
import cv2

from slidingBox import sliding_on_Image

def command_parsing():     
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the image")
    ap.add_argument("-bw", "--boxwidth", type=int ,help="width of sliding box")
    ap.add_argument("-bh", "--boxhight", type=int ,help="hight of sliding box")
    
    args = vars(ap.parse_args())
    # load the image and define the window width and height
    image = cv2.imread(args["image"])
    (boxWidth, boxHight) = (args["boxwidth"], args["boxhight"])

    return image, boxWidth, boxHight

def sliding_image(image, w, h):
    sliding_on_Image(image, w, h)

