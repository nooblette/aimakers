import STT
import TTS
import pygametest as pygame
from collections import defaultdict
import accDB
#import pygameForScriptTS as BOOK
import detect
import random

feeling_Qlist = defaultdict(list)
mp_feeling = defaultdict(list)

contents_Qlist = defaultdict(list)
mp_contents = defaultdict(list)

english_Qlist = defaultdict(list)
mp_english = defaultdict(list)


def init_feeling_Qlist():
    feeling_Qlist[0].append(accDB.select_question(0, 1, 0, 0)[0])
    feeling_Qlist[0].append(accDB.select_question(0, 1, 0, 1)[0])
    mp_feeling[0].append(accDB.select_question(0, 1, 0, 0)[1].split(','))
    mp_feeling[0].append(accDB.select_question(0, 1, 0, 1)[1].split(','))

    feeling_Qlist[1].append(accDB.select_question(0, 1, 1, 0)[0])
    feeling_Qlist[1].append(accDB.select_question(0, 1, 1, 1)[0])
    mp_feeling[1].append(accDB.select_question(0, 1, 1, 0)[1].split(','))
    mp_feeling[1].append(accDB.select_question(0, 1, 1, 1)[1].split(','))

    feeling_Qlist[2].append(accDB.select_question(0, 1, 2, 0)[0])
    feeling_Qlist[2].append(accDB.select_question(0, 1, 2, 1)[0])
    mp_feeling[2].append(accDB.select_question(0, 1, 2, 0)[1].split(','))
    mp_feeling[2].append(accDB.select_question(0, 1, 2, 1)[1].split(','))

    feeling_Qlist[3].append(accDB.select_question(0, 1, 3, 0)[0])
    feeling_Qlist[3].append(accDB.select_question(0, 1, 3, 1)[0])
    mp_feeling[3].append(accDB.select_question(0, 1, 3, 0)[1].split(','))
    mp_feeling[3].append(accDB.select_question(0, 1, 3, 1)[1].split(','))

    feeling_Qlist[4].append(accDB.select_question(0, 1, 4, 0)[0])
    feeling_Qlist[4].append(accDB.select_question(0, 1, 4, 1)[0])
    mp_feeling[4].append(accDB.select_question(0, 1, 4, 0)[1].split(','))
    mp_feeling[4].append(accDB.select_question(0, 1, 4, 1)[1].split(','))

'''
# (cid, bid, qid, stage)
def init_contents_Qlist():
    contents_Qlist[0] = [accDB.select_question(1, 1, 0, 0)[0], accDB.select_question(1, 1, 0, 1)[0]]
    mp_contents[0] = [accDB.select_question(1, 1, 0, 0)[1].split(','), accDB.select_question(1, 1, 0, 1)[1].split(',')]

    contents_Qlist[1] = [accDB.select_question(1, 1, 1, 0)[0], accDB.select_question(1, 1, 1, 1)[0]]
    mp_contents[1] = [accDB.select_question(1, 1, 1, 0)[1].split(','), accDB.select_question(1, 1, 1, 1)[1].split(',')]

    contents_Qlist[2] = [accDB.select_question(1, 1, 2, 0)[0], accDB.select_question(1, 1, 2, 1)[0]]
    mp_contents[2] = [accDB.select_question(1, 1, 2, 0)[1].split(','), accDB.select_question(1, 1, 2, 1)[1].split(',')]

    contents_Qlist[3] = [accDB.select_question(1, 1, 3, 0)[0], accDB.select_question(1, 1, 3, 1)[0]]
    mp_contents[3] = [accDB.select_question(1, 1, 3, 0)[1].split(','), accDB.select_question(1, 1, 3, 1)[1].split(',')]

    contents_Qlist[4] = [accDB.select_question(1, 1, 4, 0)[0], accDB.select_question(1, 1, 4, 1)[0]]
    mp_contents[4] = [accDB.select_question(1, 1, 4, 0)[1].split(','), accDB.select_question(1, 1, 4, 1)[1].split(',')]

    contents_Qlist[5] = [accDB.select_question(1, 1, 5, 0)[0]]
    mp_contents[5] = [accDB.select_question(1, 1, 5, 0)[1].split(',')]

    contents_Qlist[6] = [accDB.select_question(1, 1, 6, 0)[0], accDB.select_question(1, 1, 6, 1)[0],
                         accDB.select_question(1, 1, 6, 2)[0]]
    mp_contents[6] = [accDB.select_question(1, 1, 6, 0)[1].split(','), accDB.select_question(1, 1, 6, 1)[1].split(','),
                      accDB.select_question(1, 1, 6, 2)[1].split(',')]

    contents_Qlist[7] = [accDB.select_question(1, 1, 7, 0)[0], accDB.select_question(1, 1, 7, 1)[0]]
    mp_contents[7] = [accDB.select_question(1, 1, 7, 0)[1].split(','), accDB.select_question(1, 1, 7, 1)[1].split(',')]


# (cid, bid, qid, stage)
def init_englist_Qlist():
    english_Qlist[0] = [accDB.select_question(2, 1, 0, 0)[0]]
    mp_english[0] = [accDB.select_question(2, 1, 0, 0)[1].split(',')]

    english_Qlist[1] = [accDB.select_question(2, 1, 1, 0)[0]]
    mp_english[1] = [accDB.select_question(2, 1, 1, 0)[1].split(',')]

    english_Qlist[2] = [accDB.select_question(2, 1, 2, 0)[0]]
    mp_english[2] = [accDB.select_question(2, 1, 2, 0)[1].split(',')]

    english_Qlist[3] = [accDB.select_question(2, 1, 3, 0)[0]]
    mp_english[3] = [accDB.select_question(2, 1, 3, 0)[1].split(',')]

    english_Qlist[4] = [accDB.select_question(2, 1, 4, 0)[0]]
    mp_english[4] = [accDB.select_question(2, 1, 4, 0)[1].split(',')]

    english_Qlist[5] = [accDB.select_question(2, 1, 5, 0)[0]]
    mp_english[5] = [accDB.select_question(2, 1, 5, 0)[1].split(',')]

    english_Qlist[6] = [accDB.select_question(2, 1, 6, 0)[0]]
    mp_english[6] = [accDB.select_question(2, 1, 6, 0)[1].split(',')]


def check_mp(answer, key, i, kind):
    if kind == "f":
        cand_mp = mp_feeling[key]
    elif kind == "c":
        cand_mp = mp_contents[key]
    elif kind == "e":
        cand_mp = mp_english[key]

    for check_mpw in cand_mp[i]:
        if check_mpw in answer:
            return True
    return False


def print_q(key, qlist, kind):
    for i, q in enumerate(qlist):
        TTS.tts(q)
        pygame.play_text("sound.mp3")
        answer = STT.main()
        print(answer)  # for check
        if check_mp(answer, key, i, kind):
            accDB.insert_quiz_answer(1, key, i, answer, 1)
            continue
        else:
            # TTS.tts("흥미로운 대답이네요") # set parameter to text wanted to switch sound
            pygame.play_text("incorrect.mp3")  # play mp3 file
            accDB.insert_quiz_answer(1, key, i, answer, 0)
            return False
    pygame.play_text("correct.mp3")
    return True


# 우선 이렇게 짜보고, 시간 여유 있으면 버튼인식하는걸 다른 프로세스에서 돌려서 시그널 보내는 방식으로 수정해보기
def reading():
    pygame.play_text("성냥팔이 소녀 읽어줄게.mp3")  # 미리 mp3 파일로 저장해놓기
    while True:
        BOOK.reading()  # 영어로
        if detect.btn_detect():
            BOOK.reading()  # 영어 문장 반복
        BOOK.reading()  # 한글로
        if detect.btn_detect():
            BOOK.reading()  # 영어 문장 반복


def quiz():
    pygame.play_text("재밌었어? 퀴즈도 풀어보자")  # 미리 mp3 파일로 저장해놓기

    init_feeling_Qlist()  # initialize feeling question list
    init_contents_Qlist()  # initialize contents question list
    init_englist_Qlist()  # initialize english question list

    feeling_idx, contents_idx, english_idx = set(), set(), set()

    # randomly indexing
    feeling_idx.add(random.choice([0, 1, 2, 3, 4]))
    feeling_idx.add(random.choice([0, 1, 2, 3, 4]))
    contents_idx.add(random.choice([0, 1, 2, 3, 4, 5, 6, 7]))
    contents_idx.add(random.choice([0, 1, 2, 3, 4, 5, 6, 7]))
    english_idx.add(random.choice([0, 1, 2, 3, 4, 5, 6]))
    english_idx.add(random.choice([0, 1, 2, 3, 4, 5, 6]))

    for idx in feeling_idx:
        if not print_q(idx, feeling_Qlist[idx], 'f'):
            continue

    for idx in contents_idx:
        if not print_q(idx, contents_Qlist[idx], 'c'):
            continue

    for idx in english_idx:
        if not print_q(idx, english_Qlist[idx], 'e'):
            continue

    '''
'''
    for key, qlist in feeling_Qlist.items():
        if print_q(key, qlist, 'f') == False:
            continue  # pass to next question

    for key, qlist in contents_Qlist.items():
        if print_q(key, qlist, 'c') == False:
            continue
    '''

'''
def book_report():
    pygame.play_text("느낀점을 한줄로 말해줘.mp3")  # 미리 mp3 파일로 저장해놓기
    contents = STT.main()
    print(contents)  # for check
    accDB.insert_book_report(1, contents)
'''