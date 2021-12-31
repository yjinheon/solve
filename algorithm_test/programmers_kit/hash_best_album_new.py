# 최종적으로 이게 남음

from collections import defaultdict

temp_gen = ["classic", "pop", "classic", "classic", "pop"]
temp_plays = [500, 600, 150, 800, 2500]

def solution(genre,plays):
    res = []
    
    gen_dict = defaultdict(lambda: 0)
    total_dict = defaultdict(list)
    
    for i in range(len(genre)):
        gen_dict[genre[i]] += plays[i]
        total_dict[genre[i]].append((plays[i], i)) # 중요

    sorted_gen = sorted(gen_dict.items(), key=lambda x: x[1], reverse=True)
    
    
    for (genre, total_play) in sorted_gen:
        total_dict[genre] = sorted(total_dict[genre], key=lambda x: (-x[0], x[1])) # 재생수 내림차순, 인덱스 오름차순
        res += [idx for (play, idx) in total_dict[genre][:2] ]        
    
    return res
    
if __name__ == "__main__":
    print(solution(temp_gen, temp_plays))