import STT
import TTS
import pygametest as pygame
from collections import defaultdict
import accDB
import reading


def choose():
    # TTS.tts("책 읽어줄까? 아니면 나랑 애기할래?")
    pygame.play_text("choose.mp3")  # 미리 mp3파일로 저장해놓았다가 출력하는 것만 구현
    answer = STT.main()
    keywords_b = ["책", "첵", "채", "체"]
    keywords_t = ["얘", "예", "이", "야"]

    for keyword in keywords_b:
        if keyword in answer:
            reading.reading()
            reading.quiz()
            reading.book_report()
            return

    for keyword in keywords_t:
        if keyword in answer:
            return

    pygame.play_text("call_me_again.mp3")

