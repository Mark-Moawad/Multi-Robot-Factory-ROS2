cmake_minimum_required(VERSION 3.8)
project(factory_interfaces)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(std_msgs REQUIRED)

# Message / Service / Action files
set(MSG_FILES
  "msg/Proximity.msg"
  "msg/Order.msg"
  "msg/Kit.msg"
  "msg/DetectedObject.msg"
  "msg/LogicalCameraImage.msg"
  "msg/Model.msg"
  "msg/PopulationState.msg"
  "msg/StorageUnit.msg"
  "msg/ConveyorBeltState.msg"
  "msg/KitObject.msg"
  "msg/VacuumGripperState.msg"
  "msg/KitTray.msg"
  "msg/TrayContents.msg"
)

set(SRV_FILES
  "srv/AGVControl.srv"
  "srv/GetMaterialLocations.srv"
  "srv/SubmitTray.srv"
  "srv/PopulationControl.srv"
  "srv/VacuumGripperControl.srv"
  "srv/ConveyorBeltControl.srv"
  "srv/ConvertMetresToFeet.srv"
)

set(ACTION_FILES
  "action/CounterWithDelay.action"
)

rosidl_generate_interfaces(${PROJECT_NAME}
  ${MSG_FILES}
  ${SRV_FILES}
  ${ACTION_FILES}
  DEPENDENCIES builtin_interfaces std_msgs geometry_msgs
)

ament_export_dependencies(rosidl_default_runtime)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

install(DIRECTORY msg srv action
  DESTINATION share/${PROJECT_NAME}
  PATTERN "*.swp" EXCLUDE
)

ament_package()
