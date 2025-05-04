#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Diego Minguzzi 2025
from .document_reader import DocumentReader
from .word_document_profile import WordDocumentProfile
from entities.doc import Document, Metadata, Paragraph, Section

import docx
import logging as log
import os
import typing

class WordDocumentReader(DocumentReader):

  def __init__( self, stripParagraphs: bool= True):
    super().__init__()
    self._docProfile= WordDocumentProfile()
    self._parStyleRank= self._docProfile.paragraphStyleRank

    self._stripParagraphs= stripParagraphs

  def readDocument(self, filepath: str) -> Document:
    metadata = Metadata.createFromFilepath( filepath)

    tmpTitle = os.path.splitext(os.path.basename(filepath))[0]

    indxParagraph=0

    wordDoc = docx.Document(filepath)
    paragraphs= wordDoc.paragraphs

    if len(paragraphs)==0:
      return Document( '', metadata)

    rootSection= Section()

    par= paragraphs[indxParagraph]
    parStyleName= par.style.name

    while indxParagraph < len(paragraphs):
      indx = self._traverseSection( paragraphs=paragraphs,
                                    indxParagraph=indxParagraph,
                                    parentSection=rootSection)
      indxParagraph= indx

    return Document( tmpTitle, metadata, rootSection)

  #------------------------------------------------------------------------------------------------
  def _traverseSection( self,
                        paragraphs,
                        indxParagraph: int,
                        parentSection: Section,
                        parentRank:int=0) -> int:
    indx = indxParagraph

    par= paragraphs[indx]
    parStyleName= par.style.name

    if self._parStyleRank.isTextRank( parStyleName):
      (indx, paragraph) = self._traverseParagraph( paragraphs, indx)
      currSection= parentSection.createSubsection( paragraph=paragraph)

    else:
      while indx<len(paragraphs):
        par= paragraphs[indx]
        parStyleName= par.style.name
        assert( not self._parStyleRank.isTextRank( parStyleName))

        sectRank = self._parStyleRank.getRank( parStyleName)
        if sectRank <= parentRank:
          return indx

        sectionTitle= par.text

        if (indx+1) >= len(paragraphs):
          currSection= parentSection.createSubsection( title= sectionTitle, paragraph=Paragraph())
          return indx+1 # TODO
        else:
          nextIndx= indx+1
          nextPar= paragraphs[ nextIndx]
          nextParName= nextPar.style.name
          nextRank = self._parStyleRank.getRank( nextParName)

          if self._parStyleRank.isTextRank( nextParName):
            (indx, paragraph) = self._traverseParagraph( paragraphs, nextIndx)
            if indx>=len(paragraphs):
              currSection= parentSection.createSubsection( title= sectionTitle, paragraph=paragraph)
              return indx

            nextIndx= indx
            nextPar= paragraphs[ nextIndx]
            nextParName= nextPar.style.name
            assert( not self._parStyleRank.isTextRank( nextParName))
            nextRank = self._parStyleRank.getRank( nextParName)
          else:
            paragraph= Paragraph()

          currSection= parentSection.createSubsection( title= sectionTitle, paragraph=paragraph)

          nextRank = self._parStyleRank.getRank( nextParName)
          if sectRank < nextRank:
            indx = self._traverseSection(paragraphs, nextIndx, currSection, sectRank)
          elif nextRank <= parentRank:
            return nextIndx
          else:
            indx = nextIndx

    return indx

  #------------------------------------------------------------------------------------------------
  def _traverseParagraph(self,
                         paragraphs,
                         indxParagraph: int) -> typing.Tuple[int, Paragraph]:
    indx= indxParagraph
    textRows= list()

    hasFoundNonEmptyRow= False

    while indx < len(paragraphs):
      parStyleName= paragraphs[indx].style.name

      if self._parStyleRank.isTextRank( parStyleName):
        rowText= paragraphs[indx].text

        if self._stripParagraphs:
          isRowEmpty= (0==len(rowText.strip()))
          if (not hasFoundNonEmptyRow) and isRowEmpty:
            indx += 1
            continue
          if not isRowEmpty:
            hasFoundNonEmptyRow= True

        textRows.append(rowText)
        indx += 1
      else:
        break

    if self._stripParagraphs:
      while len(textRows)>0 and not textRows[-1].strip():
        textRows.pop()

    return (indx, Paragraph( textRows))
