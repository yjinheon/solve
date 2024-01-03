from random import randint
import time


# decorator 를 활용한 실행시간 측정
def check_time(func):
    def wrapper_fn(*args,**kwargs):
        start_time = time.time()
        func_result = func(*args,**kwargs)
        print(f"Processing time is {(time.time()-start_time):.2f}")
        return func_result
    return wrapper_fn


def main():
    print("start")


if __name__ == "__main__":
    main()
