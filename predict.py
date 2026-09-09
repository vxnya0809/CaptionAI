import cv2
import mediapipe as mp 
import joblib
model = joblib.load("gesture_model.pk1")
mp_hands = mp.solutions.hands
hands=mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence = 0.7,
    min_tracking_confidence = 0.7
)
mp_draw=mp.solutions.drawing_utils
def predict_gesture():
    camera = cv2.VideoCapture(0)
    predicted_text = ""
    while True:
        success,frame = camera.read()
        if not success:
            break
        frame=cv2.flip(frame,1)
        rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS
                )
                landmarks = []
                for lm in hand_landmarks.landmark:
                    landmarks.extend([lm.x,lm.y,lm.z])
                prediction = model.predict([landmarks])
                predicted_text=prediction[0]
                cv2.putText(
                    frame,
                    f"Gesture : {predicted_text}",
                    (20,50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0,255,0),
                    2
                )
        cv2.imshow("CaptionAI",frame)
        key = cv2.waitKey(1)
        if key == ord("q"):
            break
    camera.release()
    cv2.destroyAllWindows()
    return predicted_text
