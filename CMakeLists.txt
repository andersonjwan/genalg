cmake_minimum_required(VERSION 3.18)

# project name and version
project(genalg VERSION 0.0.1)

# compilation standards
set(CXX_STANDARD 20)
set(CXX_STANDARD_REQUIRED ON)

option(MATPLOTPLUSPLUS "Enable Matplot++ for visualizations" OFF)

add_subdirectory(src)
add_subdirectory(examples)
add_subdirectory(external)
