#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Diego Minguzzi 2025
from entities.doc import Section

import logging as log
import unittest

#---------------------------------------------------------------------------------------------------
class TestSection(unittest.TestCase):

  def testCreate(self):
    obj = Section( title='The section title')
    log.debug(f'Title:{ obj.title}')


#---------------------------------------------------------------------------------------------------
if __name__ == '__main__':
  unitTestLoglevel =log.ERROR
  log.basicConfig( level=unitTestLoglevel, format='%(asctime)s - %(levelname)s - %(message)s')

  unittest.main()
