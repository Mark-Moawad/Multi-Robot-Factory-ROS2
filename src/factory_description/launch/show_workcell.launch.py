#!/usr/bin/env python3
import os
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import xacro

def generate_launch_description():
    with_robot2 = LaunchConfiguration('with_robot2')
    with_sensors = LaunchConfiguration('with_sensors')

    pkg_share = get_package_share_directory('factory_description')
    assembly_xacro = os.path.join(pkg_share, 'xacro', 'assemblies', 'factory_workcell.xacro')

    # Defer xacro expansion until launch runtime by evaluating LaunchConfigurations
    # We process once here (static) for simplicity; for dynamic arg changes a xacro exec node could be used.
    doc = xacro.process_file(assembly_xacro, mappings={
        'with_robot2': 'true',
        'with_sensors': 'true'
    })
    robot_desc = doc.toprettyxml(indent='  ')

    return LaunchDescription([
        DeclareLaunchArgument('with_robot2', default_value='true'),
        DeclareLaunchArgument('with_sensors', default_value='true'),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_desc}],
        )
    ])
