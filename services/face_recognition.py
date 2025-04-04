import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2


#Model Path
#model_path = "blaze_face_short_range.tflite"



#cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Camer is not accessible!!")
    
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab the Frame!!")
        break
    
    cv2.imshow("Camer Feed",frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()



#Run Face Detection to Extract the Features of the User With openCV
#Perform Face Recognition with FaceNet 
#store the User Embedding in the Data Base 
#Run Face Recognition to Correctly Detect the user 