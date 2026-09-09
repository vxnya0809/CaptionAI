import cv2
import mediapipe as mp
import pandas as pd 
import os
mp_hands=mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=1,
    min_detection_confidence=0.5
)
dataset_path="dataset"
data = []
for gesture in os.listdir(dataset_path):
    gesture_path = os.path.join(dataset_path,gesture)
    if not os.path.isdir(gesture_path):
        continue
    print(f"Processing: {gesture}")
    for image_name in os.listdir(gesture_path):
        image_path = os.path.join(gesture_path,image_name)
        image = cv2.imread(image_path)
        if image is None :
            continue
        rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)
        if results.multi_hand_landmarks:
            hand=results.multi_hand_landmarks[0]
            landmarks=[]
            for lm in hand.landmark:
                landmarks.extend([lm.x,lm.y,lm.z])
            landmarks.append(gesture)
            data.append(landmarks)
print("Extraction complete!")
columns=[]
for i in range(21):
    columns.append(f"x{i}")
    columns.append(f"y{i}")
    columns.append(f"x{i}")
columns.append("label")
df=pd.DataFrame(data,columns=columns)
df.to_csv("landmarks.csv",index=False)
print("CSV Saved Successfully!")
print(df.head())