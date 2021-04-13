#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Example 4: TTS - getText2VoiceStream"""

from __future__ import print_function

import grpc
import gigagenieRPC_pb2
import gigagenieRPC_pb2_grpc
import MicrophoneStream as MS
import user_auth as UA
import os
from ctypes import *

HOST = 'gate.gigagenie.ai'
PORT = 4080

ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)
def py_error_handler(filename, line, function, err, fmt):
  dummy_var = 0
c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)
asound = cdll.LoadLibrary('libasound.so')
asound.snd_lib_error_set_handler(c_error_handler)


# TTS : getText2VoiceStream
def getText2VoiceStream(inText,inFileName):  # 음성으로 변환할 텍스트와 만들 파일의 이름을 받아서 음성파일을 생성

	channel = grpc.secure_channel('{}:{}'.format(HOST, PORT), UA.getCredentials())  # api를 사용하기위해 client 인증
	stub = gigagenieRPC_pb2_grpc.GigagenieStub(channel)

	message = gigagenieRPC_pb2.reqText()
	message.lang=0  # 한국어이므로 lang을 0으로 설정
	message.mode=0
	message.text=inText  # 변환할 텍스트이름
	writeFile=open(inFileName,'wb')  # 변환할 파일 명을 쓰기용도로(write + binary) 오픈
	for response in stub.getText2VoiceStream(message):
		if response.HasField("resOptions"):
			print ("\n\nResVoiceResult: %d" %(response.resOptions.resultCd))
		if response.HasField("audioContent"):
			print ("Audio Stream\n\n")
			writeFile.write(response.audioContent)  # 파일내에 변환한 음성을 삽입
	writeFile.close()
	return response.resOptions.resultCd

def main():
	output_file = "testtts.wav"  # 변환해서 만들 파일 명
	getText2VoiceStream("안녕하세요. 반갑습니다.", output_file)  # 음성으로 변환하고 싶은 텍스트
	MS.play_file(output_file)
	print( output_file + "이 생성되었으니 파일을 확인바랍니다. \n\n\n")
	

if __name__ == '__main__':
	main()
