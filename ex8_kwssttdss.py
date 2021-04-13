#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Date:2019.02.18
Example 8: 음성인식 TTS 대화 결합 예제
"""

from __future__ import print_function

import MicrophoneStream as MS
import ex1_kwstest as kws  # ex1 호출하기
import ex4_getText2VoiceStream as tts  #ex4 Text To Sound
import ex6_queryVoice as dss  #ex6 음성대화
import time

def main():
	#Example8 KWS+STT+DSS
	#호출어로 Ai Makers Kit를 호출하고 대화
	#kws로 호출 -> dss로 음성으로 질문하고 텍스트로 답변받음 -> tts로 답변받은 텍스트를 음성으로 출력

	KWSID = ['기가지니', '지니야', '친구야', '자기야']
	while 1:
		recog=kws.test(KWSID[0])  # 기가지니 호출
		if recog == 200:
			print('KWS Dectected ...\n')
			dss_answer = dss.queryByVoice()  # 음성으로 질문하고 답변을 dss_answer에 받음
			tts_result = tts.getText2VoiceStream(dss_answer, "result_mesg.wav")  # 답변받은 텍스트를 음성으로 변환해서 결과를 result_mesg.wav라는 파일에 저장
			if dss_answer == '':
				print('질의한 내용이 없습니다.\n\n\n')
			elif tts_result == 500:
				print("TTS 동작 에러입니다.\n\n\n")
				break
			else:
				MS.play_file("result_mesg.wav")	 # 답변받은 텍스트로 만든 음성파일을 읽어서 음성으로 질문의 결과를 출력	
			time.sleep(2)  # 2초간 프로세스 중지
		else:
			print('KWS Not Dectected ...')

if __name__ == '__main__':
    main()
