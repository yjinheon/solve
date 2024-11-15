def memo_fib(input_value, save_memo):
    save_memo[1],save_memo[2] = 1,1
    for i in range(3,input_value+1):
        save_memo[i] = save_memo[i-1]+save_memo[i-2]
    return save_memo[input_value]


if __name__ == "__main__":
    save_memo = {}
    print(memo_fib(33, save_memo))

