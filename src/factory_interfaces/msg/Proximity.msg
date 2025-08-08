# Single reading from a binary proximity sensor that detects the presence of
# objects within its sensing range.
std_msgs/Header header           # timestamp when the sensor reading was taken
bool object_detected             # is there something in the proximity of the sensor?
float32 min_range                # minimum range value [m]
float32 max_range                # maximum range value [m]
