import threading, time
import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from mavros_msgs.msg import State
from mavros_msgs.srv import SetMode, CommandBool, CommandTOL
from geometry_msgs.msg import PoseStamped
from rclpy.qos import qos_profile_sensor_data

class FlightCommander(Node):
    def __init__(self):
        super().__init__('flight_commander')
        self.state = State()
        self.pose = PoseStamped()

        #subscribers, to state and posr updates
        self.create_subscription(State, '/mavros/state', self._state_cb, 10)
        self.create_subscription(PoseStamped, '/mavros/local_position/pose', self._pose_cb, qos_profile_sensor_data)


