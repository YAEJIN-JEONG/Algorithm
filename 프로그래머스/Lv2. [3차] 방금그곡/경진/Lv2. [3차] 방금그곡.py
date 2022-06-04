# https://programmers.co.kr/learn/courses/30/lessons/17683
def solution(m, musicinfos):
    musics, convert = [], {'C#': 'H', 'D#': 'I', 'F#': 'J', 'G#': 'K', 'A#': 'L'}

    # '#' 붙은 애들 바꾸기
    for k, v in convert.items():
        m = m.replace(k, v)

    for info in musicinfos:
        s, e, title, melody = info.split(',')
        sh, sm = map(int, s.split(':'))
        eh, em = map(int, e.split(':'))
        # 재생 시간
        playtime = eh * 60 + em - sh * 60 - sm

        # '#' 붙은 애들 바꾸기
        for k, v in convert.items():
            melody = melody.replace(k, v)

        # [재생 멜로디, 곡 이름]
        musics.append([melody * (playtime // len(melody)) + melody[:playtime % len(melody)], title])

    # 재생 멜로디 길이 기준 내림차순 정렬
    musics.sort(key=lambda x: len(x[0]), reverse=True)

    for melody, title in musics:
        if m in melody:
            return title

    return '(None)'
