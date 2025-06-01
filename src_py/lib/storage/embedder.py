#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Diego Minguzzi 2025
import abc

Embedding = list[ float]

class Embedder:
  @abc.abstractmethod
  def embedDocument(self, doc: str) -> Embedding:
    raise NotImplementedError()

  def embedDocuments(self, docs: list[str]) -> list[Embedding]:
    raise NotImplementedError()

  def modelId( self) -> str:
    raise NotImplementedError()

  def embeddingSize(self) -> int:
    """ Returns the size of the embedding vector. """
    raise NotImplementedError()
