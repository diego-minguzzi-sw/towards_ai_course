#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Diego Minguzzi 2025

ParagraphStyleRank = int
ParagraphStyleName = str

class ParagraphStyle:
  def __init__(self, name: ParagraphStyleName, rank: ParagraphStyleRank):
    if str != type(name):
      raise TypeError('name')

    if int != type(rank):
      raise TypeError('rank')

    if rank<0:
      raise ValueError('rank')

    self._name = name
    self._rank = rank

  @property
  def name(self) -> str:
    return self._name

  @property
  def rank(self) -> int:
    return self._rank

  def __str__( self) -> str:
    return f'(name:{self._name} rank:{self._rank})'
