cmake_minimum_required(VERSION 3.17)
project(j_image_addon VERSION 0.1)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_INCLUDE_CURRENT_DIR ON)

set(SRC_DIR ${CMAKE_CURRENT_SOURCE_DIR}/src/)

set(MAIN_SRC
        ${SRC_DIR}/imageHandler.cpp
        ${SRC_DIR}/imageHandler.h
        ${SRC_DIR}/main.cpp
        )

# CMAKE_PREFIX_PATH for local
set(CMAKE_PREFIX_PATH /Users/justin/lib_source/ImageMagick-7.0.10)

find_path(IMAGEMAGICK_INCLUDE_DIR ImageMagick-7)
find_library(IMAGEMAGICK_LIBRARIES Magick++-7.Q16HDRI)

add_library(j_image_addon ${MAIN_SRC})

target_include_directories(
    j_image_addon PUBLIC ${IMAGEMAGICK_INCLUDE_DIR}
)

target_link_libraries(
    j_image_addon PUBLIC ${IMAGEMAGICK_LIBRARIES}
)
