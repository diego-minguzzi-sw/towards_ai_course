#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Diego Minguzzi 2025
from entities.doc import Paragraph

from typing import List
import copy

##################################################################################################
class Section:

  def __init__( self,
                title: str= '',
                paragraph: Paragraph= Paragraph(),
                parentSection=None,
                depth: int=0):
    if str != type(title):
      raise TypeError('title')

    if Paragraph != type(paragraph):
      raise TypeError('paragraph')

    if int != type(depth):
      raise TypeError('depth')

    self._title= title
    self._paragraph= copy.deepcopy( paragraph)
    self._parentSection= parentSection
    self._subSections= list()
    self._depth= depth

  @property
  def title( self): return self._title

  @property
  def paragraph( self): return self._paragraph

  @property
  def hasParentSection( self) -> bool:
    return None != self._parentSection

  def parentSection( self):
    return self._parentSection

  def parentTitle( self, rootTitle:str='') -> str:
    if self._parentSection is None:
      return rootTitle
    return self._parentSection.title

  def isRootSection( self) -> bool:
    return None == self._parentSection

  def hasParentSection( self) -> bool:
    return None != self._parentSection

  def createSubsection( self,
                        title: str= '',
                        paragraph: Paragraph= Paragraph()):
    newSection= Section(title=title,
                        paragraph=paragraph,
                        parentSection=self,
                        depth=self._depth+1)
    self._subSections.append(newSection)
    return newSection

  @property
  def subsections( self): return self._subSections

  @property
  def numSubsections( self) -> int: return len( self._subSections)

  @property
  def depth( self) -> int: return self._depth

  def __str__(self):
    return f'(title:{self._title} depth:{self._depth})'