# Multi Robot Factory Workspace

A professional ROS 2 (Jazzy) workspace showcasing a modular multi-robot factory stack with simulation, motion planning, control, and behavior trees.

## Package Plan
- factory_interfaces: Messages, services, actions.
- factory_description: Robot & cell description (URDF/Xacro, meshes).
- factory_control: ros2_control configs & controller launch.
- factory_sim: Gazebo (modern) worlds and launch integration.
- factory_sim_plugins: Custom Gazebo / ros_gz plugins.
- factory_moveit_config: MoveIt 2 configuration.
- factory_bringup: System-level launch and parameter layering.
- factory_bt_nodes: BehaviorTree.CPP ROS node plugins.
- factory_bt_trees: XML BT definitions & task compositions.
- factory_tasks: Higher-level task orchestration/demos.
- factory_tools: Utility scripts (calibration, data capture).
- factory_testing: Integration and simulation tests.

## Roadmap (High Level)
1. Interfaces
2. Core demo nodes
3. Control + Description + Simulation
4. Plugins + MoveIt 2
5. Behavior Trees & Task orchestration
6. Testing & CI

## Build
```
colcon build --symlink-install
source install/setup.bash
```

## License
To be determined.
