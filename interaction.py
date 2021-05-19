import STT
import TTS
import pygametest as pygame
from  collections import defaultdict

feeling_Qlist = defaultdict(list)
mp_feeling = defaultdict(list)

contents_Qlist = defaultdict(list)
mp_contents = defaultdict(list)

def init_feeling_Qlist():
    feeling_Qlist[0] = ["성냥팔이 소녀가 혼자 분수 옆에 앉아있었을 때 기분이 어땠을까요?", "왜 슬펐을까요?"]
    mp_feeling[0] = [["슬펐","슬퍼", "쓸", "슈"], ["혼자", "추위", "외로", "외롭", "슬퍼", "슬펐"]]

    feeling_Qlist[1] = ["성냥팔이 소녀가 성냥을 한 상자도 팔지 못했을 때 기분이 어땠을까요?", "왜 그렇게 생각했나요?"]
    mp_feeling[1] = [["두려", "고려", "무서", "무섭", "걱정"], ["아빠", "아버지", "화", "분노", "두려" ,"무서", "무섭"]] 

    feeling_Qlist[2] = ["소녀가 성냥에 불을 붙여 따뜻한 음식들과 난로를 보았을 때 기분이 어땠을까요?", "왜 그렇게 생각했나요?"]
    mp_feeling[2] = [["행복", "기뻤", "꿈", "깁", "집", "지"], [ "원했", "갖고", "희망", "소망"]]

    feeling_Qlist[3] = ["소녀가 할머니를 봤을 때 기분이 어땠을까요?", "왜 그렇게 생각했나요?"]
    mp_feeling[3] = [["행복", "기뻤", "꿈", "깁", "집", "지"], ["그리워", "보고싶"]]

    feeling_Qlist[4] = ["길에서 성냥팔이 소녀를 발견한 사람들의 기분은 어땠을까요?", "왜 그렇게 생각했을까요?"]
    mp_feeling[4] = [["안타까", "불쌍", "가엾","가여", "됐다", "없", "엽"], ["외로","외롭",  "혼자", "안타까", "불쌍" ,"누워", "누웠"]]

def init_contents_Qlist():
    contents_Qlist[0] = ["아빠는 왜 화를 낼 것 같나요?", "왜 하나도 팔지 못했을까요?"]
    mp_contents[0] = [[],[]]

    contents_Qlist[1] = ["아빠에게 왜 거짓말을 했을까요?", "아빠는 왜 성냥을 사용하지 못하도록 했을까요?"]
    mp_contents[1] = [[],[]]

    contents_Qlist[2] = ["음식이 진짜일까요 가짜일까요?", "왜 가짜음식이 보였을까요?"]
    mp_contents[2] = [[],[]]

    contents_Qlist[3] = ["소녀의 인생에서 부족했던 것은 무엇이었을까요?", "왜 그렇게 생각했나요?"]
    mp_contents[3] = [[],[]]

    contents_Qlist[4] = ["소녀는 무엇을 위해 기도했나요?", "왜 그런 기도를 했을까요?"]
    mp_contents[4] = [[],[]]

    contents_Qlist[5] = ["친구가 이 동화의 소녀였다면 성냥에 불을 붙였을때 어떤 것이 떠올랐을까요?"]
    mp_contents[5] = [[],[]]

    contents_Qlist[6] = ["성냥팔이 소녀가 가장 보고싶었던 사람은 누구였을까요?", "할머니를 더 보기위해 소녀는 어떤 행동을 했나요?", "성냥을 켰을떄 할머니가 어떻게 됐나요?"]
    mp_contents[6] = [[],[]]

    contents_Qlist[7] = ["성냥팔이 소녀는 마지막에 어떻게 됐나요?", "그때 소녀의 기분은 어땠을까요?"]
    mp_contents[7] = [[],[]]



def check_mp(answer, key, i, kind):
    if kind == "f" : cand_mp = mp_feeling[key]
    elif kind == "c": cand_mp = mp_contents[key]

    for check_mp in cand_mp[i]:
        if check_mp in answer:
            return True
    return False


	

def print_q(key, qlist, kind):
    for i, q in enumerate(qlist):
        TTS.tts(q)
        pygame.play_text("sound.mp3")
        answer = STT.main()
        print(answer) # for check
        if check_mp(answer, key, i, kind) == True:
            continue
        else:
            # TTS.tts("흥미로운 대답이네요") # set parameter to text wanted to switch sound
            pygame.play_text("incorrect.mp3") # play mp3 file
            return False
    pygame.play_text("correct.mp3")
    return True


def QnA():
    init_feeling_Qlist() # initialize feeling question list
    init_contents_Qlist() # initialize contents question list
    for key, qlist in feeling_Qlist.items():
        if print_q(key, qlist, 'f') == False:
            continue # pass to next question

    for key, qlist in contents_Qlist.items():
        if print_q(key, qlist, 'c') == False:
            continue
