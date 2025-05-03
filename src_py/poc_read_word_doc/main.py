#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Diego Minguzzi 2025
from doc_rw import WordDocumentReader

import argparse
import logging as log
import os

"""
python3 ${REPO_ROOT}/src_py/poc_read_word_doc/main.py ${TAI_DATASET_ROOT}/cobot_kb/Example.doc
"""

if __name__ == "__main__":
  log.basicConfig( level=log.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

  parser = argparse.ArgumentParser(description="Read and process a Word document.")
  parser.add_argument("filepath", type=str, help="Path to the Word document to be read.")
  args = parser.parse_args()

  if not os.path.exists(args.filepath):
    log.error(f"File not found: {args.filepath}")
    exit(1)

  reader = WordDocumentReader()
  try:
    document = reader.readDocument(args.filepath)
    log.info(f"Document read successfully: {document.title}")
  except Exception as e:
    log.error(f"An error occurred while reading the document: {e}")
    exit(1)


