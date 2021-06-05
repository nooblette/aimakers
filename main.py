import STT
import TTS
import pygametest as pygame
import reading
import interaction
import time

from  collections import defaultdict


def call():
    try:
        speech = STT.main()
        keywords = ["리","버"]
        for keyword in keywords:
            if keyword in speech:
                return True
            else : return False 
    except UnboundLocalError:
        #pygame.play_text("please_speech_again.mp3")
        return False



if __name__ == "__main__":
    while True:
        while True:
            if call():
                pygame.play_text("birdsong_real_1.wav")  # 미리 mp3파일로 저장해놓았다가 출력하는 것만 구현
                interaction.choose()
            continue
