from collections import Counter, defaultdict
from typing import DefaultDict, TextIO

"""
## 개쩌네 
def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer



def solution(genres, plays):
    answer = []
    # { 장르 : 총 재생 횟수 } 사전
    playsDict = {}
    # { 장르 : [ ( 플레이 횟수, 고유 번호 ) ] }
    d = { }

    # 사전들 초기화
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        playsDict[genre] = playsDict.get(genre, 0) + play
        d[genre] = d.get(genre, []) + [ (play, i) ]
        
    # 재생 횟수 내림차순으로 장르별로 정렬
    genreSort = sorted(playsDict.items(), key=lambda x: x[1], reverse=True)
    
    # 재생 횟수 내림차순, 인덱스 오름차순 정렬
    # 장르별로 최대 2개 선택
    for (genre, totalPlay) in genreSort:
        d[genre] = sorted(d[genre], key=lambda x: (-x[0], x[1]))
        answer += [ idx for (play, idx) in d[genre][:2] ]
    
    return answer
"""

# Holy Shit!


def solution(genres, plays):
    answer = []
    
    gen_dic = defaultdict(lambda: 0)
    total_list = defaultdict(lambda: [])

    for i in range(len(genres)):
        gen_dic[genres[i]] += plays[i]
        total_list[genres[i]].append((plays[i], i))

    gen_dic = sorted(gen_dic, key=lambda x: x[1], reverse=True)

    for i in total_list:
        total_list[i] = sorted(total_list[i], key=lambda x: x[0], reverse=True)[:2]

    while len(total_list) > 0:
        gere_max = gen_dic.pop(0)
        for t in total_list:
            if t == gere_max[0]:
                if len(total_list[t]) > 1:
                    answer.append(total_list[t][0][1])
                    answer.append(total_list[t][1][1])
                else:
                    answer.append(total_list[t][0][1])
    return answer


temp_gen = ["classic", "pop", "classic", "classic", "pop"]

if __name__ == "__main__":
    print(solution(temp_gen, temp_plays))
