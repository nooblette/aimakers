#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Example 1: GiGA Genie Keyword Spotting"""

from __future__ import print_function

import audioop
from ctypes import *
import RPi.GPIO as GPIO
import ktkws # KWS
import MicrophoneStream as MS
KWSID = ['기가지니', '지니야', '친구야', '자기야']
RATE = 16000
CHUNK = 512

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(31, GPIO.OUT)
btn_status = False

def callback(channel):  
	print("falling edge detected from pin {}".format(channel))
	global btn_status
	btn_status = True
	print(btn_status)

GPIO.add_event_detect(29, GPIO.FALLING, callback=callback, bouncetime=10)
# line 17~29 : GPIO 설정 부분, 버튼의 LED초기 설정과 버튼이 눌러졌을때 동작 처리

ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)
def py_error_handler(filename, line, function, err, fmt):
  dummy_var = 0
c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)
asound = cdll.LoadLibrary('libasound.so')
asound.snd_lib_error_set_handler(c_error_handler)


def detect():  # 마이크에서 들어오는 데이터를 호출어 인식하는 모듈을 사용하여 동작
	with MS.MicrophoneStream(RATE, CHUNK) as stream:  # MicroStream클래스를 통해 rate와 chunk처리, stream이라는 객체 생성
		audio_generator = stream.generator()  # stream은 iterator Object(값을 차례대로 꺼낼 수 있음)

		for content in audio_generator:  # iterator로 반복
			rc = ktkws.detect(content)  # ktkws 모듈을 봐야 알 것 같은데 아마 내용을 인식하면 ktkws의 detect 함수가 1을 리턴
			rms = audioop.rms(content,2)
			#print('audio rms = %d' % (rms))

			if (rc == 1):  # 호출어가 인식되면
				MS.play_file("../data/sample_sound.wav")  # '띠리링'소리를 출력
				return 200

def btn_detect():  # 버튼이 눌리는 것을 처리
	global btn_status
	with MS.MicrophoneStream(RATE, CHUNK) as stream:  # MicroStream클래스를 통해 rate와 chunk처리, stream이라는 객체 생성
		audio_generator = stream.generator()  # stream은 iterator Object(값을 차례대로 꺼낼 수 있음)

		for content in audio_generator:
			GPIO.output(31, GPIO.HIGH)  # GPIO(버튼설정)
			rc = ktkws.detect(content)
			rms = audioop.rms(content,2)
			#print('audio rms = %d' % (rms))
			GPIO.output(31, GPIO.LOW)
			if (btn_status == True):  # 버튼이 눌러진것이 확인되면
				rc = 1  # rc를 1로
				btn_status = False			
			if (rc == 1):  # rc값이 1이면 버튼이 눌러진것이므로
				GPIO.output(31, GPIO.HIGH)
				MS.play_file("../data/sample_sound.wav")  # '띠리링'소리를 출력
				return 200

def test(key_word = '기가지니'):  # 마이크로 호출어를 인식하는 함수, 기가지니, 지니야, 친구야의 호출어를 지정 할 수 있음
	rc = ktkws.init("../data/kwsmodel.pack")
	print ('init rc = %d' % (rc))  # 진행사항을 출력
	rc = ktkws.start()
	print ('start rc = %d' % (rc))
	print ('\n호출어를 불러보세요~\n')
	ktkws.set_keyword(KWSID.index(key_word))
	rc = detect()  # 호출어가 제대로 인식되었으면 200을 
	print ('detect rc = %d' % (rc))
	print ('\n\n호출어가 정상적으로 인식되었습니다.\n\n')
	ktkws.stop()
	return rc

def btn_test(key_word = '기가지니'):  # 버튼을 인식해서 진행
	global btn_status
	rc = ktkws.init("../data/kwsmodel.pack")
	print ('init rc = %d' % (rc))
	rc = ktkws.start()
	print ('start rc = %d' % (rc))
	print ('\n버튼을 눌러보세요~\n')
	ktkws.set_keyword(KWSID.index(key_word))
	rc = btn_detect()
	print ('detect rc = %d' % (rc))
	print ('\n\n호출어가 정상적으로 인식되었습니다.\n\n')
	ktkws.stop()
	return rc

def main():
	test()  # 음성호출
	#btn_test()  # 버튼호출

if __name__ == '__main__':
	main()
