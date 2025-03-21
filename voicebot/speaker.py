import rclpy
from rclpy.node import Node
import speech_recognition as sr
from std_msgs.msg import String

class VoicePublisher(Node):
    def __init__(self):
        super().__init__('sendingCommand')
        self.cmndpub=self.create_publisher(String,'voice_command',10)
        self.timer = self.create_timer(0.5,self.sendCommand)

    def sendCommand(self):
        self.voice=String()
        recognizer=sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            try:
                self.voice.data = recognizer.recognize_google(audio)
                self.cmndpub.publish(self.voice)
                self.get_logger().info(f"Published: {self.voice.data}")
            except sr.UnknownValueError:
                self.get_logger().warn("Speech not recognized")
            except sr.RequestError:
                self.get_logger().warn("Could not request results from Google Speech Recognition") 
        
        


def main():
    rclpy.init()

    voicepub= VoicePublisher()

    rclpy.spin(voicepub)

    VoicePublisher.destroy_node()
    rclpy.shutdown()


if __name__=='__main__':
    main()
