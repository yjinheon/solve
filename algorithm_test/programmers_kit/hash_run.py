"""

수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.


import collections

counter를 통해 이름을 key , 수를 value로 하는 dictionary 생성

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

"""


def solution(participant, completion):
    temp = {} # key,value를 가진 딕셔너리 이용
    #딕셔너리에 참가자 이름(key)과 해당 이름 사람수(value) 넣기 
    for i in participant :
        if i in temp : 
            temp[i]+=1
        else: 
            temp[i] =1
  
    #완주자 이름(key)의 value가 1이면 지우기, 동명이인이면 -1  
    for i in completion :
        if temp[i]==1 : 
            del temp[i]
        else : 
            temp[i] -=1

    #딕셔너리를 리스트로 바꾸고 가장 첫번째꺼 리턴(어차피 하나뿐)
    return list(temp.keys())[0]


ex_p = ["leo", "kiki", "eden"]
ex_c = ["leo","kiki"]


if __name__ == "__main__":
	print(solution(ex_p,ex_c))
