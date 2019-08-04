# Original .bashrc
source /etc/skel/.bashrc

# ROS
source /opt/ros/melodic/setup.bash

# Autoware
export AUTOWARE_COMPILE_WITH_CUDA=1
source /workspace/install/setup.bash

# CUDA
export PATH="/usr/local/cuda/bin:$PATH"
export LD_LIBRARY_PATH="/usr/local/cuda/lib64:$LD_LIBRARY_PATH"

