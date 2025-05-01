#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Diego Minguzzi 2025
from .document_reader import DocumentReader
from entities.doc import Document
from entities.doc import Metadata

import docx
import os

class WordDocumentReader(DocumentReader):

  def readDocument(self, filepath: str) -> Document:
    metadata =metadata = Metadata.createFromFilepath( filepath)
    wordDoc = docx.Document( filepath)

    tmpTitle = os.path.splitext(os.path.basename(filepath))[0]
    result= Document( tmpTitle, metadata)
    indxParagraph=0

  """
  0== documentRank
  def rootTraverse( parentSection=None, parentRank=0, )
    fistRank
    if firstRank is textRank:
      rootSection = Section()
      currParagraph= traverseParagraph( iter, rootSection)
      add the paragraph to the root section
    else:
      set the firstRank
      section = traverseSection( iter, sectionRank, sectionTitle, parentSection=None, parentRank=0)

  def traverseSection( iter, sectionRank, sectionTitle, parentSection, parentRank):
    if nextRank is textRank:
      currParagraph= traverseParagraph( iter, rootSection)
    if nextRank >= sectionRank
      reject next
      return Section(sectionRank, sectionTitle)
    if nextRank < sectionRank
      section = Section(sectionRank, sectionTitle)
      childSection= traverseSection( iter, nextRank, sectionTitle, section, sectionRank):
      add childSection to parent
      return section

  """


  def traverseDocument():
    """
    start at the first paragraph
    prevRank = textRank
    currSection = empty Section

    while currRank == prevRank == textRank
      add the text to the current paragraph



    if currRank == prevRank == textRank


    if currRank > prevRank:
      add the current paragraph and section to the
       if
    """
    pass