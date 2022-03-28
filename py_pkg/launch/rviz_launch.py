from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
import os.path



def generate_launch_description():

    package_dir = get_package_share_directory('py_pkg')
    urdf = os.path.join(package_dir,'carver.urdf')
    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            name='robot_state_publisher',
            executable='robot_state_publisher',
            output ='screen',
            arguments=[urdf]),
        Node(
            package='joint_state_publisher_gui',
            name='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            
            arguments=[urdf]),

        Node(
            package='rviz2',
            
            executable='rviz2',
            name='rviz2',  
            output ='screen',  ),

        
    ])