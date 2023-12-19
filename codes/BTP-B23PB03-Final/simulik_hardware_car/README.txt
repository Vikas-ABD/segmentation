Raspberry Pi Car Control System
This folder contains Simulink models and instructions for setting up a Raspberry Pi-based car control system. The system allows you to control a car remotely using your Android phone, which also provides a live video stream from the Raspberry Pi camera.

Prerequisites
Before you start, make sure you have the following:

MATLAB installed on your computer.

Simulink installed with the necessary toolboxes:

Simulink
Raspberry Pi Support Package
Image Processing Toolbox
Computer Vision Toolbox
MATLAB Support Package for Android
Raspberry Pi with MATLAB Raspbian OS installed. Follow MATLAB's documentation for instructions on installing MATLAB on Raspberry Pi.

Setup Instructions
1. Open the Simulink Model
Open the raspimodel.slx file in Simulink. Ensure that all required toolboxes are installed.

2. Deploy Model to Raspberry Pi
Deploy the Simulink model to your Raspberry Pi. This will enable the car to execute the control logic.

3. Install Android Packages and Toolboxes
Install the required Android packages and toolboxes in MATLAB to enable communication with your Android phone.

4. Deploy Android Model
Open the androidmodel.slx file in Simulink and deploy it to your Android phone. This model handles the communication between the phone and the Raspberry Pi.

5. Connect Raspberry Pi and Phone to the Same WiFi Network
Ensure both the Raspberry Pi and your Android phone are connected to the same WiFi network to establish communication.

6. Run the System
Now that everything is set up, run the system. You should be able to control the car using your Android phone and receive a live video stream from the Raspberry Pi camera.

Object Detection
If you want to incorporate object detection, use the object_detection.slx file in Simulink. This model enhances the system's capabilities by integrating object detection algorithms.

Feel free to explore and modify the Simulink models according to your requirements.

Note: Make sure to refer to the MATLAB and Simulink documentation for detailed instructions on each step and additional troubleshooting tips.