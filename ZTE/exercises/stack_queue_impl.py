class MyStackArr:
    def __init__(self):
        self.value = []

    def lookup(self, val=None):
        if val:
            for idx, a in enumerate(self.value):
                if val == a:
                    return idx
        else:
            print("Check searched value")

    def push(self, val):
        if val:
            self.value.append(val)

    def pop(self):
        return self.value.pop()

    def peek(self):
        if len(self.value) > 0:
            return self.value[-1]
        else:
            return None


class ListNode:
    def __init__(self, val = None):
        self.val = val
        self.next = ''
        self.prev = ''

class MyStackLinked:
    def __init__(self):
        self.curNode = ListNode()

    def lookup(self, a=None):
        if a:
            pos = 0
            x = self.curNode
            while x.val:
                if x.val == a:
                    print('Value Matched')
                    return pos
                else:
                    x = self.curNode.next
                    pos += 1
        else:
            print("Check searched value")

    def push(self, v):
        if v:
            if not self.curNode.val:
                self.curNode.val = v
            else:
                n = ListNode(v)
                n.prev = self.curNode
                self.curNode.next = n
                self.curNode = n

    def pop(self):
        if not self.curNode.prev:
            print("No Previous Node")
        else:
            n = self.curNode.prev
            p = self.curNode
            n.next = ''
            self.curNode = n
            return p.val

    def peek(self):
        return self.curNode.val if self.curNode.val else None

class myQueueArr:
    def __init__(self):
        self.value = []

    def lookup(self, val=None):
        if val:
            for idx, a in enumerate(self.value):
                if val == a:
                    return idx
        else:
            print("Check searched value")

    def push(self, val):
        if val:
            self.value.append(val)

    def pop(self):
        return self.value.pop(0)

    def peek(self):
        return None if len(self.value) <= 0 else self.value[0]


class myQueueLL:
    def __init__(self, val = None):
        self.curNode = ListNode(val)
        self.next = ''
        self.prev = ''

    def lookup(self, a):
        if a:
            while self.curNode.val:
                if val == a:
                    return idx
        else:
            print("Check searched value")

    def push(self, val):
        if val:
            self.value.append(val)

    def pop(self):
        return self.value.pop(0)

    def peek(self):
        return None if len(self.value) <= 0 else self.value[0]


if __name__ == "__main__":
    ms = MyStackArr()
    print(ms.peek())
    ms.push(10)
    print(ms.peek())
    ms.push(20)
    print(ms.peek())
    print("Popped: ", ms.pop())
    print(ms.peek())
    ms.push(10)
    print(ms.peek())
    ms.push(30)
    print(ms.peek())
    print(ms.lookup(30))

    # ml = MyStackLinked()
    # ml.push(10)
    # print(ml.peek())
    # ml.push(20)
    # print(ml.peek())
    # print("Popped: ", ml.pop())
    # print(ml.peek())
    # ml.push(20)
    # print(ml.peek())
    # ml.push(30)
    # print(ml.peek())
    # ml.lookup(30)
    # print("Popped: ", ml.pop())
    # print(ml.peek())

    # mq = myQueueArr()
    # mq.push(10)
    # print(mq.peek())
    # mq.push(20)
    # print(mq.peek())
    # print("Popped: ", mq.pop())
    # print(mq.peek())
    # mq.push(20)
    # print(mq.peek())
    # mq.push(30)
    # print(mq.peek())
    # print(mq.lookup(30))
    # print("Popped: ", mq.pop())
    # print(mq.peek())
    # print("Popped: ", mq.pop())
    # print(mq.peek())
    # print("Popped: ", mq.pop())
    # print(mq.peek())

    # mq = myQueueArr()
    # mq.push(10)
    # print(mq.peek())
    # mq.push(20)
    # print(mq.peek())
    # print("Popped: ", mq.pop())
    # print(mq.peek())
    # mq.push(20)
    # print(mq.peek())
    # mq.push(30)
    # print(mq.peek())
    # print(mq.lookup(30))
    # print("Popped: ", mq.pop())
    # print(mq.peek())
    # print("Popped: ", mq.pop())
    # print(mq.peek())
    # print("Popped: ", mq.pop())
    # print(mq.peek())

