# --------------------------------------------------------------------------------------------------
# Diego Minguzzi 2025
# Adapted from the Llama Index Starter tutorial:
#   https://docs.llamaindex.ai/en/stable/getting_started/starter_example/
# --------------------------------------------------------------------------------------------------
import asyncio
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.agent.workflow import AgentWorkflow
from llama_index.core.workflow import Context
from llama_index.llms.gemini import Gemini
from llama_index.llms.openai import OpenAI
from llama_index.core import StorageContext, load_index_from_storage
import logging as log
import os

log.basicConfig(level=log.INFO, format='%(asctime)s [%(levelname)5s] - %(message)s',
                  datefmt='%H:%M:%S')

indexPersistDirStorage='storage'

if os.path.exists(indexPersistDirStorage):
  log.info(f'Loading index from {indexPersistDirStorage}')
  storage_context = StorageContext.from_defaults(persist_dir= indexPersistDirStorage)
  index = load_index_from_storage(storage_context)
else:
  log.info(f'Creating index, storing to {indexPersistDirStorage}')
  documents = SimpleDirectoryReader("data").load_data()
  index = VectorStoreIndex.from_documents(documents)
  query_engine = index.as_query_engine()
  index.storage_context.persist( indexPersistDirStorage)


# Define a simple calculator tool
def multiply(a: float, b: float) -> float:
    """Useful for multiplying two numbers."""
    return a * b

def add(a: float, b: float) -> float:
    """Useful for adding two numbers."""
    return a + b

async def search_documents(query: str) -> str:
    """Useful for answering natural language questions about an personal essay written by Paul Graham."""
    response = await query_engine.aquery(query)
    return str(response)

# llm=Gemini(model="models/gemini-1.5-flash")
llm=OpenAI(model="gpt-4o-mini")

# Create an agent workflow with our calculator tool
agent = AgentWorkflow.from_tools_or_functions(
    [ add,
      multiply,
      search_documents],
    llm=llm,
    system_prompt="""You are a helpful assistant that can:
    . multiply two numbers,
    . add two numbers
    . search through documents to answer questions""",
)

async def main():
    log.info('main started.')
    # Run the agent


    # Context remembers the conversation.
    ctx = Context(agent)

    """
    response = await agent.run("What is 1234 * 4567?",ctx)
    print(str(response))

    response = await agent.run("My name is Logan", ctx=ctx)
    print(str(response))

    response = await agent.run("What is my name?", ctx=ctx)
    print(str(response))
    """

    response = await agent.run("What art school did Paul Graham attend? Respond precisely taking into account all his story.", ctx=ctx)
    print(str(response))

    log.info('main terminated.')

# Run the agent
if __name__ == "__main__":


    # https://stackoverflow.com/questions/78780089/how-do-i-get-rid-of-the-annoying-terminal-warning-when-using-gemini-api
    os.environ["GRPC_VERBOSITY"] = "FATAL"
    os.environ["GLOG_minloglevel"] = "3"
    asyncio.run(main())
