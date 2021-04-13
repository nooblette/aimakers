#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Example 2: STT - getVoice2Text """

from __future__ import print_function

import grpc
import gigagenieRPC_pb2
import gigagenieRPC_pb2_grpc
import MicrophoneStream as MS
import user_auth as UA
import audioop
import os
from ctypes import *

HOST = 'gate.gigagenie.ai'
PORT = 4080
RATE = 16000
CHUNK = 512

ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)
def py_error_handler(filename, line, function, err, fmt):
  dummy_var = 0
c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)
asound = cdll.LoadLibrary('libasound.so')
asound.snd_lib_error_set_handler(c_error_handler)

def generate_request():  # 마이크에서 가져온 데이터를 기가지니 STT API에 입력할 수 있도록 변환 (API호출은 하루 최대 500건)
    with MS.MicrophoneStream(RATE, CHUNK) as stream:
        audio_generator = stream.generator()
    
        for content in audio_generator:
            message = gigagenieRPC_pb2.reqVoice()
            message.audioContent = content
            yield message
            
            rms = audioop.rms(content,2)
            #print_rms(rms)

def getVoice2Text():	
    print ("\n\n음성인식을 시작합니다.\n\n종료하시려면 Ctrl+\ 키를 누루세요.\n\n\n")
    channel = grpc.secure_channel('{}:{}'.format(HOST, PORT), UA.getCredentials())
    stub = gigagenieRPC_pb2_grpc.GigagenieStub(channel)
    # line 43,44 : user_auth.py 파일에서 입력한 client id,ket,secret(사용자의 인증 API키)를 받아서 GRPC 패키지를 사용
    # GRPC -> 라즈베리파이와 서버가 통신하기위해 사용하는 프로토콜, 인증된 API 모듈로 STT, TTS, Query 사용가능
    
    request = generate_request()
    resultText = ''
    for response in stub.getVoice2Text(request):
        if response.resultCd == 200: # partial, 계속 인식될 때
            print('resultCd=%d | recognizedText= %s'
                  % (response.resultCd, response.recognizedText))
            resultText = response.recognizedText
        elif response.resultCd == 201: # final, 인식이 완료되고 최종적인 값을 출력할때
            print('resultCd=%d | recognizedText= %s' 
                  % (response.resultCd, response.recognizedText))
            resultText = response.recognizedText
            break
        else:
            print('resultCd=%d | recognizedText= %s' 
                  % (response.resultCd, response.recognizedText))
            break

    print ("\n\n인식결과: %s \n\n\n" % (resultText))  # 인식이 끝나면 인식 결과를 출력하고 결과로 변환된 text를 리턴
    return resultText

def main():
    # Sound To Text(STT)
    text = getVoice2Text()  # 인식된 음성을 텍스트로 바꾸어서 text라는 변수에 리턴, 음성인식은 100글자 이하만 가능

if __name__ == '__main__':
    main()
