# Eye-Tracking-Data-in-Driving-Simulator
Applications of AI and machine learning with eye tracking data in driving simulator scenarios ( GSOC 2024 Prototype)

**Description of Visual Test.py :**

- The code processes a video file of driving footage along with associated data stored in a CSV file.
- It uses OpenCV for video manipulation and pandas for data handling.
- Functions are defined to extract steering angle, detect lane departure, and potentially detect hazards in the environment.
- Inside the main loop, each frame of the video is processed to calculate driver risk scores based on steering angle and lane departure.
- Visualizations or overlays for risk scores are not implemented in this code.
- The program terminates when the user presses 'q'.

**Description of Drive Analysis.ipynb :**

- The code loads data from a CSV file using pandas and handles exceptions if the file is not found or if there are parsing errors.
- After loading the data, it checks for missing values in specific columns and issues warnings if found.
- Statistical analysis is performed on the data, including calculating average speed and standard deviation of speed.
- Events such as harsh acceleration, harsh braking, and sharp turns are identified based on predefined thresholds.
- Lane departures are calculated based on lane offset, and the total duration off-lane is computed.
- Time-to-collision (TTC) metrics are calculated based on relative speed and headway distance.
- A heatmap visualization is generated to represent driver input intensity over time, including steering, acceleration, and braking.
