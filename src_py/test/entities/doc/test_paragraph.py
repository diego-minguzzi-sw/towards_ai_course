#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Diego Minguzzi 2025

from entities.doc import Paragraph

import logging as log
import unittest

#---------------------------------------------------------------------------------------------------
class TestParagraph(unittest.TestCase):

  def testCreate(self):
    obj = Paragraph()

  def testCreateWithText(self):
    obj = Paragraph( ['line 1', 'line 2'])
    self.assertEqual( obj.numTextLines(), 2)

#---------------------------------------------------------------------------------------------------
if __name__ == '__main__':
  unitTestLoglevel =log.ERROR
  log.basicConfig( level=unitTestLoglevel, format='%(asctime)s - %(levelname)s - %(message)s')

  unittest.main()

