#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Diego Minguzzi 2025

from enum import Enum
import logging as log

#--------------------------------------------------------------------------------------------------
class EmbedderEnum(Enum):
  FastEmbedBase = ('BAAI/bge-base-en',)
  FastEmbedNomicAI = ('nomic-ai/nomic-embed-text-v1.5',)
  FastEmbedDefault = FastEmbedNomicAI

  def __init__(self, modelId):
    self._modelId= modelId

  @property
  def modelId(self):
    return self._modelId

if __name__ == "__main__":
  def main():
    log.basicConfig(level=log.ERROR, format='%(asctime)s %(levelname)s %(funcName)s:%(lineno)d: %(message)s - ')
    for embedder in EmbedderEnum:
      print(f'{embedder.name:<20} modelId:{embedder.modelId}')
  main()



