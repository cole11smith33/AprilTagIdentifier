# AprilTagIdentifier

  This project takes live video feed, and is able to identify all present apriltags (family, number and pose). Code for this project can easily be implemented in ROS2 node to run on robots (eg. Turtlebot4) and on simulation software (eg. Gazebo, PyBullet, WeBots).

<img width="1026" alt="Screenshot 2025-01-01 at 3 24 37 PM" src="https://github.com/user-attachments/assets/0448ce4a-dc78-4998-b430-74c5cd3fb662" />

  AprilTag is a fidual marker system developed by the APRIL Robotics Lab from the University of Michigan. These tags are useful for robotics and camera calibration. This project that I created is part of the larger work ARCO Labs at McMaster University under the management of Dr. Giamou. AprilTagIdentifier is a small step towards the eventual goal of having an autonomous fleet of drones to map subterranean environments. 

  ## Setup

#### 1. Clone the GitHub repository
  git clone https://github.com/cole11smith33/AprilTagIdentifier

#### 2. Change parameter passed to VideoCapture in line 24 in apriltags.py
  start at 0, and try incrementing number by 1 until you are using the correct device. 0 will corrospond to your computers main priority, and as the number increases, will switch between the lower priority accessory cameras.
