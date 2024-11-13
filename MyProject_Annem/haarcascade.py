import cv2
import os
import pandas as pd

# Define the absolute paths to the Haar cascade XML files
face_cascade_path = r'C:\Users\saad2\Desktop\Project_Omotec\MyProject\opencv_3.4_data_haarcascades\haarcascade_frontalface_default.xml'
eye_cascade_path = r'C:\Users\saad2\Desktop\Project_Omotec\MyProject\opencv_3.4_data_haarcascades\haarcascade_eye.xml'
smile_cascade_path = r'C:\Users\saad2\Desktop\Project_Omotec\MyProject\opencv_3.4_data_haarcascades\haarcascade_smile.xml'

# Check if all the files exist before loading them
if not os.path.isfile(face_cascade_path):
    raise FileNotFoundError(f"Face cascade file not found at {face_cascade_path}")
if not os.path.isfile(eye_cascade_path):
    raise FileNotFoundError(f"Eye cascade file not found at {eye_cascade_path}")
if not os.path.isfile(smile_cascade_path):
    raise FileNotFoundError(f"Smile cascade file not found at {smile_cascade_path}")

# Load the Haar cascades using absolute paths
face_cascade = cv2.CascadeClassifier(face_cascade_path)
eye_cascade = cv2.CascadeClassifier(eye_cascade_path)
smile_cascade = cv2.CascadeClassifier(smile_cascade_path)

# Initialize webcam video capture
cap = cv2.VideoCapture(0)

# Create a list to store the feature details
features_list = []

while True:
    # Read the frame from the camera
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale (Haar Cascades work better on grayscale images)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Draw a rectangle around the detected face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Store face features
        features_list.append(['Face', x, y, w, h])

        # Region of interest for detecting eyes and smile within the face rectangle
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # Detect eyes within the face region
        eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=10, minSize=(15, 15))
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
            # Store eye features relative to the face region
            features_list.append(['Eye', x + ex, y + ey, ew, eh])

        # Detect smile within the face region
        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.7, minNeighbors=22, minSize=(25, 25))
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 0, 255), 2)
            # Store smile features relative to the face region
            features_list.append(['Smile', x + sx, y + sy, sw, sh])

    # Display the resulting frame with detected features
    cv2.imshow('Face, Eyes, and Smile Detection', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()

# Create a DataFrame to store the features
features_df = pd.DataFrame(features_list, columns=['Feature', 'X', 'Y', 'Width', 'Height'])

# Save the features to a CSV file
features_df.to_csv('detected_features.csv', index=False)
print("Feature details saved to detected_features.csv")

# If you prefer saving to an Excel file, use:
features_df.to_excel('detected_features.xlsx', index=False)