from llama_index.core import Settings
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI
from llama_index.vector_stores.qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from typing import Any, List, Optional, Sequence, Union

import asyncio
import google.genai.errors
import json
import logging as log
import os
import pprint
import qdrant_client
import time


from llama_index.core.llms.function_calling import FunctionCallingLLM
from llama_index.core.base.llms.types import ChatMessage
from llama_index.core.constants import DEFAULT_TEMPERATURE, DEFAULT_NUM_OUTPUTS

class GoogleGenAI(FunctionCallingLLM):
    def __init__(self,
                 model_name: str,
                 temperature: float = DEFAULT_TEMPERATURE,
                 max_tokens: Optional[int] = None,):
        # Initialize the base class and the GoogleGenAI client
        super().__init__(model= model_name, temperature=temperature, max_tokens=max_tokens)
        self._llm = GoogleGenAI(model=model_name)
        self._num_achat_requests = 0

    @property
    def metadata(self): return self._llm.metadata

    def complete( self, prompt: str, formatted: bool = False, **kwargs: Any):
        log.info('complete executed.')
        try:
            return self._llm.complete( prompt, formatted, **kwargs)
        except Exception as exc:
            log.error(f'complete: exception:{type(my_llm).__name__}: {exc.message}')
            raise

    async def acomplete(self, prompt: str, formatted: bool = False, **kwargs: Any):
        log.info('acomplete executed.')
        result = await self._llm.acomplete( prompt, formatted, **kwargs)
        return result

    def stream_complete( self, prompt: str, formatted: bool = False, **kwargs: Any):
        log.info('stream_complete executed.')
        return self._llm.stream_complete( prompt, formatted, **kwargs)

    async def astream_complete( self, prompt: str, formatted: bool = False, **kwargs: Any):
        log.info('astream_complete executed.')
        result = await self._llm.astream_complete( prompt, formatted, **kwargs)
        return result

    def chat(self, messages: Sequence[ChatMessage], **kwargs: Any):
        log.info('chat executed.')
        return self._llm.chat( messages, **kwargs)

    async def achat(self, messages: Sequence[ChatMessage], **kwargs: Any):

        try:
            result = await self._llm.achat( messages, **kwargs)
            self._num_achat_requests += 1
            return result
        except google.genai.errors.ClientError as exc:
            log.error(f'achat: ClientError:{type(exc).__name__}: {exc.message}')
            if (exc.code==429):
                log.error(f'achat: RESOURCE EXAUSTED....................................................... num reqs:{self._num_achat_requests}')
            else:
                log.error('achat: NOT RESOURCE EXAUSTED...................................................')
                raise
        except Exception as exc:
            log.error(f'achat: exception:{type(exc).__name__}: {exc.message}')
            raise

        await asyncio.sleep( 60)
        self._num_achat_requests = 0
        log.error('Second attempt...........................................................................')
        try:
            result = await self._llm.achat( messages, **kwargs)
            self._num_achat_requests += 1
            log.error('Second attempt executed ..................................................................')
            return result
        except Exception as exc:
            log.error(f'achat: exception:{type(exc).__name__}: {exc.message}')
            raise

    def stream_chat(self, messages: Sequence[ChatMessage], **kwargs: Any):
        log.info('stream_chat executed.')
        return self._llm.stream_chat( messages, **kwargs)

    async def astream_chat(self, messages: Sequence[ChatMessage], **kwargs: Any):
        log.info('astream_chat executed.')
        response= await self._llm.astream_chat( messages, **kwargs)
        return response

    def _prepare_chat_with_tools(
        self,
        tools: Sequence["BaseTool"],
        user_msg: Optional[Union[str, ChatMessage]] = None,
        chat_history: Optional[List[ChatMessage]] = None,
        verbose: bool = False,
        allow_parallel_tool_calls: bool = False,
        tool_choice: Union[str, dict] = "auto",
        strict: Optional[bool] = None,
        **kwargs: Any):
        return self._llm._prepare_chat_with_tools(tools,
                                                  user_msg,
                                                  chat_history,
                                                  verbose,
                                                  allow_parallel_tools_calls,
                                                  tool_choice,
                                                  strict,
                                                  **kwargs)
