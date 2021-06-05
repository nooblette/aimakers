import STT
import TTS
import pygametest as pygame
from collections import defaultdict
import accDB
import freetalking
import reading
from time import sleep

def speech_recog():
    for i in range(5): # 5번까지만 인식해보고 안되면 return false
        try:
            answer = STT.main()
            print(answer) # for check
            return answer
        except UnboundLocalError:
            if i < 4:
                pygame.play_text("please_speech_again.mp3")

    pygame.play_text("not_accept.mp3")
    return "not_recog"


def choose():
    # TTS.tts("책 읽어줄까? 아니면 나랑 애기할래?")
    pygame.play_text("choose.mp3")  # 미리 mp3파일로 저장해놓았다가 출력하는 것만 구현
    sleep(1)
    answer = speech_recog()
    if answer == "not_recog":
        pygame.play_text("call_me_again.mp3")
        return

    keywords_b = ["책", "첵", "채", "체"]
    keywords_t = ["얘", "예", "이", "야"]

    for keyword in keywords_b:
        if keyword in answer:
            reading.reading()
            sleep(1)
            reading.quiz()
            sleep(1)
            reading.book_report()
            pygame.play_text("fun_talk.mp3")
            pygame.play_text("call_me_again.mp3")
            return

    for keyword in keywords_t:
        if keyword in answer:
            freetalking.freetalking()
            sleep(1)
            #pygame.play_text("fun_talk.mp3")
            pygame.play_text("call_me_again.mp3")
            return

    pygame.play_text("call_me_again.mp3")
    return
