class myBinNode:
    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.left = None
        self.right = None


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


def insert(bt, v):
    if not bt:
        return myBinNode(v)
    elif v < bt.val:
        bt.left = insert(bt.left, v)
        return bt
    elif v >= bt.val:
        bt.right = insert(bt.right, v)
        return bt
    else:
        print("error")

def lookup(bt, v):
    """using stacks"""
    st = MyStackArr()
    st.push(bt)
    while len(st.value) > 0:
        cur = st.pop()
        print(cur.val)
        if cur.val == v:
            print(f"Found value {cur.val} required {v}")
            return True
        if cur.left:
            st.push(cur.left)
        if cur.right:
            st.push(cur.right)
    return false

def qlookup(bt, v):
    st = myQueueArr()
    st.push(bt)
    if not bt:
        return False
    while len(st.value) > 0:
        cur = st.pop()
        print(cur.val)
        if cur.val == v:
            print(f"Found value {cur.val} required {v}")
            return True
        if cur.right:
            st.push(cur.right)
        if cur.left:
            st.push(cur.left)
    return False

def print2DTree(root, space=0, LEVEL_SPACE = 5):
    if (root == None): return
    space += LEVEL_SPACE
    print2DTree(root.right, space)
    # print() # neighbor space
    for i in range(LEVEL_SPACE, space): print(end = " ")
    print("|" + str(root.val) + "|<")
    print2DTree(root.left, space)

if __name__ == "__main__":
    bt = myBinNode(7)
    insert(bt, 9)
    insert(bt, 5)
    insert(bt, 3)
    insert(bt, 6)
    insert(bt, 1)
    insert(bt, 2)
    insert(bt, 12)
    insert(bt, 121)
    insert(bt, 11)
    print2DTree(bt)
    qlookup(bt,121)
    lookup(bt,1)