#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Diego Minguzzi 2025
from .paragraph_style_rank import ParagraphStyleRank

class WordDocumentProfile:

  def __init__(self, paragraphStyleRank=None):
    if paragraphStyleRank is None:
      self._paragraphStyleRank = WordDocumentProfile.createDefaultParagraphStyleRank()

  @property
  def paragraphStyleRank(self):
    return self._paragraphStyleRank

  @staticmethod
  def createDefaultParagraphStyleRank():
      ranks= [['Title'],
              ['Heading 1'],
              ['Heading 2'],
              ['Heading 3'],
              ['Heading 4'],
              ['Heading 5'],
              ['Heading 6'],
              ['Normal','No Spacing','List Paragraph','Body Text','Code','Table Paragraph']
      ]
      return ParagraphStyleRank( ranks)