#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Diego Minguzzi 2025

from typing import List
import argparse
import copy
import datetime as dt
import hashlib
import os

##################################################################################################
class Metadata:
  def __init__(self,
               filename: str,
               digest: bytes,
               creationTime: dt.datetime):
    if str != type(filename):
      raise TypeError('filename')

    if bytes != type(digest):
      raise TypeError('digest')

    if 0==len(digest):
      raise ValueError('digest is empty')

    if dt.datetime != type(creationTime):
      raise TypeError('creationTime')

    self._filename= filename
    self._filepath= os.path.abspath(filename)
    self._digest = digest
    self._creationTime= copy.deepcopy( creationTime)

  @property
  def digest( self):
    return self._digest

  @property
  def filename( self):
    return self._filename

  @property
  def filepath( self):
    return self._filepath

  def __str__( self):
    return f'(filename:{self._filename}, filepath:{self._filepath}, digest:{self._digest.hex()}, creationTime:{self._creationTime})'


#--------------------------------------------------------------------------------------------------
def createMetadata(filePath: str) -> 'Metadata':

  if not os.path.exists(filePath):
    raise FileNotFoundError(f'{filePath} does not exist')

  if not os.path.isfile(filePath):
    raise ValueError(f'{filePath} is not a file')

  filename = os.path.basename(filePath)
  creationTime = dt.datetime.fromtimestamp(os.path.getmtime(filePath))

  with open(filePath, 'rb') as file:
    fileContent = file.read()
    digest = hashlib.md5(fileContent).digest()

  return Metadata(filename=filename, digest=digest, creationTime=creationTime)

#--------------------------------------------------------------------------------------------------
if __name__ == "__main__":

  parser = argparse.ArgumentParser(description="Generate metadata for a file.")
  parser.add_argument("file", type=str, help="Path to the file")
  args = parser.parse_args()

  try:
    metadata = createMetadata(args.file)
    print(metadata)
  except (FileNotFoundError, ValueError, TypeError) as e:
    print(f"Error: {e}")
