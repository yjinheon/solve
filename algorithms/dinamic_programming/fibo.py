def memo_fib(input_value, save_memo):
    if input_value == 0:  # 에러케이스를 만들어둬야 한다.
        return 0

    elif input_value == 1:
        return 1

    elif input_value in save_memo:
        return save_memo[input_value]

    else:
        res = memo_fib(input_value - 2, save_memo) + memo_fib(
            input_value - 1, save_memo
        )
        save_memo[input_value] = res
        return res


if __name__ == "__main__":
    save_memo = {}
    print(memo_fib(40, save_memo))
    print("hello world")
