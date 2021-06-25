cmake_minimum_required(VERSION 3.10)

project(getzipgit VERSION 0.0.1)

install(PROGRAMS bin/getzipgit DESTINATION bin)
install(FILES README.md DESTINATION TYPE DATA)
install(FILES LICENSE DESTINATION TYPE DATA)
