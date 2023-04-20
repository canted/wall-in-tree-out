from prompt import get_chat_prompt
import os
import openai

openai_api_key = os.environ['OPENAI_API_KEY']

def complete(message):
  # full_prompt = get_chat_prompt(message)

  print("querying openai...")

  try:
      response = openai.ChatCompletion.create(
          model="gpt-3.5-turbo", # text-davinci-003 # gpt-3.5-turbo
          messages=get_chat_prompt(message), # get_legacy_prompt(message)
          stream=True 
      )

      # html = markdown2.markdown(response['choices'][0]['message']['content'])

  except openai.error.APIError as e:
    # Check if the error is related to rate limits or usage limits
    if e.status_code == 429:
        response = "Sorry, the usage limit has been reached. Please try again later."
    else:
        response = "An error occurred while processing your request. Please try again later."

  return response
