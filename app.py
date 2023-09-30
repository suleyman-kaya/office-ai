from flask import Flask, request
from AI import roles
from secret_keys import openai_keys
from termcolor import colored
from electronics.lamp import role_ac, role_kapa, relay_1, relay_2, relay_3, relay_4
import openai

openai.api_key = openai_keys.current_api_key

messages = [ {"role": "system", "content": roles.mergen} ]

def reply_the_prompt(prompt):
	message = prompt["prompt"]
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
	return reply

def komut_kontrol(komut):
	try:
		komut_no = komut.split("|")
		komut_no = int(komut_no[1])
		if(komut_no == 1):
			role_ac(relay_1)
		elif(komut_no == 2):
			role_ac(relay_2)
		elif(komut_no == 3):
			role_ac(relay_3)
		elif(komut_no == 4):
			role_ac(relay_4)
		elif(komut_no == 5):
			role_kapa(relay_1)
		elif(komut_no == 6):
			role_kapa(relay_2)
		elif(komut_no == 7):
			role_kapa(relay_3)
		elif(komut_no == 8):
			role_kapa(relay_4)
		else:
			print("OK.")
	except:
		print("OK.")
app = Flask(__name__)

@app.route('/post', methods=['POST'])
def post():
	data = request.get_json()
	ai_res = reply_the_prompt(data)
	komut_kontrol(ai_res)
	response = {"response" : ai_res}
	return response
app.run()

