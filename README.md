## Receipt Information Object Detection

An object detection system which can detect useful information like address & price from purchase receipts.

<div float="left" align="center">
<img src="/examples/receipt_detection_1.jpg"  width="30%"/>
<img src="/examples/receipt_detection_2.jpg"  width="30%"/> 
<img src="/examples/receipt_detection.jpg"  width="30%"/> 
</div>


## To Run (Locally)

1. Git clone the repository on your system. This will download the pre-trained model and required files on your computer.
```
git clone https://github.com/deepeshdm/Receipt_Info_Detection.git
```

2. Install the required dependencies to run the app
```
pip install -r requirements.txt
```

3. Open the "main.py" file , pass the required values to the function , Execute the file.

```python
import cv2
from API import make_detection
  
# Path to Input image. NOTE : Minimum image size is 512x512
IMAGE_PATH = 'C:/Users/Deepesh/Desktop/Receipt Detection/Resized Receipt Images/image_85.jpg'

# PROVIDE PATH TO LABEL MAP
LABELS_PATH = 'C:/Users/Deepesh/Desktop/Receipt Detection/label_map.pbtxt'

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
```
   
### NOTE : All the input images are automatically resized to 512x512.


## Important

If you encounter an error - 'tensorflow has no attribute gfile' , then you'll have to make changes to your site-packages present locally.
- Follow this : https://github.com/tensorflow/tensorflow/issues/31315























