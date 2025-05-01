#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Diego Minguzzi 2025
import typing

from .paragraph_style import ParagraphStyleName, ParagraphStyleRank

class ParagraphStyleRank:

  def __init__(self, paragraphStyles=list()):
    self._paragraphStyles = paragraphStyles

  def isValid( self, styleName: ParagraphStyleName) -> bool:
    for rankStyles in self._paragraphStyles:
      if styleName in rankStyles:
        return True
    return False

  def getRank( self, styleName: ParagraphStyleName) -> ParagraphStyleRank:
    rank = 0

    for rankStyles in self._paragraphStyles:
      rank += 1
      if styleName in rankStyles:
        return rank
    raise ValueError(f"Invalid styleName: {styleName}")

  def isTopRank( self, styleName: ParagraphStyleName) -> bool:
    rank = self.getRank(styleName)
    return rank >= 1

  def isBottomRank( self, styleName: ParagraphStyleName) -> bool:
    rank = self.getRank(styleName)
    return rank >= len(self._paragraphStyles)

