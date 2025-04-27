#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Diego Minguzzi 2025
from entities.doc import Document

import logging as log
import unittest

#---------------------------------------------------------------------------------------------------
class TestDocument(unittest.TestCase):

  def testCreate(self):
    wantTitle= 'Document title'
    doc = Document( title=wantTitle)
    log.debug(f'doc.title:{doc.title}')
    self.assertEqual( doc.title, wantTitle)


#---------------------------------------------------------------------------------------------------
if __name__ == '__main__':
  unitTestLoglevel =log.DEBUG
  log.basicConfig( level=unitTestLoglevel, format='%(asctime)s - %(levelname)s - %(message)s')

  unittest.main()
