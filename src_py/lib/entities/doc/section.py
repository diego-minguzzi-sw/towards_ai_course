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
                parentSection=None):
    if str != type(title):
      raise TypeError('title')

    if Paragraph != type(paragraph):
      raise TypeError('paragraph')

    self._title= title
    self._paragraph= copy.deepcopy( paragraph)
    self._parentSection= None
    self._subSections= list()

  @property
  def title( self): return self._title

  @property
  def paragraph( self): return self._paragraph

  @property
  def hasParentSection( self) -> bool:
    return None != self._parentSection

  def parentSection( self):
    return self._parentSection

  def createSubsection( self,
                        title: str= '',
                        paragraph: Paragraph= Paragraph()):
    newSection= Section(title=title,
                        paragraph=paragraph,
                        parentSection=self)
    self._subSections.append(newSection)
    return newSection

  @property
  def subsections( self): return self._subSections

  @property
  def numSubsections( self) -> int: return len( self._subSections)

  def __str__(self):
    return f'(title:{self._title})'