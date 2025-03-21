
# Voice Bot

I have used ROS2 Humble for this assignment.

## Prerequisites

For this assignment, a python library called SpeechRecognition is used.

To install SpeechRecognition

```bash
  pip install SpeechRecognition
```


## Installation

1. First of all, you have to create a ros workspace and then in the src folder clone this repo.

```bash
  git clone https://github.com/Tasfiq-Mahmud/Voicebot.git
```

2. Now, you have to build the package.
Go to the root workspace directory and run

```bash
  colcon build
```

3. Source the workspace.

```bash
  source install/setup.bash #setup.zsh if you are using zsh
```

4.Now, launch gazebo and turtlebot3 simulation bot 

```bash
  export TURTLEBOT3_MODEL=burger 
  ros2 launch turtlebot3_gazebo empty_world.launch.py
```

5.Now, in another terminal, run voice.launch.py. (do step 3 for the new terminal)

```bash
  ros2 launch voicebot voice.launch.py
```

If the launch file doesnt work, then in two terminal(do step 3 for each) run these two programs separately


```bash
  ros2 run voicebot speaker.py
```

```bash
  ros2 run voicebot writer.py
```

