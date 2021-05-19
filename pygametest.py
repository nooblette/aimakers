import pygame

def play_text(mp3_file):
    # music_file = "test_question1.mp3"   # mp3 or mid file


    freq = 24000    # sampling rate, 44100(CD), 16000(Naver TTS), 24000(google TTS)
    bitsize = -16   # signed 16 bit. support 8,-8,16,-16
    channels = 1    # 1 is mono, 2 is stereo
    buffer = 2048   # number of samples (experiment to get right sound)

    # default : pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096) //default는 사운드 속도가 비정상적
    pygame.mixer.init(freq, bitsize, channels, buffer)
    pygame.mixer.music.load(mp3_file)
    pygame.mixer.music.play()

    clock = pygame.time.Clock()
    while pygame.mixer.music.get_busy():
        clock.tick(30)
    pygame.mixer.quit()    

# Pygame은 아래와 같은 다양한 함수를 제공한다.
# 
# 멈추기( pygame.mixer.music.stop() )
# 볼륨 설정(예 pygame.mixer.music.set_volume(0.8))
# 페이드아웃(예 pygame.mixer.music.fadeout(1000))
# 자세한건 https://www.pygame.org/docs/ 참고
