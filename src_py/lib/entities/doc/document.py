#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Diego Minguzzi 2025
from entities.doc import Metadata
from entities.doc import Section

from typing import List
import copy

##################################################################################################
class Document:
  #-----------------------------------------------------------------------------------------------
  def __init__( self,
                title: str,
                metadata: Metadata,
                rootSection= Section()):
    if str!=type(title):
      raise TypeError('title')

    if Metadata!=type(metadata):
      raise TypeError('metadata')

    if Section!=type(rootSection):
      raise TypeError('rootSection')

    self._title= title
    self._metadata = copy.deepcopy(metadata)
    self._rootSection= copy.deepcopy( rootSection)

  @property
  def title( self): return self._title

  @property
  def rootSection( self): return self._rootSection

  @property
  def metadata( self): return self._metadata

