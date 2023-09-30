from AI import roles
from secret_keys import openai_keys
from termcolor import colored
import openai

openai.api_key = openai_keys.current_api_key

messages = [ {"role": "system", "content": roles.mergen} ]

while True:
	message = input(colored("Siz >", "cyan", "on_white") + " ")
	if message:
		messages.append(
			{"role": "user", "content": message},
		)
		chat = openai.ChatCompletion.create(
			model="gpt-3.5-turbo", messages=messages
		)
	reply = chat.choices[0].message.content
	print(colored("MERGEN", "white", "on_green"), f"{reply}")
	messages.append({"role": "assistant", "content": reply})
