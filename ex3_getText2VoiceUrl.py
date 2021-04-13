#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Example 3: TTS - getText2VoiceUrl"""

from __future__ import print_function

import grpc
import gigagenieRPC_pb2
import gigagenieRPC_pb2_grpc
import user_auth as UA
import os

HOST = 'gate.gigagenie.ai'
PORT = 4080


# TTS : getText2VoiceUrl
def getText2VoiceUrl(inText):  #inText를 출력할 수 있는 url를 출력(출력하는 url은 1분간 유효함)

	channel = grpc.secure_channel('{}:{}'.format(HOST, PORT), UA.getCredentials())
	stub = gigagenieRPC_pb2_grpc.GigagenieStub(channel)

	message = gigagenieRPC_pb2.reqText()
	message.lang=0  # 한국어명 lang = 0 
	message.mode=0
	message.text=inText  # 변환할 텍스트 입력
	response = stub.getText2VoiceUrl(message)  # url로 변환
	# line 24~28 : 사용할 언어를 설정, 텍스트를 입력해 변환

	print ("\n\nresultCd: %d" % (response.resultCd))
	if response.resultCd == 200:
		print ("TTS 생성에 성공하였습니다.\n\n\n아래 URL을 웹브라우져에 넣어보세요.")
		print ("Stream Url: %s\n\n" % (response.url))
	else:
		print ("TTS 생성에 실패하였습니다.")
		print ("Fail: %d" % (response.resultCd)) 

def main():
	# Text to SPeech(TTS) : 지정된 텍스트를 음성으로 바꾸어 음성을 들을 수 있는 url을 제공
	getText2VoiceUrl("안녕하세요. 반갑습니다.")  # 변경하고싶은 단어나 문장을 매개변수로 설정

if __name__ == '__main__':
	main()
