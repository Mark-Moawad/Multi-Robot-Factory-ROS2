#!/usr/bin/env python3
import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import xacro

def generate_launch_description():
    pkg_share = get_package_share_directory('factory_description')
    assembly_xacro = os.path.join(pkg_share, 'xacro', 'assemblies', 'factory_workcell.xacro')
    doc = xacro.process_file(assembly_xacro, mappings={'with_robot2': 'false', 'with_sensors': 'false'})
    robot_desc = doc.toprettyxml(indent='  ')

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_desc}],
        )
    ])
