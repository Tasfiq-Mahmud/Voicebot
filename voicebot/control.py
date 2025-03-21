import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from geometry_msgs.msg import Twist
import re
import time

class controlTurtle(Node):
    def __init__(self):
        super().__init__('control_turtle')
        self.sub=self.create_subscription(String,'voice_command', self.controlclbk,10)
        self.pub=self.create_publisher(Twist,'cmd_vel',10)
        self.energy=10
        self.get_logger().info(f'Remaining Energy: 10.0')
    
    def create(self,msg):
        vel=Twist()
        s=msg.lower()
        l=['heal','heel','hill']
        if any(x in s for x in l):
            self.energy+=5
            return vel,0,'Healing'
        elif 'forward' in s:
            r='forward'
            vel.linear.x=0.1
        elif 'backward' in s:
            r='backward'
            vel.linear.x=-0.1
        elif 'left' in s:
            r='left'
            vel.angular.z=0.5
        elif 'right' in s:
            r='right'
            vel.angular.z=-0.5
        
        sec=re.search(r'(\d+)\s*(s|sec|second|seconds)',s,re.IGNORECASE)
        try:
            num=float(sec.group(1))
        except:
            num=2
        return vel,num,('Moving '+r+' for '+str(num)+' seconds')

    def controlclbk(self,cmnd):
        self.get_logger().info(f'Command Taken - {cmnd.data}')
        vel,num,r=self.create(cmnd.data)
        if self.energy-num<0:
            self.get_logger().info(f'Not Sufficient Energy.Remaining Energy: {self.energy}.')
            return
        self.energy-=num # movement time equals to energy loss
        self.get_logger().info(r)
        self.get_logger().info(f'Remaining Energy: {self.energy}')
        self.pub.publish(vel)
        time.sleep(num)
        self.pub.publish(Twist())


def main():
    rclpy.init()
    turtle=controlTurtle()
    rclpy.spin(turtle)
    controlTurtle.destroy_node()
    rclpy.shutdown()
    

if __name__=='__main__':
    main()