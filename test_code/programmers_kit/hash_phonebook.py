import collections

def solution(phone_book):
    phone_book = sorted(phone_book)

    temp = [i[:2] for i in phone_book]

    temp_count = collections.Counter(temp)

    if any(v > 1 for v in temp_count.values()):
        answer = False
    else:
        answer = True
    
    return answer


# 이게 훨씬 깔끔하다.
def solution2(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True



ex=["119", "97674223", "1195524421"]


if __name__ == "__main__":
    print(solution(ex))