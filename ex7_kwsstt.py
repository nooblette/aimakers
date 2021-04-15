#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Date:2019.02.18
Example 7: 호출어 음성인식 결합 예제
"""
from __future__ import print_function

import time
import ex2_getVoice2Text as gv2t  #ex2 Sound To Text
import ex1_kwstest as kws  #ex1 호출어 인식

def main():  # ex1과 ex2를 합침, 호출어를 사용하여 AMK를 호출하고, 음성을 텍스트로 받음
	#Example7 KWS+STT
	#KWS -> ex1_kwstest : 호출어를 인식
	#gv2t -> ex2_getVoice2Text : 기가지니를 호출 한 후 음성으로 데이터 입력
	#KWS로 기가지니 호출 -> gv2t로 음성으로 데이터 입력

	KWSID = ['기가지니', '지니야', '친구야', '자기야']
	while 1:
		recog=kws.test(KWSID[0])  # '기가지니' 로 스피커 호출
		if recog == 200:
			print('KWS Dectected ...\n Start STT...')
			text = gv2t.getVoice2Text()  # 음성으로 입력받은 데이터를 텍스트로 변환해서 리턴
			print('Recognized Text: '+ text)  # 리턴받은 데이터를 화면에 출력
			time.sleep(2)  # 2초동안 아무 반응 없으면 종료
			
		else:
			print('KWS Not Dectected ...')

if __name__ == '__main__':
    main()
