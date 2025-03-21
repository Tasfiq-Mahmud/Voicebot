from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='voicebot',
            executable='speaker',
            name='speaker_turtle',
            output='screen',
        ),
        Node(
            package='voicebot',
            executable='control',
            name='control_turtle',
            output='screen'
        ),
    ])