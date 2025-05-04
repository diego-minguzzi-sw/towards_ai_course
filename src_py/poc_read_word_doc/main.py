#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Diego Minguzzi 2025

from doc_rw import WordDocumentReader
from entities.doc import Section

import argparse
import logging as log
import os

"""
python3 ${REPO_ROOT}/src_py/poc_read_word_doc/main.py ${TAI_DATASET_ROOT}/cobot_kb/Example.docx
python3 ${REPO_ROOT}/src_py/poc_read_word_doc/main.py ${TAI_DATASET_ROOT}/cobot_kb/Example2.docx
python3 ${REPO_ROOT}/src_py/poc_read_word_doc/main.py ${TAI_DATASET_ROOT}/cobot_kb/TCS_Users_Guide_3.0C1.docx
python3 ${REPO_ROOT}/src_py/poc_read_word_doc/main.py ${TAI_DATASET_ROOT}/cobot_kb/Guidance_Programming_Language.docx
python3 ${REPO_ROOT}/src_py/poc_read_word_doc/main.py ${TAI_DATASET_ROOT}/cobot_kb/Guidance_Programming_Language_mini.docx
"""

if __name__ == "__main__":
  log.basicConfig(level=log.DEBUG, format='%(asctime)s %(levelname)s %(funcName)s:%(lineno)d: %(message)s - ')

  def sectionVisitor( section: Section):
    depth= section.depth
    indent= '..' * depth
    print(f'{indent}Section: \"{section.title}\"')
    print(f'{indent}Text:    {section.paragraphAllText()[:100]}')

  parser = argparse.ArgumentParser(description="Reads a Microsoft Word document docx file.")
  parser.add_argument("filepath", type=str, help="Path to the Word document to be read.")
  args = parser.parse_args()

  if not os.path.exists(args.filepath):
    log.error(f"File not found: {args.filepath}")
    exit(1)

  reader = WordDocumentReader()
  try:
    document = reader.readDocument(args.filepath)
    print(f"Document read successfully: {document.title}")
    print(f"Metadata:{document.metadata}")

    document.visitSectionsDepthFirst( sectionVisitor )
  except Exception as exc:
    log.error(f"An error occurred while reading the document: {exc}")
    exit(1)


