import requests
import time
import math
import json
from bs4 import BeautifulSoup

TOKEN = "546951764:AAHrXPtQpeYQBQLs3VX9NHau_j3Sz28q4Qw"
URL = f"https://telegg.ru/orig/bot{TOKEN}"

messages = [{'update_id': 0}]

users = {}

keyboard = {
	'keyboard': [[{'text': 'Back'}, {'text': 'Next'}]],
	'resize_keyboard': True
}

hide_keyboard = {
	'hide_keyboard': True
}

def getPageText(page):
	text = requests.get(f"https://knijky.ru/books/ya-poslannik?page={page}").text
	print(text)
	bs = BeautifulSoup(text)
	return bs.find("table").text

def showKeyboard(user):
	user['params']['keyboard'] = True
	sendMethod("sendMessage", f"chat_id={user['id']}&text=Keyboard showed!&reply_markup={json.dumps(keyboard)}")

def hideKeyboard(user):
	user['params']['keyboard'] = False
	sendMethod("sendMessage", f"chat_id={user['id']}&text=Keyboard hided!&reply_markup={json.dumps(hide_keyboard)}")

def sendPage(id, page):
	sendMessage(id, f"Page: {page}")
	sendMessage(id, getPageText(text))

def nxt(user):
	user['params']['page'] += 1
	sendPage(user['id'], user['params']['page'])

def back(user):
	if(user['params']['page'] > 1): user['params']['page'] -= 1
	sendPage(user['id'], user['params']['page'])

def setPage(arg, user):
	user['params']['page'] = int(arg)
	sendPage(user['id'], user['params']['page'])


commands = {
	'next': nxt,
	'back': back,
	'/show': showKeyboard,
	'/hide': hideKeyboard,
	'/page': setPage
}

def getResponse(suburl):
	return requests.get(URL + f"/{suburl}").json()

def sendMethod(method, params):
	return getResponse(f"/{method}?{params}")['result']

def sendMessage(chat_id, text, params = ""):
	requests.post(f"{URL}/sendMessage", data={'chat_id': chat_id, 'text': text})

def getUpdates():
	messages = [{'update_id': 0}]
	while True:
		messages = sendMethod("getUpdates", f"offset={messages[-1]['update_id'] + 1 if(len(messages) > 0) else 1000}")
		parse(messages)
		handleLastMessages()

def handleLastMessages():
	for user in users:
		updates = users[user]['updates']
		last_id = list(updates.keys())[-1]
		last_message = updates[last_id]

		if(not last_message['handled']):
			print(users[user]['updates'][last_id], user)
			if(last_message['text'].lower().split(' ')[0] in commands):
				if(len(last_message['text'].lower().split(' ')) > 1):
					commands[last_message['text'].lower().split(' ')[0]](last_message['text'].lower().split(' ')[1], users[user])
				else:
					commands[last_message['text'].lower()](users[user])

				users[user]['updates'][last_id]['handled'] = True

def parse(messages):
	for mes in messages:
		if('message' in mes):
			user_id = mes['message']['from']['id']
			text = mes['message']['text']
			update_id = mes['update_id']

			if(not user_id in users): users[user_id] = {'id': user_id, 'updates': {}, 'params': {'page': 1, 'keyboard': False}}
			if(not update_id in users[user_id]['updates']): users[user_id]['updates'][update_id] = {'id': update_id, 'text': text, 'handled': False}

getUpdates()