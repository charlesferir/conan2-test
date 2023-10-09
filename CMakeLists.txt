cmake_minimum_required(VERSION 3.0.0)
project(hello VERSION 0.1.0 LANGUAGES C CXX)

find_package(spdlog REQUIRED)

add_executable(hello src/main.cpp)
target_link_libraries(hello spdlog::spdlog)
