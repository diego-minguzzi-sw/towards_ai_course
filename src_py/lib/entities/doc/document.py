#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Diego Minguzzi 2025
from entities.doc import Metadata, Section

from typing import List
import copy

##################################################################################################
class Document:
  """ Document entity, composes of metadata and a tree of Sections.
  """
  #-----------------------------------------------------------------------------------------------
  def __init__( self,
                title: str,
                metadata: Metadata,
                rootSection: Section):
    if str!=type(title):
      raise TypeError('title')

    if Metadata!=type(metadata):
      raise TypeError('metadata')

    if Section!=type(rootSection):
      raise TypeError('rootSection')

    if rootSection is None:
      raise ValueError('rootSection')

    self._title= title
    self._metadata = copy.deepcopy(metadata)
    self._rootSection= rootSection

  @property
  def title( self): return self._title

  @property
  def rootSection( self): return self._rootSection

  @property
  def metadata( self): return self._metadata

  def visitSectionsDepthFirst(self, visitor: callable):
    """  visitor accepts a Section as only argument. """

    def _visit(section: Section):
      visitor(section)
      for subsection in section.subsections:
        _visit( subsection)

    _visit(self._rootSection)


