# import the necessary packages
from calculator_functions import *
from imutils import face_utils
import dlib
import imutils
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("--model", required=True, help="Model path")
args = vars(ap.parse_args())

model_path = args['model']

# Now, intialize the dlib's face detector model as 'detector' and the landmark predictor model as 'predictor'
print("[INFO] Loading the predictor ...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(model_path)

print("[INFO] Loading the Camera ...")
cap = cv2.VideoCapture(0)

print("[INFO] Predictor is ready!")

while True:
    ret, frame = cap.read()

    cv2.putText(frame, "PRESS 'q' TO EXIT", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 3)

    frame = imutils.resize(frame, width=700)
    (h, w) = frame.shape[:2]
    rects = detector(frame, 0)
    
    if len(rects) > 0:
        rect = get_max_area_rect(rects)

        (x, y, w, h) = face_utils.rect_to_bb(rect)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        shape = predictor(frame, rect)
        shape = face_utils.shape_to_np(shape)

        leftEye = shape[0:6]
        rightEye = shape[6:12]
        mouth = shape[12:32]

        for (sX, sY) in shape:
            cv2.circle(frame, (sX, sY), 1, (0, 0, 255), -1)
        
    cv2.imshow("output", frame)

    # detect any kepresses
    key = cv2.waitKey(1) & 0xFF
    
    # set the last active check time as current time
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

# do a bit of cleanup
cv2.destroyAllWindows()