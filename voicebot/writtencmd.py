import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class VoicePublisher(Node):
    def __init__(self):
        super().__init__('sendingCommand')
        self.cmndpub=self.create_publisher(String,'voice_command',10)
        self.timer = self.create_timer(0.5,self.sendCommand)

    def sendCommand(self):
        self.voice=String()
        self.voice.data=input("Give command -")
        self.cmndpub.publish(self.voice)

def main():
    rclpy.init()

    voicepub= VoicePublisher()

    rclpy.spin(voicepub)

    VoicePublisher.destroy_node()
    rclpy.shutdown()


if __name__=='__main__':
    main()
