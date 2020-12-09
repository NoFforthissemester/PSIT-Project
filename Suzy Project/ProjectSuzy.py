import speech_recognition as sr
import requests
from gtts import gTTS 
from playsound import playsound 
from datetime import datetime 


r = sr.Recognizer()

def weather():
	url_w = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q=Bangkok'
	json_data_w = requests.get(url_w).json()
	format_add_w = json_data_w['weather'][0]["main"]
	if format_add_w == 'Clouds':
		format_add_w = 'มีเมฆมาก'
	return format_add_w

def temp():
	url_t = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q=Bangkok&units=metric'
	json_data_t = requests.get(url_t).json()
	format_add_t = json_data_t['main'][0]["temp"]
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
		if text == "อากาศเป็นไงบ้าง":
			text = weather()
		if text == "อุณหภูมิวันนี้":
			text = temp()

	except:
		text = "ขอโทษค่ะ ฉันไม่เข้าใจในสิ่งที่คุณพูด"
	tts = gTTS(text, lang="th") 
	tts.save("./answer.mp3") 
	playsound("./answer.mp3")
