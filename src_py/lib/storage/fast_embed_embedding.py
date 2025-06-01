#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Diego Minguzzi 2025
import storage

import fastembed as fe
import logging as log
import time

# Check
# https://qdrant.github.io/fastembed/Getting%20Started/#quick-start

class FastEmbedEmbedder( storage.Embedder):
  def __init__( self, modelId= 'BAAI/bge-base-en'):
    if not type(modelId) is str:
      raise TypeError('modelId should be a string or None')
    else:

      for model in fe.TextEmbedding.list_supported_models():
        id, dim = model['model'], model['dim']
        if id == modelId:
          self._embeddingSize= int( dim)
          self._modelId= id
          log.info(f'Found modelId:{self._modelId} embedding size:{self._embeddingSize}')

        if (self._modelId is None) or (self._embeddingSize is None):
          raise ValueError(f'Model {modelId} not supported.')

      self._textEmbedding= fe.TextEmbedding( self._modelId)

  def embedDocument(self, doc: str) -> storage.Embedding:
    embeddingsGenerator = self._textEmbedding.embed( [doc])
    return list(embeddingsGenerator)[0]

  def embedDocuments(self, docs: list[str]) -> list[storage.Embedding]:
    embeddingsGenerator = self._textEmbedding.embed( docs)
    return list(embeddingsGenerator)

  def modelId( self) -> str:
    return self._modelId

  def embeddingSize(self) -> int:
    return self._embeddingSize

if __name__ == "__main__":
  def main():
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

    print(f'Text to embed: {text}')
    supportedModels = fe.TextEmbedding.list_supported_models()
    for model in supportedModels:
      model, dim, description = model['model'], model['dim'], model['description'][:80]
      print(f'{model[:40]:<40}, {dim:>4}, {description}')

    embedder= FastEmbedEmbedder()
    embeddingSize= embedder.embeddingSize()
    print(f'Embedding size:{embeddingSize}')

    embedding = embedder.embedDocument( text)
    start_time = time.time()
    numIterations= 10
    for _ in range(numIterations):
      embedding = embedder.embedDocument(text)
    end_time = time.time()

    average_time = (end_time - start_time) / numIterations
    print(f'Average time for embedding: {average_time:.6f} seconds')

    print(f'Embedding size:{len(embedding)}')
    assert embeddingSize == len( embedding)

    print(f'Embedding:{embedding[:10]}')

  log.basicConfig(level=log.INFO, format='%(asctime)s %(levelname)s %(funcName)s:%(lineno)d: %(message)s - ')
  main()

