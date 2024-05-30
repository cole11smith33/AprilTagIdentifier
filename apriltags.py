import cv2
import apriltag

#Convert frame into grayscale
def preprocess_frame(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return gray

#Draw bounding boxes around perimeter of AprilTag
def draw_apriltags(image, detections):
    for detection in detections:

        #Extract information regarding specific tag
        tag_id = detection.tag_id
        corners = detection.corners
        
        #Draw bounding box
        cv2.polylines(image, [corners.astype(int)], True, (0, 255, 0), 2)
        
        #Write which tag it is
        cv2.putText(image, str(tag_id), (int(corners[0][0]), int(corners[0][1])), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

#Open up video capture device (may need to be changed between 0 and 1 depending on network connectivity)
cap = cv2.VideoCapture(1)

# Ensure webcam has opened correctly
if not cap.isOpened():
    print("Error: Failed to open webcam")
    exit()

detector = apriltag.Detector()

#Continually take new frames from webcam
while True:
    #Read frame
    ret, frame = cap.read()
    
    #Check if the frame was successfully read
    if not ret:
        print("Error: Failed to read frame from webcam")
        break
    
    #Convert the frame to grayscale and preprocess it (ensures that doesn't exceeed quality that vscode can handle)
    gray = preprocess_frame(frame)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    
    #Detect AprilTags in the frame
    detections = detector.detect(blurred)
    
    #Draw and display boxes and IDs around frame
    draw_apriltags(frame, detections)
    cv2.imshow('AprilTags Detection', frame)
    
    #Check for key press 'q' to exit the loop
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

#Release the video capture device and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
