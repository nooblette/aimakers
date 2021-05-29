import STT
import TTS
import pygametest as pygame
import accDB
import detect


def call():
    speech = STT.main()
    keywords = ["리딩버드"]
    for keyword in keywords:
        if keyword in speech:
            return True
    return False
