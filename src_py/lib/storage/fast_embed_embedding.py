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
      self._modelId= None

      for model in fe.TextEmbedding.list_supported_models():
        id, dim = model['model'], model['dim']
        log.debug(f'modelId:\"{id}\", size:{dim}')
        if str(id) == str(modelId):
          self._embeddingSize= int( dim)
          self._modelId= id
          log.info(f'Found modelId:{self._modelId} embedding size:{self._embeddingSize}')

      if self._modelId is None:
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
  #------------------------------------------------------------------------------------------------
  def testModel( embedder, numIterations: int, text: str):
    embeddingSize= embedder.embeddingSize()
    print(f'Embedding size:{embeddingSize}')

    start_time = time.time()
    numIterations= 10
    for _ in range(numIterations):
      embedding = embedder.embedDocument(text)
      assert embeddingSize == len( embedding)
    end_time = time.time()

    average_time = (end_time - start_time) / numIterations
    print(f'\n{embedder.modelId()} {numIterations} iterations. Average time for embedding: {average_time:.6f} seconds')

  #------------------------------------------------------------------------------------------------
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
    print(f'Text to embed: {text}\n')

    for model in fe.TextEmbedding.list_supported_models():
      model, dim, description = model['model'], model['dim'], model['description'][:100]
      print(f'{model[:40]:<40}, {dim:>4}, {description}')

    embedder= FastEmbedEmbedder( modelId='nomic-ai/nomic-embed-text-v1.5')
    testModel( embedder, numIterations=10, text= text)

    embedder= FastEmbedEmbedder( modelId='BAAI/bge-base-en')
    testModel( embedder, numIterations=10, text= text)

    # embedder= FastEmbedEmbedder( modelId='jinaai/jina-embeddings-v3')
    # testModel( embedder, numIterations=10, text= text)

  log.basicConfig(level=log.ERROR, format='%(asctime)s %(levelname)s %(funcName)s:%(lineno)d: %(message)s - ')
  main()

