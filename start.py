import STT
import TTS
import pygametest as pygame
import accDB
import detect


def call():
    speech = STT.main()
    print(speech)
    keywords = ["리", "버"]
    for keyword in keywords:
        if keyword in speech:
            return True
    return False
