#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Example 5: Dialog - queryByText"""

from __future__ import print_function

import grpc
import user_auth as UA
import gigagenieRPC_pb2
import gigagenieRPC_pb2_grpc
import os

HOST = 'gate.gigagenie.ai'
PORT = 4080

# DIALOG : queryByText
def queryByText(text):  # 질문한 텍스트 대한 대답을 텍스트로 받음

	channel = grpc.secure_channel('{}:{}'.format(HOST, PORT), UA.getCredentials())
	stub = gigagenieRPC_pb2_grpc.GigagenieStub(channel)

	message = gigagenieRPC_pb2.reqQueryText()
	message.queryText = text  # 질문할 텍스트
	message.userSession = "1234"  # 질의의 문맥을 유지할때 필요한 값으로 문맥에 따라 다르게 설정(코드로 보면 이해가 잘 안돼서 실제로 실행시켜봐야 알 것 같음)
	message.deviceId = "yourdevice"  # 해당 AI스피커의 정보, 디바이스에 따라 다르게 설정(보통 MAC주소로 설정)
		
	response = stub.queryByText(message)  # 입력한 질의어로 query API에 질문을 입력

	print ("\n\nresultCd: %d" % (response.resultCd))
	if response.resultCd == 200:
		print ("\n\n\n질의한 내용: %s" % (response.uword))
		#dssAction = response.action
		for a in response.action:
			response = a.mesg
		parsing_resp = response.replace('<![CDATA[', '')
		parsing_resp = parsing_resp.replace(']]>', '')
		print("\n\n질의에 대한 답변: " + parsing_resp + '\n\n\n')
		#return response.url
	else:
		print ("Fail: %d" % (response.resultCd))
		#return None	 

def main():

	# Dialog : queryByText
	queryByText("안녕")  # 질의어를 quertByText함수로 전달, 이떄의 질의어는 '안녕'


if __name__ == '__main__':
	main()
