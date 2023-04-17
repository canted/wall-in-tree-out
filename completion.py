from prompt import get_full_prompt
import os
import openai
import markdown2

openai_api_key = os.environ['OPENAI_API_KEY']

def complete(message):
  full_prompt = get_full_prompt(message)

  print("querying openai...")

  try:
      response = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=full_prompt
      )

      html = markdown2.markdown(response['choices'][0]['message']['content'])

  except openai.error.APIError as e:
    # Check if the error is related to rate limits or usage limits
    if e.status_code == 429:
        html = "Sorry, the usage limit has been reached. Please try again later."
    else:
        html = "An error occurred while processing your request. Please try again later."

  return html
