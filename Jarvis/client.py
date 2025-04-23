from openai import OpenAI
import openai

client = OpenAI(
  api_key="<Your Key Here>",
)

try:
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
        {"role": "user", "content": "what is coding"}
      ]
    )

    print(completion.choices[0].message.content)

except openai.RateLimitError:
    print("⚠️ Rate limit exceeded or quota exhausted. Please check your usage at https://platform.openai.com/account/usage")

except Exception as e:
    print("❌ Error:", e)
