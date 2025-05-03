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

  def __init__( self):
    super().__init__()
    self._docProfile= WordDocumentProfile()
    self._parStyleRank= self._docProfile.paragraphStyleRank

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
      indxParagraph = self._traverseSection(paragraphs=paragraphs,
                                            indxParagraph=indxParagraph,
                                            parentSection=rootSection)

    return Document( tmpTitle, metadata, rootSection)

  #------------------------------------------------------------------------------------------------
  def _traverseSection( self,
                        paragraphs,
                        indxParagraph: int,
                        parentSection: Section,
                        parentRank:int=0) -> int:
    # log.debug(f'_traverseSection started: indxParagraph:{indxParagraph}')
    indx = indxParagraph

    par= paragraphs[indx]
    parStyleName= par.style.name

    if self._parStyleRank.isTextRank( parStyleName):
      (indx, paragraph) = self._traverseParagraph( paragraphs, indx)
      currSection= parentSection.createSubsection( paragraph=paragraph)
      log.debug(f'createSubsection: \"{currSection.parentTitle()}\" -> \"{currSection.title}\" depth:{currSection.depth}')
    else:
      while indx<len(paragraphs):
        par= paragraphs[indx]
        parStyleName= par.style.name
        sectRank = self._parStyleRank.getRank( parStyleName)
        if sectRank <= parentRank:
          return indx

        sectionTitle= par.text

        if (indx+1)<len(paragraphs):
          nextIndx= indx+1
          nextPar= paragraphs[ nextIndx]
          nextParName= nextPar.style.name
          if self._parStyleRank.isTextRank( nextParName):
            (indx, paragraph) = self._traverseParagraph( paragraphs, nextIndx)
            if indx>=len(paragraphs):
              currSection= parentSection.createSubsection( title= sectionTitle, paragraph=paragraph)
              log.debug(f'createSubsection: \"{currSection.parentTitle()}\" -> \"{currSection.title}\" depth:{currSection.depth}')
              # log.debug(f'paragraph text:{paragraph.allText()}')
              return indx
            nextIndx= indx
            nextPar= paragraphs[ nextIndx]
            nextParName= nextPar.style.name
          else:
            paragraph= Paragraph()

          currSection= parentSection.createSubsection( title= sectionTitle, paragraph=paragraph)
          log.debug(f'\"{currSection.parentTitle()}\" -> \"{currSection.title}\" {parStyleName} depth:{currSection.depth}')
          # log.debug(f'paragraph text:{paragraph.allText()}')

          nextRank = self._parStyleRank.getRank( nextParName)
          if sectRank < nextRank:
            indx = self._traverseSection(paragraphs, nextIndx, currSection, sectRank)

    return indx

  #------------------------------------------------------------------------------------------------
  def _traverseParagraph(self,
                         paragraphs,
                         indxParagraph: int) -> typing.Tuple[int, Paragraph]:
    indx= indxParagraph
    result = Paragraph()

    while indx < len(paragraphs):
      parStyleName= paragraphs[indx].style.name
      if self._parStyleRank.isTextRank( parStyleName):
        result.addTextRow( paragraphs[indx].text)
        indx += 1
      else:
        break

    return (indx, result)
