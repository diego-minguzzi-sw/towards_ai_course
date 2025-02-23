# --------------------------------------------------------------------------------------------------
# Diego Minguzzi 2025
# Adapted from the Llama Index Starter tutorial:
#   https://docs.llamaindex.ai/en/stable/getting_started/starter_example/
# --------------------------------------------------------------------------------------------------
import asyncio
from llama_index.core import StorageContext, load_index_from_storage, set_global_handler
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.agent.workflow import AgentWorkflow
from llama_index.core.agent import ReActAgent
from llama_index.llms.gemini import Gemini
from llama_index.llms.openai import OpenAI
from llama_index.core.tools import FunctionTool
from llama_index.core.workflow import Context

import logging as log
import os

log.basicConfig(level=log.INFO, format='%(asctime)s [%(levelname)5s] - %(message)s',
                  datefmt='%H:%M:%S')

indexPersistDirStorage='storage'

def multiply(a: float, b: float) -> float:
    """Multiply two numbers and returns the product"""
    return a * b

multiply_tool = FunctionTool.from_defaults(fn=multiply)


def add(a: float, b: float) -> float:
    """Add two numbers and returns the sum"""
    return a + b

add_tool = FunctionTool.from_defaults(fn=add)


# llm=Gemini(model="models/gemini-1.5-flash")
llm=OpenAI(model="gpt-4o-mini")

# Create an agent workflow with our calculator tool
agent = ReActAgent.from_tools([multiply_tool, add_tool], llm=llm, verbose=True)

async def main():
    log.info('main started.')
    set_global_handler("simple")
    response = agent.chat("What is 20+(2*4)? Use a tool to calculate every step.")
    log.info(f'response:\n\t{response}')

    log.info('main terminated.')

# Run the agent
if __name__ == "__main__":

    os.environ["GRPC_VERBOSITY"] = "FATAL"
    os.environ["GLOG_minloglevel"] = "3"
    asyncio.run(main())
