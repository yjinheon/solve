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


if __name__ == "__main__":
    @check_time
    def test_fn():
        for i in range(1000000):
            randint(1,100)
    test_fn()

