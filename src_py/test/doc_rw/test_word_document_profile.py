#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Diego Minguzzi 2025

from doc_rw import ParagraphStyle, WordDocumentProfile

import logging as log
import unittest
from collections import namedtuple



#---------------------------------------------------------------------------------------------------
class TestParagraphStyle(unittest.TestCase):

  def testCreate(self):
    obj = WordDocumentProfile()

  def testRanks(self):
    wantRanks= [ParagraphStyle('Title', 1),
                ParagraphStyle('Heading 1', 2),
                ParagraphStyle('Heading 2', 3),
                ParagraphStyle('Heading 3', 4),
                ParagraphStyle('Heading 4', 5),
                ParagraphStyle('Heading 5', 6),
                ParagraphStyle('Heading 6', 7),
                ParagraphStyle('Normal', 8),
                ParagraphStyle('No Spacing', 8),
                ParagraphStyle('List Paragraph', 8)
              ]
    obj = WordDocumentProfile()
    paragraphStyleRank = obj.paragraphStyleRank
    for wantRank in wantRanks:
      log.debug(f'Testing wantRank: {wantRank}')
      self.assertTrue( paragraphStyleRank.isValid( wantRank.name))

      if ( paragraphStyleRank.isValid( wantRank.name)):
        gotRank= paragraphStyleRank.getRank( wantRank.name)
        log.debug(f'gotRank: {gotRank} wantRank:{wantRank.rank}')
        self.assertTrue( gotRank== wantRank.rank)

#---------------------------------------------------------------------------------------------------
if __name__ == '__main__':
  unitTestLoglevel =log.DEBUG
  log.basicConfig( level=unitTestLoglevel, format='%(asctime)s - %(levelname)s - %(message)s')

  unittest.main()

