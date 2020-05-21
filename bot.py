import requests
import time
import math
from bs4 import BeautifulSoup

TOKEN = "546951764:AAHrXPtQpeYQBQLs3VX9NHau_j3Sz28q4Qw"
URL = f"https://telegg.ru/orig/bot{TOKEN}"

def getResponse(suburl):
	return requests.get(URL + f"/{suburl}").json()

def sendMethod(method, params):
	return getResponse(f"/{method}?{params}")['result']

def lastMessage():
	mess = sendMethod("getUpdates", "")
	mes = mess[-1]
	#for mes in mess:
	if('message' in mes):
		return (f"{mes['message']['from']['id']}, {mes['message']['from']['first_name']}, {mes['message']['text']}, {time.ctime(mes['message']['date'])}")
	else:
		return (f"{mes['edited_message']['from']['id']}, {mes['edited_message']['from']['first_name']}, {mes['edited_message']['text']}, {time.ctime(mes['edited_message']['date'])} '<edited>'")

def main():
	while True:
		commands = input().split(" ")
		if(commands[0] == "exit"): 
			print("Exiting...")
			break
		sendMethod(commands[0], commands[1] if (len(commands) > 1) else "")

def sendMessage(id, text):
	sendMethod("sendMessage", "chat_id={id}&text{text}")

#lastMessage()

def mainx():
	last = lastMessage()
	while True:
		mes = lastMessage()
		if(last != mes): 
			last = mes
			print(mes)
#headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive'}
#r = requests.post("https://charts.forexpf.ru/html/htmlquotes/q", data=)
#rx = requests.get(f"https://charts.forexpf.ru/html/htmlquotes/q?msg=1;SID={r};T={math.floor(time.time()*1000)}").text
#bs = BeautifulSoup(r).text#.find('td', attrs = {'id':"b_29"}).text
#print(r)

#import sseclient
'''

url = f"https://charts.forexpf.ru/html/htmlquotes/qsse?msg=1;SID={sid};T={math.floor(time.time()*1000)}"
print(url)'''
#r = requests.get(f"https://charts.forexpf.ru/html/htmlquotes/qsse?msg=1;SID={sid};T={math.floor(time.time()*1000)}", stream=True)
'''print(r.status_code)
mess = sseclient.SSEClient(r).events()
print(len(list(mess)))
for i in mess:
	print(i)'''
sid = requests.get("https://charts.forexpf.ru/html/htmlquotes/q")

r = requests.Request("POST", "https://charts.forexpf.ru/html/htmlquotes/q", params=f"1;SID={sid.text};B=;A=;NCH=;NCHP=;S=29;S=30")
print(r.prepare())#r = requests.post("https://charts.forexpf.ru/html/htmlquotes/q", params=f"1;SID={sid.text};B=;A=;NCH=;NCHP=;S=29;S=30")