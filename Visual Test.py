import cv2
import numpy as np
import pandas as pd

# Function to extract steering angle from data point
def get_steering_angle(data_point):
    return data_point["steering_angle"]

def detect_lane_departure(frame):
    lower_white = np.array([200, 200, 200])
    upper_white = np.array([255, 255, 255])
    
    mask = cv2.inRange(frame, lower_white, upper_white)
    
    lane_contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return is_lane_departure

def detect_hazards(frame):
    return detect_hazards

# Load the video file and associated data
video = cv2.VideoCapture("Experimenter_9110002_53.mp4")
data = pd.read_csv("Experimenter_9110002_53.dat")

driver_risk_score = 0
driver_attention_score = 0

# Main loop to process each frame of the video
while True:
    ret, frame = video.read()
    if not ret:
        break

    timestamp = ...
    data_point = data.loc[data['timestamp'] == timestamp]
    steering_angle = get_steering_angle(data_point)
    is_lane_departure = detect_lane_departure(frame)

    driver_risk_score += abs(steering_angle)
    if is_lane_departure:
        driver_risk_score += 10

    cv2.imshow("Driver Monitoring", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close any open windows
video.release()
cv2.destroyAllWindows()
