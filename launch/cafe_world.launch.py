from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    world_path = os.path.join(
        get_package_share_directory('my_cafe_world'),
        'worlds',
        'my_cafe.world'
    )

    return LaunchDescription([
        # Start Gazebo server with the custom world
        ExecuteProcess(
            cmd=['gazebo', '--verbose', world_path, '-s', 'libgazebo_ros_factory.so'],
            output='screen'
        ),

        # Optionally spawn your robot if you have a URDF/SDF
        # Example:
        # Node(
        #     package='gazebo_ros',
        #     executable='spawn_entity.py',
        #     arguments=['-entity', 'my_robot', '-file', os.path.join(
        #         get_package_share_directory('my_robot_description'), 'urdf', 'robot.urdf')],
        #     output='screen'
        # )
    ])

