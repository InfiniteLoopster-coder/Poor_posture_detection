import time
from playsound import playsound
import os
from config.settings import ALERT_SOUND_PATH, ALERT_COOLDOWN

class AlertSystem:
    def __init__(self):
        self.last_alert_time = 0

    def trigger_alert(self, message="Bad Posture Detected!"):
        """
        Triggers an alert by playing a sound if cooldown time has passed.
        """
        current_time = time.time()
        if current_time - self.last_alert_time > ALERT_COOLDOWN:
            print(message)  # Optionally log or print the message.
            # Ensure the alert sound file exists before playing.
            if os.path.exists(ALERT_SOUND_PATH):
                playsound(ALERT_SOUND_PATH)
            else:
                print(f"Alert sound not found at {ALERT_SOUND_PATH}")
            self.last_alert_time = current_time
