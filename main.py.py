import cv2
import mediapipe as mp
from hand_utils import HandDetector
from calculator import Calculator

def main():
    detector = HandDetector()
    calc = Calculator()
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        success, frame = cap.read()
        if not success: break
        
        frame = detector.find_hands(frame)
        landmarks = detector.get_landmarks(frame)
        
        if landmarks:
            num = detector.count_fingers(landmarks)
            operation = detector.detect_operation(landmarks)
            calc.process_input(num, operation)
        
        # Display UI
        cv2.putText(frame, f"Input: {calc.current_input}", (10, 50), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(frame, f"Result: {calc.result}", (10, 100),
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        
        cv2.imshow("Hand Sign Calculator", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()