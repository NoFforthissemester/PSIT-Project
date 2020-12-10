import speech_recognition as sr
import requests
import webbrowser
import random
from gtts import gTTS 
from playsound import playsound 
from datetime import datetime 


r = sr.Recognizer()

def openurl():
	webbrowser.open('www.it.kmitl.ac.th', new=2)
def openmusic():
	webbrowser.open('www.spotify.com', new=2)

def weather():
	url_w = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q=Bangkok'
	json_data_w = requests.get(url_w).json()
	check_cast = str(json_data_w["weather"][0]["id"])
	dic_th = {'200':'มีพายุฝนฟ้าคะนองและมีฝนเล็กน้อย',\
			  '201':'มีพายุฝนฟ้าคะนองและมีฝนตก',\
			  '202':'มีฝนฟ้าคะนองและมีฝนตกหนัก',\
			  '210':'มีพายุฟ้าคะนองเล็กน้อย',\
			  '211':'มีพายุฝนฟ้าคะนอง',\
			  '212':'มีพายุฝนฟ้าคะนองหนัก',\
			  '221':'มีพายุฝนฟ้าคะนอง',\
			  '230':'มีฝนฟ้าคะนองและมีฝนตกปรอยๆ',\
			  '231':'มีพายุฝนฟ้าคะนองและมีฝนตกปรอยๆ',\
			  '232':'มีพายุฝนฟ้าคะนองและมีฝนตกปรอยๆ',\
			  '300':'มีฝนเบาบาง',\
			  '301':'ฝนตกปรอยๆ',\
			  '302':'มีฝนตกปรอยๆอย่างแรง',\
			  '310':'ฟ้าว่างแต่มีมีฝนตกปรอยๆ',\
			  '311':'มีฝนปรอยๆ',\
			  '312':'มีฝนตกปรอยๆอย่างแรง',\
			  '313':'มีฝนตกปรอยๆ',\
			  '314':'มีฝนตกหนักและมีฝนตกปรอยๆ',\
			  '321':'มีฝนตกปรอยๆ',\
			  '500':'มีฝนตกปรอยๆ',\
			  '501':'มีฝนตกปานกลาง',\
			  '502':'มีฝนตกหนัก',\
			  '503':'มีฝนตกหนักมาก',\
			  '504':'มีฝนตกชุก',\
			  '511':'มีฝนเยือกแข็ง',\
			  '520':'มีฝนตกชุก',\
			  '521':'มีฝนตก',\
			  '522':'มีฝนตกหนัก',\
			  '531':'มีฝนตกพรำๆ',\
			  '701':'มีหมอกบางเบา',\
			  '711':'มีควัน',\
			  '721':'มีหมอกควัน',\
			  '731':'มีทราย / ฝุ่นหมุนวน',\
			  '741':'มีหมอกหนา',\
			  '751':'มีทราย',\
			  '761':'มีฝุ่น',\
			  '762':'มีเถ้าภูเขาไฟ',\
			  '771':'มีพายุ',\
			  '781':'มีพายุทอร์นาโด',\
			  '800':'ฟ้าโปร่ง',\
			  '801':'มีเมฆบางเบา',\
			  '802':'มีเมฆกระจาย',\
			  '803':'มีเมฆหนา',\
			  '804':'มีเมฆมืดครึ้ม'
			}
	report_weather = dic_th.get(check_cast)
	return report_weather

def temperature():
    api_address='http://api.openweathermap.org/data/2.5/weather?q=Bangkok&appid=9486b253fad80b593ccee78727b6e327&units=metric'
    json_data = requests.get(api_address).json()
    temp = json_data['main']['temp']
    return ("%.2f Celcius" % temp)

with sr.Microphone() as source: 
	playsound("./signal.mp3") 
	audio = r.record(source, duration=5) 
	playsound("./signal.mp3") 

	try:
		text = r.recognize_google(audio, language="th") 
		if "ชื่ออะไร" in text:
			text = "สวัสดีฉันชื่อซูซี่"
		if "ผม" in text:
			text = text.replace("ผม", "ฉันเองก็")
		if "ครับ" in text:
			text = text.replace("ครับ", "ค่ะ")
		if text == "กี่โมงแล้ว":
			now = datetime.now() 
			text = now.strftime("ขณะนี้เวลา%Hนาฬิกา%Mนาที%Sวินาที")
		if text == "วันนี้วันที่":
			now = datetime.now()
			text = now.strftime("%x")
		if text == "สภาพอากาศวันนี้":
			text = weather()
		if text == "อุณหภูมิตอนนี้":
			text = temperature()
		if text == "เปิดเว็บ":
			openurl()
		if text == "เปิดเพลง":
			openmusic()

	except:
		mess_list_1 = ['ขอโทษค่ะ ฉันไม่เข้าใจในสิ่งที่คุณพูด', 'ฉันไม่สามารถเข้าใจสิ่งที่คุณพูดได้ค่ะ', 'ไม่เข้าใจค่ะ']
		text = random.choice(mess_list_1)
	tts = gTTS(text, lang="th") 
	tts.save("./answer.mp3") 
	playsound("./answer.mp3")
