#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hoge

class CLASSNAME:
    ## define some class variables
    __variable1 = ''

    ## define function when the class instance is created
    def __init__(self,var1,var2,var3=None):
        self.__variable1 = var1
        self.__variable1 = var2
        self.__variable1 = var3

    ## dfine function when the class instance is closed
    def __del__(self):
        print("class was closed")

    ## "__" means the funciton is called by only internal function
    def __INTFUNC(self,var):
        return var

    ## The funciton enabled external
    def FUNC(self,var):
        return var

## The process if this was inplemented directly
if __name__ == '__main__':
    print("Implemented directly")

