import sys


class MaxHeap:

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = sys.maxsize
        self.Front = 1


    def parent(self, pos):
        return pos // 2


    def leftChild(self, pos):
        return 2 * pos


    def rightChild(self, pos):
        return (2 * pos) + 1


    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]


    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Head[self.size] = element

        current = self.size

        while self.Heap[current] > self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def isLeaf(self, pos):
        if 2 * pos >= self.size and pos <= self.size:
            return True
        return False

    def extractMax(self):
        popped = self.Heap[self.Front]
        self.Heap[self.Front] = self.Heap[self.size]
        self.size -= 1
        self.maxHeapify(self.Front)
        return popped

    def maxHeapify(self, pos):
        if not self.isLeaf(pos):
            if self.Heap[self.leftChild(pos)] > self.Heap[pos] or \
                         self.Heap[self.rightChild(pos)] > self.Heap[pos]:

                if self.Heap[self.leftChild(pos)] > self.Heap[self.rightChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.maxHeapify(self.leftChild(pos))

                else:
                    self.swap(pos, self.rightChild(pos))
                    self.maxHeapify(self.rightChild(pos))
