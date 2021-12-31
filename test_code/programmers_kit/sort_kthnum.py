ex = [1,5,2,6,3,7,4]



commands = [[2,5,3],[4,4,1],[1,7,3]]

def kthnum(array,commands):
    answer = []
    
    for i in commands:
        temp=array[i[0]-1:i[1]]
        temp= sorted(temp)
        answer.append(temp[i[2]-1])
        
    return answer


# lambda와 map을 활용한 풀이


def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))



if __name__ == "__main__":
    print(kthnum(ex,commands))
    print(ex[1:3])