def memoize_factorial(f):
    memory = {}

    def save_memory(num):
        if num not in memory:
            memory[num] = f(num)

        return memory[num]

    return save_memory

@memoize_factorial # 함수를 인자로 받아 memoize_factorial함수 실행
def facto(num):
    if num == 1:
        return 1
    return num * facto(num-1)



if __name__ == "__main__":
    num = 4
    print(facto(num))
