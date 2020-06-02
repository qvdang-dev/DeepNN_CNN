import cv2
import imutils
import time

def resize_Imgae(image, scale = 2, minSize = (30, 30)):
    # return the original image at the first time
    # yield image

    while True:
        width_resized = int(image.shape[1]/ scale)
        image = imutils.resize(image, width = width_resized)
        
        if image.shape[0] < minSize[0] or image.shape[1] < minSize[1]:
            break

        yield image

def sliding_Box(image, step, boxSize):
    for y in range(0, image.shape[0], step):
        for x in range(0, image.shape[1], step):
            yield (x, y, image[y:y + boxSize[1], x:x + boxSize[0]])
             
# loop over the image pyramid
def sliding_on_Image(image, boxWidth, boxHight):
    for resized in resize_Imgae(image, scale=1.5):
        # loop over the sliding window for each layer of the pyramid
        for (x, y, window) in sliding_Box(resized, step = 32, boxSize=(boxWidth, boxHight)):
            # if the window does not meet our desired window size, ignore it
            if window.shape[0] != boxHight or window.shape[1] != boxWidth:
                continue
            # THIS IS WHERE YOU WOULD PROCESS YOUR WINDOW, SUCH AS APPLYING A
            # MACHINE LEARNING CLASSIFIER TO CLASSIFY THE CONTENTS OF THE
            # WINDOW
            # since we do not have a classifier, we'll just draw the window
            clone = resized.copy()
            cv2.rectangle(clone, (x, y), (x + boxWidth, y + boxHight), (0, 255, 0), 2)
            cv2.imshow("Window", clone)
            cv2.waitKey(1)
            time.sleep(0.025)
