#
# Example of how to send a prompt to OpenAI using plain Json.
#
import logging as log
import os
import pprint
import requests

url = "https://api.openai.com/v1/chat/completions"

#--------------------------------------------------------------------------------------------------
def sendPrompt( userPrompt: str, maxTokens=60, temperature=0.7):
  log.debug('sendPrompt started.')
  OPEN_AI_KEY_NAME='OPENAI_API_KEY'
  if not OPEN_AI_KEY_NAME in os.environ:
    log.error(f'Environment variable {OPEN_AI_KEY_NAME} not set.')
    return
  openaiKey=os.environ[OPEN_AI_KEY_NAME]

  headers = {
      "Authorization": f"Bearer {openaiKey}",
      "Content-Type": "application/json",
  }

  # The data payload with your prompt and other parameters
  data = {
      "model": "gpt-4o-mini",
      "messages": [
          {
              "role": "system",
              "content": "You are a helpful assistant that translate from English to French"
          },
          {
              "role": "user",
              "content": userPrompt
          }
      ],
      "max_tokens": int(maxTokens),
      "temperature": float(temperature),
  }

  response = requests.post(url, json=data, headers=headers)

  result=None
  if response.status_code == 200:
    log.debug(f'response:\n'+ pprint.pformat(response.json(), width=100))

    choices= response.json()['choices']
    if len(choices)<=0:
      log.error('The response has no content')
    else:
      result= choices[0]['message']['content']
      log.debug(f'result:{result}')
  else:
    print(f"Failed to fetch data: {response.status_code}, {response.text}")

  log.debug('sendPrompt terminated.\n')
  return result

#--------------------------------------------------------------------------------------------------
def main():
  log.debug('main started.')
  sendPrompt("Bye, see you later.")
  log.debug('main terminated.\n')

#--------------------------------------------------------------------------------------------------
if __name__ == "__main__":
  log.basicConfig(level=log.DEBUG, format='%(asctime)s [%(levelname)5s] - %(message)s',
                  datefmt='%H:%M:%S')
  log.debug('Debug message.')
  log.info('Info message.')
  main()
