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
    log.debug('readDocument started.')
    metadata = Metadata.createFromFilepath( filepath)

    tmpTitle = os.path.splitext(os.path.basename(filepath))[0]

    indxParagraph=0

    wordDoc = docx.Document(filepath)
    paragraphs= wordDoc.paragraphs

    if len(paragraphs)==0:
      return Document( "", metadata)

    rootSection= Section()

    par= paragraphs[indxParagraph]
    parStyleName= par.style.name

    while indxParagraph < len(paragraphs):
      indxParagraph = self._traverseSection(paragraphs=paragraphs,
                                            indxParagraph=indxParagraph,
                                            parentSection=rootSection)

    log.debug('readDocument terminated.')
    return Document( tmpTitle, metadata, rootSection)

  #------------------------------------------------------------------------------------------------
  def _traverseSection( self,
                        paragraphs,
                        indxParagraph: int,
                        parentSection: Section,
                        parentRank:int=0) -> int:
    log.debug(f'_traverseSection started: indxParagraph:{indxParagraph}')
    indx = indxParagraph

    par= paragraphs[indx]
    parStyleName= par.style.name

    if self._parStyleRank.isTextRank( parStyleName):
      log.debug(f'parStyleName: indx:{indx} {parStyleName}: got text rank.')
      (indx, paragraph) = self._traverseParagraph( paragraphs, indx)
      parentSection.createSubsection( paragraph=paragraph)
    else:
      log.debug(f'parStyleName: indx:{indx} {parStyleName}: got header rank.')
      while indx<len(paragraphs):
        par= paragraphs[indx]
        parStyleName= par.style.name
        sectRank = self._parStyleRank.getRank( parStyleName)
        if sectRank <= parentRank:
          log.debug(f'_traverseSection terminated: indx:{indx}')
          return indx

        sectionTitle= par.text

        if (indx+1)<len(paragraphs):
          nextIndx= indx+1
          nextPar= paragraphs[ nextIndx]
          nextParName= nextPar.style.name
          if self._parStyleRank.isTextRank( nextParName):
            (indx, paragraph) = self._traverseParagraph( paragraphs, nextIndx)
          else:
            paragraph= Paragraph()

          currSection= parentSection.createSubsection( title= sectionTitle, paragraph=paragraph)
          nextRank = self._parStyleRank.getRank( nextParName)
          log.debug(f'parStyleName: indx:{indx} {parStyleName}: sectRank:{sectRank} nextRank:{nextRank}')
          if sectRank < nextRank:
            log.debug('About to call _traverseSection.')
            indx = self._traverseSection(paragraphs, nextIndx, currSection, sectRank)
            log.debug(f'_traverseSection ws executed: indx:{indx}')

    log.debug(f'_traverseSection terminated: indx:{indx}')
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
        log.debug(f'parStyleName: {parStyleName}: text rank. Added to paragraph.')
        result.addTextRow( paragraphs[indx].text)
        indx += 1
      else:
        log.debug(f'parStyleName: {parStyleName}: not text rank. terminating.')
        break

    return (indx, result)

