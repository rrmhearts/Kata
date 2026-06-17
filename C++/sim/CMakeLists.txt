cmake_minimum_required(VERSION 3.10)
project(OpenGLWindow)

set(CMAKE_CXX_STANDARD 17)

# Include directories for Glad and GLFW headers
include_directories(include)

# Add your executable and source files (include glad.c here)
add_executable(OpenGLWindow src/main.cpp src/glad.c)

# Find and link GLFW and system OpenGL
find_package(glfw3 REQUIRED)
target_link_libraries(OpenGLWindow glfw GL dl)
