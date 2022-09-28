from collections import deque


class Queue:
    def __init__(self):
        self.seq = deque()

    def push(self, item):
        self.seq.appendleft(item)

    def retrieve(self):
        return self.seq.pop()

    def length(self):
        return len(self.seq)

    def is_empty(self):
        return len(self.seq) == 0


if __name__ == '__main__':
    stack = Queue()
    stack.push('one')
    stack.push('two')
    stack.push('three')
    print(stack.seq)
    print(stack.retrieve())
    print(stack.seq)
