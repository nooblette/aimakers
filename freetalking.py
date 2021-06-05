import STT_en as STT
import TTS_en
import pygametest as pygame
from collections import defaultdict
import accDB
import detect
import random
from time import sleep

food_Qlist = defaultdict(list)
mp_food = defaultdict(list)

hobby_Qlist = defaultdict(list)
mp_hobby = defaultdict(list)

test_Qlist = defaultdict(list)
mp_test = defaultdict(list)

friend_Qlist = defaultdict(list)
mp_friend = defaultdict(list)

class_Qlist = defaultdict(list)
mp_class = defaultdict(list)


# (sid, pid, stage)
def init_food_Qlist():
    food_Qlist[0].append(accDB.select_Freetalk(0,0,0)[0])
#    mp_food[0].append(accDB.select_Freetalk(0,0,0)[1])

    food_Qlist[0].append(accDB.select_Freetalk(0,0,1)[0])
#    mp_food[0].append(accDB.select_Freetalk(0,0,1)[1])

    food_Qlist[0].append(accDB.select_Freetalk(0,0,2)[0])
#    mp_food[0].append(accDB.select_Freetalk(0,0,2)[1])

    food_Qlist[0].append(accDB.select_Freetalk(0,0,3)[0])
#    mp_food[0].append(accDB.select_Freetalk(0,0,3)[1])

    food_Qlist[1].append(accDB.select_Freetalk(0,1,0)[0])
#    mp_food[1].append(accDB.select_Freetalk(0,1,0)[1])

    food_Qlist[1].append(accDB.select_Freetalk(0,1,1)[0])
#    mp_food[1].append(accDB.select_Freetalk(0,1,1)[1])

    food_Qlist[1].append(accDB.select_Freetalk(0,1,2)[0])
#    mp_food[1].append(accDB.select_Freetalk(0,1,2)[1])
    
def init_hobby_Qlist():
    hobby_Qlist[0].append(accDB.select_Freetalk(1,0,0)[0])
#    mp_hobby[0].append(accDB.select_Freetalk(1,0,0)[1])

    hobby_Qlist[0].append(accDB.select_Freetalk(1,0,1)[0])
#    mp_hobby[0].append(accDB.select_Freetalk(1,0,1)[1])

    hobby_Qlist[0].append(accDB.select_Freetalk(1,0,2)[0])
#    mp_hobby[0].append(accDB.select_Freetalk(1,0,2)[1])

    hobby_Qlist[0].append(accDB.select_Freetalk(1,0,3)[0])
#    mp_hobby[0].append(accDB.select_Freetalk(1,0,3)[1])

    hobby_Qlist[0].append(accDB.select_Freetalk(1,0,4)[0])
#    mp_hobby[0].append(accDB.select_Freetalk(1,0,4)[1])

    hobby_Qlist[1].append(accDB.select_Freetalk(1,1,0)[0])
#    mp_hobby[1].append(accDB.select_Freetalk(1,1,0)[1])

    hobby_Qlist[1].append(accDB.select_Freetalk(1,1,1)[0])
#    mp_hobby[1].append(accDB.select_Freetalk(1,1,1)[1])

    hobby_Qlist[1].append(accDB.select_Freetalk(1,1,2)[0])
#    mp_hobby[1].append(accDB.select_Freetalk(1,1,2)[1])

def init_friend_Qlist():
    friend_Qlist[0].append(accDB.select_Freetalk(2,0,0)[0])
#    mp_friend[0].append(accDB.select_Freetalk(2,0,0)[1])

    friend_Qlist[0].append(accDB.select_Freetalk(2,0,1)[0])
#   mp_friend[0].append(accDB.select_Freetalk(2,0,1)[1])

    friend_Qlist[0].append(accDB.select_Freetalk(2,0,2)[0])
#    mp_friend[0].append(accDB.select_Freetalk(2,0,2)[1])

def speech_recog():
    for i in range(5): # 5번까지만 인식해보고 안되면 return false
        try:
            answer = STT.main()
            print(answer) # for check
            return answer
        except UnboundLocalError:
            if i < 4:
                pygame.play_text("please_speech_again.mp3")
    return "not_recog"


def check_mp(answer, key, i, kind):
    return True
'''
    if kind == "food":
        cand_mp = mp_food[key]
    elif kind == "hobby":
        cand_mp = mp_hobby[key]
    elif kind == "friend":
        cand_mp = mp_friend[key]

    for check_mpw in cand_mp[i]:
        if check_mpw in answer:
            return True
    return False
'''

def print_q(key, qlist, kind):
    if kind == 'food': sid = 0
    elif kind == 'hobby': sid = 1
    elif kind == 'friend' : sid = 2

    for idx, q in enumerate(qlist):
        TTS_en.tts(q)
        pygame.play_text("sound.mp3")
        answer = speech_recog()
        print(answer) # for check

        if answer == "not_recog":
            #"대답하기 어렵구나, 다음에 또 불러줘"
            pygame.play_text("noanswer.mp3") # 사용자가 답을 안했을 때
            return False
        
        if check_mp(answer, key, idx, kind):
            accDB.insert_Freetalk_Answer(sid, key, idx, answer, 1) 
            continue # 다음 질문 하기

        else:
            pygame.play_text("incorrect.mp3")  # 이상한 대답을 했을때 (임의)
            return False

    # "즐거운 시간이였어"
    pygame.play_text("fun_en_talk.mp3")
    sleep(1)
    return True



def freetalking():
    pygame.play_text("let_talk.mp3")

    init_food_Qlist()
    init_hobby_Qlist()
    init_friend_Qlist()

    food_idx, hobby_idx, friend_idx  = set(), set(), set() 

    food_idx.add(random.choice([0, 1]))
    hobby_idx.add(random.choice([0, 1]))
    friend_idx.add(random.choice([0]))

    for idx in food_idx:
        if not print_q(idx, food_Qlist[idx], 'food'):
            continue

    for idx in hobby_idx:
        if not print_q(idx, hobby_Qlist[idx], 'hobby'):
            continue

    for idx in friend_idx:
        if not print_q(idx, friend_Qlist[idx], 'friend'):
            continue



#freetalking()
