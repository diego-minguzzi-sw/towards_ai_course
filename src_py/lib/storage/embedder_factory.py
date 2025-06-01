#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Diego Minguzzi 2025

from .embedder import Embedder
from .embedder_enum import EmbedderEnum
from .fast_embed_embedding import FastEmbedEmbedder

import logging as log

#--------------------------------------------------------------------------------------------------
class EmbedderFactory:

  @staticmethod
  def createEmbedder( embedder= EmbedderEnum.FastEmbedDefault) -> Embedder:
    log.info(f'embedder modelId: {embedder.modelId}')

    match embedder:
      case EmbedderEnum.FastEmbedBase:
        return FastEmbedEmbedder( embedder.modelId)

      case EmbedderEnum.FastEmbedNomicAI:
        return FastEmbedEmbedder( embedder.modelId)

    raise ValueError(f"Unsupported embedder: {embedder.modelId}")




