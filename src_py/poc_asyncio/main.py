#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Diego Minguzzi 2025

#
# https://qdrant.github.io/fastembed/Getting%20Started/#quick-start

import asyncio
import logging as log
import os

#--------------------------------------------------------------------------------------------------
async def add( x: int, y: int) -> int:
  await asyncio.sleep(1)
  return x + y

#--------------------------------------------------------------------------------------------------
async def sleepForCycles( numCycles: int) -> int:
  log.info('Started')
  for i in range(numCycles):
    log.info(f'Sleeping for cycle {i + 1} of {numCycles}')
    await asyncio.sleep(1)
  log.info('Terminated')
  return numCycles

#--------------------------------------------------------------------------------------------------
async def testSleepForCycles():
  log.info('Started')
  numCycles= 3
  futureResult = asyncio.create_task( sleepForCycles(numCycles))
  await asyncio.sleep(1)

  try:
    futureResult.cancel()
    result = await futureResult
    log.info(f'Slept for {result} cycles')
  except asyncio.exceptions.CancelledError as exc:
    log.error(f'Exception: {type(exc)}')

  log.info('Terminated')

#--------------------------------------------------------------------------------------------------
async def testAsynch():
  log.info('Started')
  resultObj = asyncio.create_task( add( 3, 5))
  resultObj2 = asyncio.create_task( add( 5, 7))
  log.info('waiting...')

  result= await resultObj
  log.info(f'result: {result}')

  result2= await resultObj2
  log.info(f'result2: {result2}')

  log.info('Terminated')

#--------------------------------------------------------------------------------------------------
if __name__ == "__main__":
  log.basicConfig(level=log.INFO, format='%(asctime)s %(levelname)s %(funcName)s:%(lineno)d: %(message)s')
  log.info('Started')
  result = asyncio.run( add(1, 2))
  log.info(f'result: {result}')

  asyncio.run( testAsynch())

  asyncio.run( testSleepForCycles())

  log.info('Terminated')
