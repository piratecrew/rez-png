# -*- coding: utf-8 -*-

name = 'png'

version = '1.6.29'

authors = ['fredrik.brannbacka']

variants = [["platform-linux"]]

def commands():
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")
