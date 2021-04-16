cmake_minimum_required(VERSION 3.17)
project(j_image_addon VERSION 0.1)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_INCLUDE_CURRENT_DIR ON)

set(NODE_MODULES_DIR ${CMAKE_CURRENT_LIST_DIR}/node_modules)
set(SRC_DIR ${CMAKE_CURRENT_LIST_DIR}/src)
set(MAIN_SRC
        ${SRC_DIR}/imageHandler.cpp
        ${SRC_DIR}/imageHandler.h
        ${SRC_DIR}/main.cpp
        )

# CMAKE_PREFIX_PATH for local
list(APPEND CMAKE_PREFIX_PATH "/Users/justin/lib_source/ImageMagick-7.0.10" "${NODE_MODULES_DIR}")

find_path(IMAGEMAGICK_INCLUDE_DIR ImageMagick-7)
find_library(IMAGEMAGICK_LIBRARIES Magick++-7.Q16HDRI)

find_path(NODE_ADDON_API_INCLUDE_DIR node-addon-api)

add_library(${PROJECT_NAME} SHARED ${MAIN_SRC} ${CMAKE_JS_SRC})
set_target_properties(${PROJECT_NAME} PROPERTIES PREFIX "" SUFFIX ".node")
target_include_directories(
    ${PROJECT_NAME} PRIVATE ${IMAGEMAGICK_INCLUDE_DIR} ${NODE_ADDON_API_INCLUDE_DIR}
)
target_link_libraries(
    ${PROJECT_NAME} PRIVATE ${IMAGEMAGICK_LIBRARIES}
)

# define NPI_VERSION
add_definitions(-DNAPI_VERSION=3)
