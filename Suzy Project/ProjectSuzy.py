import speech_recognition as sr
import requests
from gtts import gTTS 
from playsound import playsound 
from datetime import datetime 


r = sr.Recognizer()

def weather():
	url_w = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q=Bangkok'
	json_data_w = requests.get(url_w).json()
	check_cast = json_data_w['weather'][0]['id']
	dic_th = {'200':'มีพายุฝนฟ้าคะนองและมีฝนเล็กน้อย',\
			  '201':'มีพายุฝนฟ้าคะนองและมีฝนตก',\
			  '202':'มีฝนฟ้าคะนองและมีฝนตกหนัก',\
			  '210':'พายุฟ้าคะนองเล็กน้อย',\
			  '211':'พายุฝนฟ้าคะนอง',\
			  '212':'พายุฝนฟ้าคะนองหนัก',\
			  '221':'พายุฝนฟ้าคะนอง',\
			  '230':'มีฝนฟ้าคะนองและมีฝนตกปรอยๆ',\
			  '231':'มีพายุฝนฟ้าคะนองและมีฝนตกปรอยๆ',\
			  '232':'มีพายุฝนฟ้าคะนองและมีฝนตกปรอยๆ',\
			  '300':'ฝนเบาบาง',\
			  '301':'ฝนตกปรอยๆ',\
			  '302':'มีฝนตกปรอยๆอย่างแรง',\
			  '310':'ฟ้าว่างแต่มีมีฝนตกปรอยๆ',\
			  '311':'ฝนปรอยๆ',\
			  '312':'มีฝนตกปรอยๆอย่างแรง',\
			  '313':'ฝนตกปรอยๆ',\
			  '314':'ฝนตกหนักและมีฝนตกปรอยๆ',\
			  '321':'ฝนตกปรอยๆ',\
			  '500':'มีฝนตกปรอยๆ',\
			  '501':'มีฝนตกปานกลาง',\
			  '502':'มีฝนตกหนัก',\
			  '503':'ฝนตกหนักมาก',\
			  '504':'ฝนตกชุก',\
			  '511':'ฝนเยือกแข็ง',\
			  '520':'ฝนตกชุก',\
			  '521':'ฝนตก',\
			  '522':'ฝนตกหนัก',\
			  '531':'ฝนตกพรำๆ',\
			  '701':'หมอกบางเบา',\
			  '711':'ควัน',\
			  '721':'หมอกควัน',\
			  '731':'ทราย / ฝุ่นหมุนวน',\
			  '741':'หมอกหนา',\
			  '751':'ทราย',\
			  '761':'ฝุ่น',\
			  '762':'เถ้าภูเขาไฟ',\
			  '771':'พายุ',\
			  '781':'พายุทอร์นาโด',\
			  '800':'ฟ้าโปร่ง',\
			  '801':'เมฆน้อย',\
			  '802':'เมฆกระจาย',\
			  '803':'เมฆหนา',\
			  '804':'เมฆมืดครึ้ม'
			}
	report_weather = dic_th[check_cast]
	return report_weather

def temp():
	url_t = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q=Bangkok&units=metric'
	json_data_t = requests.get(url_t).json()
	format_add_t = json_data_t['main']["temp"]
	return format_add_t

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
		if text == "อากาศเป็นไงบ้าง":
			text = weather()
		if text == "อุณหภูมิวันนี้":
			text = temp()

	except:
		text = "ขอโทษค่ะ ฉันไม่เข้าใจในสิ่งที่คุณพูด"
	tts = gTTS(text, lang="th") 
	tts.save("./answer.mp3") 
	playsound("./answer.mp3")
