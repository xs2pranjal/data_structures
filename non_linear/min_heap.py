import sys


class MinHeap:
    def __init__(self):
        self.maxsize = sys.maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = sys.maxsize
        self.FRONT = 1

    def leftChild(self, pos):
        return 2 * pos

    def isLeaf(self, pos):
        if 2 * pos >= self.size and pos <= self.size:
            return True
        return False

    def rightChild(self, pos):
        return (2 * pos) + 1

    def parent(self, pos):
        return pos // 2

    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1

        current = self.size
        self.Heap[current] = element

        while self.Heap[current] < self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def extractMin(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1

        self.minHeapify(self.FRONT)
        return popped

    def minHeapify(self, pos):
        if not self.isLeaf(pos):
            if self.Heap[self.leftChild(pos)] < self.Heap[pos] or self.Heap[self.rightChild(pos)] < self.Heap[pos]:
                if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))
                else:
                    self.swap(self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))
