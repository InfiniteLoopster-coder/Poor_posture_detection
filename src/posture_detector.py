import cv2
import mediapipe as mp
from src.utils import calculate_angle
from src.alert_system import AlertSystem
from config.settings import SHOULDER_ANGLE_THRESHOLD
from src.camera_feed import CameraFeed

class PostureDetector:
    def __init__(self):
        self.camera = CameraFeed()
        self.alert_system = AlertSystem()
        # Initialize MediaPipe Pose.
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

    def run(self):
        """
        Runs the real-time posture detection.
        """
        while True:
            ret, frame = self.camera.get_frame()
            if not ret:
                break

            # Convert the image to RGB.
            image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image_rgb.flags.writeable = False

            # Process the image to detect the pose.
            results = self.pose.process(image_rgb)

            # Convert back to BGR for rendering.
            image_rgb.flags.writeable = True
            frame = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

            if results.pose_landmarks:
                self.mp_drawing.draw_landmarks(
                    frame, results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS)
                landmarks = results.pose_landmarks.landmark

                # Extract specific landmarks:
                # left_shoulder = index 11, left_hip = index 23, left_ear = index 7
                left_shoulder = [landmarks[11].x, landmarks[11].y]
                left_hip = [landmarks[23].x, landmarks[23].y]
                left_ear = [landmarks[7].x, landmarks[7].y]

                # Calculate the angle at the left shoulder.
                angle = calculate_angle(left_ear, left_shoulder, left_hip)

                # Display the angle on the frame.
                cv2.putText(frame, f'Angle: {int(angle)}', (50, 50), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

                # Check if the angle indicates poor posture.
                if angle < SHOULDER_ANGLE_THRESHOLD:
                    cv2.putText(frame, 'Bad Posture!', (50, 100), 
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                    self.alert_system.trigger_alert()

            cv2.imshow('Posture Detection', frame)
            # Press 'Esc' key to exit.
            if cv2.waitKey(5) & 0xFF == 27:
                break

        self.camera.release()
