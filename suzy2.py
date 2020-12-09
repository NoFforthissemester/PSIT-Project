import speech_recognition as sr  #ใช้สำหรับแปลงเสียงพูดเป็นข้อความ
from gtts import gTTS #ใช้สำหรับแปลงข้อความเป็นเสียงพูด
from playsound import playsound #ใช้สำหรับเล่นไฟล์เสียง
from datetime import datetime #ใช้สำหรับดูเวลาขณะนี้


r = sr.Recognizer() #เริ่มต้นInitiate
with sr.Microphone() as source: 
	audio = r.record(source, duration=5) #บันทึกเสียง 5 วินาที
	text=""
	try:
		text = r.recognize_google(audio, language="th") #ส่งไปให้google cloud		
		if "คุณชื่ออะไร" in text:
			text = text.replace("คุณชื่ออะไร", "ฉันชื่อsuzy")
		if "ผม" in text:
			text = text.replace("ผม", "ฉันเองก็")
		if "ครับ" in text:
			text = text.replace("ครับ", "ค่ะ")
		if "มุก" in text:
			text = "ลาเร็วกว่าม้าเพราะลาไปก่อน555"
		if "กี่โมงแล้ว" in text:
			now = datetime.now() #รับค่าเวลาขณะนั้น
			text = now.strftime("%H:%M:%S")
		if "วันที่" in text:
			now = datetime.now()
			text = now.strftime("%x")
	except:
		text = "ขอโทษค่ะ"
	tts = gTTS(text, lang="th") #ส่งไปให้google cloud
	tts.save("./answer.mp3") #บันทึกเสียงที่ได้จากgoogle cloud
	playsound("./answer.mp3")
