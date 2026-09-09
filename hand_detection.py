import cv2
import mediapipe as mp 
mp_hands=mp.solutions.hands 
hands=mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw=mp.solutions.drawing_utils
camera=cv2.VideoCapture(0)
while True:
    success,frame=camera.read()
    if not success:
        print("Failed to access camera")
        break
    frame=cv2.flip(frame,1)
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=hands.process(rgb_frame)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for id,landmark in enumerate(hand_landmarks.landmark):
                h,w,c = frame.shape
                x=int(landmark.x*w)
                y=int(landmark.y*h)
                print(f"Point{id}: X={x}, Y={y}")
            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )
    cv2.imshow("CAPTIONAI",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
camera.release()
cv2.destroyAllWindows()