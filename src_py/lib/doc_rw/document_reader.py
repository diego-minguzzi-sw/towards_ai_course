#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Diego Minguzzi 2025
import abc
from entities.doc import Document

class DocumentReader:

  @abc.abstractmethod
  def readDocument(self, filepath: str) -> Document:
    pass