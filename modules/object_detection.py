import cv2

def detect_objects():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Camera error.")
        return

    print("Starting object detection. Press Q to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Object Detection", gray)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()
