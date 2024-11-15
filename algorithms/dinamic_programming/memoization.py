# 메모이재이션 적용한 경우

memo = {}

def recursive_factorial(n):
    if n == 0 :
        return 1
    elif n in memo:
        return memo[n] # memoizaiton
    else:
        result = n * recursive_factorial(n-1)
        memo[n] = result
        return result

# case 1 

if __name__ == "__main__":
    print(f"recursive_factorial(5) : {recursive_factorial(5)}, memo : {memo}")
    print(f"recursive_factorial(4) : {recursive_factorial(4)}, memo : {memo}")
    print("동일한 계산에 대해 memo[n]에 저장된 값을 재사용한다.")
        

    
