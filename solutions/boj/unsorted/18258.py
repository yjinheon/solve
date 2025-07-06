

class MyQueue:
    def __init__(self):
        self._qlist = []


    def  is_empty(self) -> bool:
        return len(self._qlist) == 0


    def push(self, x: int) -> None:
        self._qlist.append(x)
        print(self._qlist)


    def pop(self) -> int:
        return self._qlist.pop(0) 




if __name__ == '__main__':
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    obj.push(4)
    obj.push(5)
    print(obj.pop())

