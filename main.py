  
import cv2
from API import make_detection
  
# Path to Input image. NOTE : Minimum image size is 512x512
IMAGE_PATH = 'C:/Users/Deepesh/Desktop/Receipt Detection/Resized Receipt Images/image_85.jpg'

# PROVIDE PATH TO LABEL MAP
LABELS_PATH = 'C:/Users\Deepesh/Desktop/Receipt Detection/label_map.pbtxt'

MODEL_PATH = "C:/Users/Deepesh/Desktop/Receipt Detection/trained_model/saved_model"

#-----------------------------------------------------------------


OUTPUT_IMG = make_detection(IMAGE_PATH,MODEL_PATH,LABELS_PATH)

# SAVE OUTPUT IMAGE
print("Saving the output image locally...")
Save_Path = "receipt_detection_6.jpg"
cv2.imwrite(Save_Path,OUTPUT_IMG)

# DISPLAY OUTPUT
cv2.imshow("RESULT",OUTPUT_IMG)
cv2.waitKey(0)

