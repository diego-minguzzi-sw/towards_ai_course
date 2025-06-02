#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Diego Minguzzi 2025

##################################################################################################
class ExceededCapacityException( Exception):

  #-----------------------------------------------------------------------------------------------
  def __init__( self, message: str):
    super().__init__(message)



