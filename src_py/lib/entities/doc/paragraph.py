#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Diego Minguzzi 2025

from typing import List
import copy

##################################################################################################
class Paragraph:

  #-----------------------------------------------------------------------------------------------
  def __init__(self, text= list()):
    if list!=type(text):
      raise TypeError('text')
    self._text= copy.deepcopy( text)

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