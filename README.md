# ROS package for demonstrating TF (Transform) usage

## Instructions to build and use the repo:

1. Clone the repository in your local system.
2. Copy the folder demo_tf1 from ROS\_packages into your catkin working directory.
3. Perform the following commands:
```
cd ~/catkin_ws
catkin_make
source ~/.bashrc
or
source devel/setup.bash
```
4. Launch the ROS package using: `roslaunch demo_tf1 start_demo.launch`
5. Play around with the launched window to check working of TF.

## Important commands in TF:
- Generate a pdf of all the connections in TF tree of your system:
`rosrun tf view_frames`

- Continuously monitor the transform between two frames (frame2 with respect to frame1):
`rosrun tf tf_echo /frame1 /frame2`

- Alternate way to check tf tree, run rqt_gui and add tf tree plugin to view it:
`rosrun rqt_gui rqt_qui`
