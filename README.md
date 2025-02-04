# Poor Posture Detection

The **Poor Posture Detection** project monitors real-time body posture using MediaPipe and OpenCV. It calculates keypoint angles to detect poor posture (e.g., slouching) and triggers audio alerts. This system is ideal for ergonomic monitoring, fitness training, and preventative health applications.

## Features

- **Real-time Posture Analysis:** Uses MediaPipe Pose to detect body landmarks and calculate posture angles.
- **Alert System:** Plays an audio alert when poor posture is detected.
- **Modular Design:** Separate modules for posture detection, camera feed, utilities, and alert handling.
- **Configurable Settings:** Easily adjust detection thresholds and alert preferences via configuration files.

## Project Structure

poor_posture_detection/
├── src/
│   ├── posture_detector.py       # Core script for detecting body posture
│   ├── utils.py                  # Helper functions (e.g., angle calculation)
│   ├── alert_system.py           # Handles alerts (sound, notifications, etc.)
│   ├── camera_feed.py            # Captures webcam feed for real-time tracking
│   └── model/                    # (Optional) Trained models for AI-based posture classification
│       └── __init__.py           # (Empty file for package initialization)
├── assets/
│   ├── sounds/                   # Audio alerts
│   │   └── alert.mp3             # (Place your alert sound file here)
│   └── images/                   # Sample images for testing (if needed)
├── config/
│   └── settings.py               # Configuration parameters (thresholds, alert preferences)
├── notebooks/
│   └── posture_analysis.ipynb    # Jupyter notebook for testing and visualization
├── tests/
│   └── test_posture.py           # Unit tests for posture detection
├── docs/
│   └── README.md                 # Project documentation and setup guide
├── requirements.txt              # List of required dependencies
├── main.py                       # Entry point to run the posture detection system
└── .gitignore                    # Ignore unnecessary files





