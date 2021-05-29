import STT
import TTS
import pygametest as pygame
import reading
import start
import interaction
import time

from  collections import defaultdict


if __name__ == "__main__":
    while True:
        while True:
            if start.call():
                pygame.play_text("새소리.mp3")  # 미리 mp3파일로 저장해놓았다가 출력하는 것만 구현
                break
        interaction.choose()
        time.sleep(5)  # pause 5 second