cmake_minimum_required(VERSION 3.6)

project(TCC)
 
#find_package(OpenCV REQUIRED)

set(OpenCV_INCLUDE_DIRS /usr/local/share/OpenCV)

set(TCC_INCLUDE_DIRS
    ${CMAKE_SOURCE_DIR}
    ${OpenCV_INCLUDE_DIRS}
)

set(TCC_LIBRARIES
    ${OpenCV_LIBS}
)

# The list of examples to be compiled goes here.
set(TCC_EXAMPLES_SOURCES
    hello.cpp
    autocorrection.cpp
    pre_processing.cpp
    homografy.cpp
    orb.cpp
    #gabarito.cpp
    #autocorrection_test.cpp
    histogram.cpp
)

foreach(_source IN ITEMS ${TCC_EXAMPLES_SOURCES})
    # Extract name from filename without suffix and directory.
    # E.g. test/example.cpp -> example
    #      _source          -> _target
    get_filename_component(_target ${_source} NAME_WE)

    # The process of adding an executable.
    add_executable(${_target} src/${_source})
    target_include_directories(${_target} PUBLIC ${TCC_INCLUDE_DIRS})
    target_link_libraries(${_target} PUBLIC ${TCC_LIBRARIES})
endforeach()
