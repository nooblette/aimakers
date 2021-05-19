import STT
import TTS
import pygametest as pygame
from  collections import defaultdict

feeling_Qlist = defaultdict(list)
mp_feeling = defaultdict(list)

def init_feeling_Qlist():
    feeling_Qlist[0] = ["성냥팔이 소녀가 혼자 분수 옆에 앉아있었을 때 기분이 어땠을까요?", "왜 슬펐을까요?"]
    mp_feeling[0] = [["슬펐","슬퍼", "쓸", "슬"], ["혼자", "추위", "외로", "외롭", "슬퍼", "슬펐"]]

    feeling_Qlist[1] = ["성냥팔이 소녀가 성냥을 한 상자도 팔지 못했을 때 기분이 어땠을까요?", "왜 그렇게 생각했나요?"]
    mp_feeling[1] = [["두려", "무서", "무섭", "걱정"], ["아빠", "아버지", "화", "분노", "두려" ,"무서", "무섭"]] 

    feeling_Qlist[2] = ["소녀가 성냥에 불을 붙여 따뜻한 음식들과 난로를 보았을 때 기분이 어땠을까요?", "왜 행복했을까요?"]
    mp_feeling[2] = [["행복", "기뻤", "꿈"], [ "원했", "갖고", "희망", "소망"]]

    feeling_Qlist[3] = ["소녀가 할머니를 봤을 때 기분이 어땠을까요?", "왜 행복했을까요?"]
    mp_feeling[3] = [["행복", "기뻤", "꿈"], ["그리워", "보고싶"]]

    feeling_Qlist[4] = ["길에서 성냥팔이 소녀를 발견한 사람들의 기분은 어땠을까요?", "왜 그렇게 생각했을까요?"]
    mp_feeling[4] = [["안타까", "불쌍", "가엾"], ["외로","외롭",  "혼자", "안타까", "불쌍" ,"누워", "누웠"]]


def check_mp(answer, key, i):
    cand_mp = mp_feeling[key]
    for check_mp in cand_mp[i]:
        if check_mp in answer:
            return True
    return False
	

def print_q(key, qlist):
    for i, q in enumerate(qlist):
        TTS.tts(q)
        pygame.play_text("sound.mp3")
        answer = STT.main()
        print(answer) # for check
        if check_mp(answer, key, i) == True:
            continue
        else:
            # TTS.tts("흥미로운 대답이네요") # set parameter to text wanted to switch sound
            pygame.play_text("incorrect.mp3") # play mp3 file
            return False
    pygame.play_text("correct.mp3")
    return True


if __name__ == "__main__":
    init_feeling_Qlist() # initialize question list

    for key, qlist in feeling_Qlist.items():
        if print_q(key, qlist) == False:
            continue # pass to next question
