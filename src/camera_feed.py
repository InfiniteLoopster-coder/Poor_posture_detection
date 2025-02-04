import cv2

class CameraFeed:
    def __init__(self, camera_index=0):
        self.camera_index = camera_index
        self.cap = cv2.VideoCapture(self.camera_index)

    def get_frame(self):
        """
        Captures a single frame from the webcam.
        
        Returns:
            ret (bool): Whether the frame was successfully captured.
            frame (ndarray): The captured frame.
        """
        ret, frame = self.cap.read()
        return ret, frame

    def release(self):
        """
        Releases the webcam.
        """
        self.cap.release()
        cv2.destroyAllWindows()
