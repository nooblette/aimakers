import STT
import TTS
import pygametest as pygame
from collections import defaultdict

feeling_Qlist = defaultdict(list)
mp_feeling = defaultdict(list)

contents_Qlist = defaultdict(list)
mp_contents = defaultdict(list)

english_Qlist = defaultdict(list)
mp_english = defaultdict(list)


def init_feeling_Qlist():
    feeling_Qlist[0] = ["성냥팔이 소녀가 혼자 분수 옆에 앉아있었을 때 기분이 어땠을까요?", "왜 슬펐을까요?"]
    mp_feeling[0] = [["슬펐", "슬퍼", "쓸", "슈"], ["혼자", "추위", "외로", "외롭", "슬퍼", "슬펐"]]

    feeling_Qlist[1] = ["성냥팔이 소녀가 성냥을 한 상자도 팔지 못했을 때 기분이 어땠을까요?", "왜 그렇게 생각했나요?"]
    mp_feeling[1] = [["두려", "고려", "무서", "무섭", "걱정"], ["아빠", "아버지", "화", "분노", "두려", "무서", "무섭"]]

    feeling_Qlist[2] = ["소녀가 성냥에 불을 붙여 따뜻한 음식들과 난로를 보았을 때 기분이 어땠을까요?", "왜 그렇게 생각했나요?"]
    mp_feeling[2] = [["행복", "기뻤", "꿈", "깁", "집", "지"], ["원했", "갖고", "희망", "소망"]]

    feeling_Qlist[3] = ["소녀가 할머니를 봤을 때 기분이 어땠을까요?", "왜 그렇게 생각했나요?"]
    mp_feeling[3] = [["행복", "기뻤", "꿈", "깁", "집", "지"], ["그리워", "보고싶"]]

    feeling_Qlist[4] = ["길에서 성냥팔이 소녀를 발견한 사람들의 기분은 어땠을까요?", "왜 그렇게 생각했을까요?"]
    mp_feeling[4] = [["안타까", "불쌍", "가엾", "가여", "됐다", "없", "엽"], ["외로", "외롭", "혼자", "안타까", "불쌍", "누워", "누웠"]]


def init_contents_Qlist():
    contents_Qlist[0] = ["소녀는 무엇을 입고 있었나요?", "왜 그런 옷을 입고 있었을 까요?"]
    mp_contents[0] = [["드레스", "목도리"], ["돈", "경제", "여유", "가난"]]

    contents_Qlist[1] = ["성냥을 다 못팔면 아빠는 어떻게 행동할것 같나요?", "왜 그렇게 행동할까요?"]
    mp_contents[1] = [["화", "혼"], [" "]]

    contents_Qlist[2] = ["성냥을 사용하지 않았다고 얘기한것은 거짓말인가요 아닌가요?", "왜 거짓말을 했을까요??"]
    mp_contents[2] = [["거짓말"], ["성냥", "사용", "못"]]

    contents_Qlist[3] = ["음식은 진짜인가요?", "가짜인 음식이 왜 보였을까요?"]
    mp_contents[3] = [["아니", "가짜"], ["맛있는", "배고파", "먹고"]]

    # 이 질문은 구현하기 애매해서 제외했습니다
    # contents_Qlist[4] = ["소녀의 인생에서 없었던 것은 무엇인가요?", "왜 없었을까요?"]
    # mp_contents[4] = [[],[]]

    contents_Qlist[4] = ["소녀는 무엇을 기도했을까요?", "왜 그렇게 생각했나요?"]
    mp_contents[4] = [["행복", "즐거움", "기쁨", "맛", "따뜻"], ["힘들", "배고", "추워", "배고", "슬픔", "가난"]]

    contents_Qlist[5] = ["친구가 주인공이였다면 성냥에 불을 붙였을때 어떤것이 나타났을 것 같나요?"]
    mp_contents[5] = [" "]

    contents_Qlist[6] = ["성냥팔이 소녀가 가장 보고 싶었던 사람은 누구였을까요?", "할머니를 보기위해 성냥팔이 소녀는 어떻게 했나요?", "성냥을 켰을 때 할머니가 어떻게 됐나요?"]
    mp_contents[6] = [["할"], ["성냥", "하나", "더"], ["사라", "없어"]]

    contents_Qlist[7] = ["마지막에 성냥팔이 소녀는 어떻게 됐나요?", "그때 소녀는 어떤 기분이였을까요?"]
    mp_contents[7] = [["죽어", "죽었", "사라"], [" "]]


def init_englist_Qlist():
    english_Qlist[0] = ["What caused the girl's death?"]
    mp_english[0] = ["cold"]

    english_Qlist[1] = ["What did the girl want from the vision of the match?"]
    mp_english[1] = ["happiness"]

    english_Qlist[2] = ["What day did the story take place?"]
    mp_english[2] = ["one"]

    english_Qlist[3] = ["What caused the girl to use matches the most?"]
    mp_english[3] = ["grandmother, vision"]

    english_Qlist[4] = ["How the girl felt through matches."]
    mp_english[4] = ["craving", "longing", "liberation"]

    english_Qlist[5] = ["What did the girl see through the match?"]
    mp_english[5] = ["burning", "stove", "food", "christmas", "tree", "grandmother"]

    english_Qlist[6] = ["The reason why the girl didn't go home."]
    mp_english[6] = ["father", "daddy", "dad", "angry", "tell off", "matches"]


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
