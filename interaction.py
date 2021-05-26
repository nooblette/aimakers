import STT
import TTS
import pygametest as pygame
from collections import defaultdict
import accDB

feeling_Qlist = defaultdict(list)
mp_feeling = defaultdict(list)

contents_Qlist = defaultdict(list)
mp_contents = defaultdict(list)

english_Qlist = defaultdict(list)
mp_english = defaultdict(list)


def init_feeling_Qlist():
    feeling_Qlist[0] = [accDB.select_question(0, 1, 0, 0)[0], accDB.select_question(0, 1, 0, 1)[0]]
    mp_feeling[0] = [accDB.select_question(0, 1, 0, 0)[1].split(','), accDB.select_question(0, 1, 0, 1)[1].split(',')]

    feeling_Qlist[1] = [accDB.select_question(0, 1, 1, 0)[0], accDB.select_question(0, 1, 1, 1)[0]]
    mp_feeling[1] = [accDB.select_question(0, 1, 1, 0)[1].split(','), accDB.select_question(0, 1, 1, 1)[1].split(',')]

    feeling_Qlist[2] = [accDB.select_question(0, 1, 2, 0)[0], accDB.select_question(0, 1, 2, 1)[0]]
    mp_feeling[2] = [accDB.select_question(0, 1, 2, 0)[1].split(','), accDB.select_question(0, 1, 2, 1)[1].split(',')]

    feeling_Qlist[3] = [accDB.select_question(0, 1, 3, 0)[0], accDB.select_question(0, 1, 3, 1)[0]]
    mp_feeling[3] = [accDB.select_question(0, 1, 3, 0)[1].split(','), accDB.select_question(0, 1, 3, 1)[1].split(',')]

    feeling_Qlist[4] = [accDB.select_question(0, 1, 4, 0)[0], accDB.select_question(0, 1, 4, 1)[0]]
    mp_feeling[4] = [accDB.select_question(0, 1, 4, 0)[1].split(','), accDB.select_question(0, 1, 4, 1)[1].split(',')]

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

    contents_Qlist[6] = [accDB.select_question(1, 1, 6, 0)[0], accDB.select_question(1, 1, 6, 1)[0], accDB.select_question(1, 1, 6, 2)[0]]
    mp_contents[6] = [accDB.select_question(1, 1, 6, 0)[1].split(','), accDB.select_question(1, 1, 6, 1)[1].split(','), accDB.select_question(1, 1, 6, 2)[1].split(',')]

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

    for check_mp in cand_mp[i]:
        if check_mp in answer:
            return True
    return False


def print_q(key, qlist, kind):
    for i, q in enumerate(qlist):
        TTS.tts(q)
        pygame.play_text("sound.mp3")
        answer = STT.main()
        print(answer)  # for check
        if check_mp(answer, key, i, kind):
            continue
        else:
            # TTS.tts("흥미로운 대답이네요") # set parameter to text wanted to switch sound
            pygame.play_text("incorrect.mp3")  # play mp3 file
            return False
    pygame.play_text("correct.mp3")
    return True


def QnA():
    init_feeling_Qlist()  # initialize feeling question list
    init_contents_Qlist()  # initialize contents question list
    for key, qlist in feeling_Qlist.items():
        if print_q(key, qlist, 'f') == False:
            continue  # pass to next question

    for key, qlist in contents_Qlist.items():
        if print_q(key, qlist, 'c') == False:
            continue

