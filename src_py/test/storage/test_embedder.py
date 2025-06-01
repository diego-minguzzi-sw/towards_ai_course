#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Diego Minguzzi 2025
from storage import Embedder, EmbedderEnum, EmbedderFactory

import logging as log
import unittest

#---------------------------------------------------------------------------------------------------
class TestEmbedder(unittest.TestCase):

  def testEmbedder(self):
    text = (
      "Artificial intelligence (AI) is a branch of computer science that aims to create machines "
      "that can perform tasks that typically require human intelligence. These tasks include "
      "learning, reasoning, problem-solving, perception, and language understanding. AI has "
      "become an integral part of modern technology, powering applications such as virtual assistants, "
      "recommendation systems, autonomous vehicles, and more. The field of AI encompasses various "
      "subfields, including machine learning, natural language processing, computer vision, and robotics. "
      "Machine learning, a subset of AI, focuses on developing algorithms that allow computers to learn "
      "from and make predictions based on data. Natural language processing enables machines to understand "
      "and generate human language, while computer vision allows them to interpret visual information. "
      "Robotics combines AI with mechanical engineering to create intelligent machines capable of performing "
      "physical tasks. As AI continues to evolve, it raises important ethical and societal questions, such as "
      "privacy concerns, job displacement, and the potential for bias in decision-making. Despite these challenges, "
      "AI holds immense promise for improving efficiency, enhancing decision-making, and solving complex problems "
      "across various industries."
    )

    embedder = EmbedderFactory.createEmbedder()
    embeddingSize= embedder.embeddingSize()
    log.info(f'Embedding size:{embeddingSize}')

    embedding = embedder.embedDocument(text)
    self.assertEqual( len( embedding), embeddingSize)


#---------------------------------------------------------------------------------------------------
if __name__ == '__main__':
  unitTestLoglevel =log.ERROR
  log.basicConfig( level=unitTestLoglevel, format='%(asctime)s - %(levelname)s - %(message)s')

  unittest.main()
