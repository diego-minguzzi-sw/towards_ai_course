#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Diego Minguzzi 2025
import storage

from google import genai
from google.genai import types

import exc
import json
import logging as log
import pprint
import time

#--------------------------------------------------------------------------------------------------
class GoogleGenAIEmbedder( storage.Embedder):
  QUERY_TASK = 'RETRIEVAL_QUERY'
  STORE_TASK = 'RETRIEVAL_DOCUMENT'
  ERROR_CODE_QUOTA_EXCEEDED = 429

  #------------------------------------------------------------------------------------------------
  def __init__( self, modelId= 'text-embedding-004'):
    self._supportedTasks= [self.QUERY_TASK, self.STORE_TASK]

    if not type(modelId) is str:
      raise TypeError('modelId should be a string or None')
    else:
      self._modelId= modelId

      self._client= genai.Client()

      # Issues an example request to determine the embedding size.
      embeddings= self._executeSingleRequest(text='Text',
                                             taskType=GoogleGenAIEmbedder.QUERY_TASK)
      self._embeddingSize= len(embeddings)
      log.info(f'Embedding size: {self._embeddingSize}')

  #------------------------------------------------------------------------------------------------
  def embedDocument(self, doc: str) -> storage.Embedding:
    return self._executeSingleRequest( doc, GoogleGenAIEmbedder.STORE_TASK)

  #------------------------------------------------------------------------------------------------
  def embedDocuments(self, docs: list[str]) -> list[ storage.Embedding]:
    return self._executeBatchRequest( docs, GoogleGenAIEmbedder.STORE_TASK)

  #------------------------------------------------------------------------------------------------
  def embedQuery(self, doc: str) -> storage.Embedding:
    return self._executeSingleRequest( doc, GoogleGenAIEmbedder.QUERY_TASK)

  #------------------------------------------------------------------------------------------------
  def embedQueries(self, docs: list[str]) -> list[ storage.Embedding]:
    return self._executeBatchRequest( docs, GoogleGenAIEmbedder.QUERY_TASK)

  #------------------------------------------------------------------------------------------------
  def modelId( self) -> str:
    return self._modelId

  #------------------------------------------------------------------------------------------------
  def embeddingSize(self) -> int:
    return self._embeddingSize

  #------------------------------------------------------------------------------------------------
  def _executeSingleRequest( self, text: str, taskType:str):
    if taskType not in self._supportedTasks:
      raise ValueError(f'Task:\'{taskType}\' not supported.')

    try:
      result = self._client.models.embed_content(
          model=self._modelId,
          contents=text,
          config=types.EmbedContentConfig(task_type=taskType) )
      embeddings= result.embeddings[0].values
      log.debug(f'Embeddings type:{type(embeddings)}, Item type:{type(embeddings[0])} length:{len(embeddings)}')
      return embeddings

    except genai.errors.ClientError as e:
      excMessage= e.message
      if self.ERROR_CODE_QUOTA_EXCEEDED == e.code:
        log.error('GenAI Client error: exceeded Google usage limit.')
        raise exc.ExceededCapacityException(excMessage) from e

      raise RuntimeError(f'GenAI Client error: {excMessage}') from e

  #------------------------------------------------------------------------------------------------
  def _executeBatchRequest( self, texts: list[str], taskType:str) -> list[storage.Embedding]:
    if taskType not in self._supportedTasks:
      raise ValueError(f'Task:\'{taskType}\' not supported.')

    try:
      result = self._client.models.embed_content(
          model=self._modelId,
          contents=texts,
          config=types.EmbedContentConfig(task_type=taskType) )
      embeddingsResult= list()
      for embeddingsItem in result.embeddings:
        embeddingsValues = embeddingsItem.values
        log.debug(f'Embeddings type:{type(embeddingsValues)}, item type:{type(embeddingsValues[0])} length:{len(embeddingsValues)}')
        embeddingsResult.append(embeddingsValues)
      return embeddingsResult

    except genai.errors.ClientError as e:
      excMessage= e.message
      if self.ERROR_CODE_QUOTA_EXCEEDED == e.code:
        log.error('GenAI Client error: exceeded Google usage limit.')
        raise exc.ExceededCapacityException(excMessage) from e

      raise RuntimeError(f'GenAI Client error: {excMessage}') from e

#--------------------------------------------------------------------------------------------------

if __name__ == "__main__":
  #------------------------------------------------------------------------------------------------
  def testModel( embedder, numIterations: int, text: str):

    start_time = time.time()
    for _ in range(numIterations):
      embedding = embedder.embedDocument(text)
      assert embedder.embeddingSize() == len(embedding)
    end_time = time.time()

    average_time = (end_time - start_time) / numIterations
    print(f'\n{embedder.modelId()} {numIterations} iterations. Average time for embedding: {average_time:.6f} seconds')

  #------------------------------------------------------------------------------------------------
  def testModelOnBatch( embedder, batchSize: int, text: str):

    texts = [text] * batchSize

    start_time = time.time()
    embeddings = embedder.embedDocuments(texts)
    end_time = time.time()
    average_time = (end_time - start_time)/batchSize

    assert batchSize == len(embeddings)
    if batchSize> 0:
      assert embedder.embeddingSize() == len(embeddings[0])

    print(f'\nBATCH {embedder.modelId()} Batch size:{batchSize}. Time per embedding: {average_time:.6f} seconds')

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

    embedder= GoogleGenAIEmbedder()
    assert embedder is not None


    try:
      testModel( embedder, numIterations=1000, text=text)

      testModelOnBatch( embedder, batchSize=5, text=text)

    except exc.ExceededCapacityException as e:
      log.error(f'ExceededCapacityException caught:\n{e}')
    except Exception as e:
      log.error(f'Exception caught:\n{e}')


  log.basicConfig(level=log.INFO, format='%(asctime)s %(levelname)s %(funcName)s:%(lineno)d: %(message)s - ')
  main()

