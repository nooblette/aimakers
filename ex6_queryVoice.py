#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Example 6: STT + Dialog - queryByVoice"""

from __future__ import print_function

import grpc
import time
import gigagenieRPC_pb2
import gigagenieRPC_pb2_grpc
import MicrophoneStream as MS
import user_auth as UA
import os
### STT

import audioop
from ctypes import *

RATE = 16000
CHUNK = 512

HOST = 'gate.gigagenie.ai'
PORT = 4080

ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)
def py_error_handler(filename, line, function, err, fmt):
  dummy_var = 0
c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)
asound = cdll.LoadLibrary('libasound.so')
asound.snd_lib_error_set_handler(c_error_handler)

def generate_request():  # 마이크에서 가져온 데이터를 기가지니 STT API에 입력할수있도록 변환하는 함수
	with MS.MicrophoneStream(RATE, CHUNK) as stream:
		audio_generator = stream.generator()
		messageReq = gigagenieRPC_pb2.reqQueryVoice()
		messageReq.reqOptions.lang=0  # 질문할 음성이 한국어이므로 0으로 설정
		messageReq.reqOptions.userSession="1234"  # 질의의 문맥을 유지할때 필요한 값으로 문맥에 따라 다르게 설정(코드로 보면 이해가 잘 안돼서 실제로 실행시켜봐야 알 것 같음)
		messageReq.reqOptions.deviceId="aklsjdnalksd"  # 해당 AI스피커의 정보, 디바이스에 따라 다르게 설정(보통 MAC주소로 설정)
		yield messageReq
		for content in audio_generator:
			message = gigagenieRPC_pb2.reqQueryVoice()
			message.audioContent = content
			yield message
			rms = audioop.rms(content,2)

def queryByVoice():  # 음성으로 질문하고 텍스트로 대답 받기
	print ("\n\n\n질의할 내용을 말씀해 보세요.\n\n듣고 있는 중......\n")
	channel = grpc.secure_channel('{}:{}'.format(HOST, PORT), UA.getCredentials())
	stub = gigagenieRPC_pb2_grpc.GigagenieStub(channel)
	request = generate_request()  # 음성으로 입력한 질의어를 기가지니 STT API에 입력할 수 있도록 변환
	resultText = ''
	response = stub.queryByVoice(request)  
	# API에 입력할수 있도록 변환한 음성 질의어를 queryByVoice함수에 입력, 대답을 텍스트로 리턴받음
	# 음성으로 입력한 질의어로 query API에 질문을 입력
	
	if response.resultCd == 200:
		print("질의 내용: %s" % (response.uword))  # 질의내용을 출력하고
		for a in response.action:
			response = a.mesg
			parsing_resp = response.replace('<![CDATA[', '')  # 출력할때 필요없는 부분을 제거
			parsing_resp = parsing_resp.replace(']]>', '')  # 위와 마찬가지
			resultText = parsing_resp  # 답변받은 내용을 전달 받고
			print("\n질의에 대한 답변: " + parsing_resp +'\n\n\n')  # 답변을 출력

	else:
		print("\n\nresultCd: %d\n" % (response.resultCd))
		print("정상적인 음성인식이 되지 않았습니다.")
	return resultText

def main():
	queryByVoice()
	time.sleep(0.5)  # 0.5초간 프로세스 중지

if __name__ == '__main__':
	main()
