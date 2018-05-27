cmake_minimum_required(VERSION 3.10)
project(essentia_test)

#set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD 11)

add_executable(essentia_test main.cpp)

#g++ -pipe -Wall -O2 -fPIC -I/usr/local/include/essentia/ -I/usr/local/include/essentia/scheduler/ -I/usr/local/include/essentia/streaming/  -I/usr/local/include/essentia/utils -I/usr/include/taglib
#-I/usr/local/include/gaia2 -I/usr/include/qt4 -I/usr/include/qt4/QtCore -D__STDC_CONSTANT_MACROS standard_mfcc.cpp -o standard_mfcc -L/usr/local/lib -lessentia -lfftw3 -lyaml -lavcodec
#-lavformat -lavutil -lsamplerate -ltag -lfftw3f -lQtCore -lgaia2

include_directories(/usr/local/include/essentia)
include_directories(/usr/local/include/essentia/scheduler)
include_directories(/usr/local/include/essentia/streaming)
include_directories(/usr/local/include/essentia/utils)
include_directories(/usr/local/include/essentia/taglib)
include_directories(/usr/local/include/gaia2)
#include_directories(/usr/include/qt4)
#include_directories(/usr/include/qt4/QtCore)

link_directories(/usr/local/lib)

find_library(AVCODEC avcodec)
find_library(AVFORMAT avformat)
find_library(AVUTIL avutil)
find_library(SAMPLERATE samplerate)
find_library(AVRESAMPLE avresample)

message("AVCODEC " ${AVCODEC})
message("AVFORMAT " ${AVFORMAT})
message("AVUTIL " ${AVUTIL})
message("SAMPLERATE " ${SAMPLERATE})
message("AVRESAMPLE " ${AVRESAMPLE})

target_link_libraries(essentia_test essentia)
target_link_libraries(essentia_test yaml)
target_link_libraries(essentia_test ${AVCODEC})
target_link_libraries(essentia_test ${AVFORMAT})
target_link_libraries(essentia_test ${AVUTIL})
#target_link_libraries(essentia_test libav)
target_link_libraries(essentia_test ${SAMPLERATE})
target_link_libraries(essentia_test tag)
target_link_libraries(essentia_test fftw3f)
target_link_libraries(essentia_test ${AVRESAMPLE})
#target_link_libraries(essentia_test QtCore)
#target_link_libraries(essentia_test gaia2)
