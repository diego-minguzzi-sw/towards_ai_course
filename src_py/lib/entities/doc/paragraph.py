#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Diego Minguzzi 2025

from entities.doc import Figure
from typing import List
import copy

##################################################################################################
class Paragraph:
  """ A Paragraph of a document. """
  #-----------------------------------------------------------------------------------------------
  def __init__(self, text= list(), figures: List[Figure]= list()):
    if list!=type(text):
      raise TypeError('text')
    self._text= copy.deepcopy( text)

    self._figures= list()
    self.addFigures( figures)

  #-----------------------------------------------------------------------------------------------
  def setText(self, text: List[str]):
    if List[str]!=type(text):
      raise TypeError('text')
    self._text= copy.deepcopy( text)

  #-----------------------------------------------------------------------------------------------
  @property
  def text(self) -> List[str]:
    return self._text

  #-----------------------------------------------------------------------------------------------
  def allText(self) -> str:
    return '\n'.join(self._text)

  #-----------------------------------------------------------------------------------------------
  def addTextRow(self, textRow: str):
    if str != type(textRow):
      raise TypeError('textRow')
    self._text.append( textRow)

  #-----------------------------------------------------------------------------------------------
  def numTextLines(self) -> int:
    return len(self._text)

  #-----------------------------------------------------------------------------------------------
  def addFigure(self, figure: Figure):
    """ The paragraph stores a reference to the figure, it does not perform a copy of the figure.
    """
    if Figure != type(figure):
      raise TypeError('figure')
    self._figures.append( figure)

  #-----------------------------------------------------------------------------------------------
  def addFigures(self, figures: list):
    if (len(figures)>0) and ( list != type(figures)):
      raise TypeError('figures')

    for figure in figures:
      self.addFigure( figure)

  #-----------------------------------------------------------------------------------------------
  @property
  def hasFigures(self) -> bool:
    return len(self._figures)>0

  #-----------------------------------------------------------------------------------------------
  @property
  def numFigures(self) -> int:
    return len(self._figures)

  #-----------------------------------------------------------------------------------------------
  def figures(self) -> List[Figure]:
    return self._figures