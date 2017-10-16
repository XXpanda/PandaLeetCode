class Heap(object):
    def __init__(self):
        self.DEFAULT_CAPACITY = 10
        self.current_size = 0
        self.array = [None] * 10

    def enlarge_array(self, length):
        temp_array = [None] * length
        i = 1
        while i < len(self.array):
            temp_array[i] = self.array[i]
            i += 1
        self.array = temp_array

    def percolate_down(self, hole):
        tmp = self.array[hole]
        while hole * 2 <= self.current_size:
            child = hole * 2
            if child != self.current_size and self.array[child + 1] < self.array[child]:
                child += 1
            if self.array[child] < tmp:
                self.array[hole] = self.array[child]
            else:
                break
            hole = child
        self.array[hole] = tmp

    def insert(self, x):
        if self.current_size == len(self.array) - 1:
            self.enlarge_array(len(self.array) * 2 + 1)
        self.current_size += 1
        # percolate up
        hole = self.current_size
        if hole == 1:
            self.array[hole] = x
            return
        self.array[0] = x
        while x < self.array[hole/2]:
            self.array[hole] = self.array[hole/2]
            hole /= 2
        self.array[hole] = x

    def build(self, new_array):
        self.current_size = len(new_array)
        self.array = [None] * ((self.current_size + 2) * 11 / 10)
        i = 1
        for new_item in new_array:
            self.array[i] = new_item
            i += 1
        j = self.current_size / 2
        while j > 0:
            self.percolate_down(j)
            j -= 1

    def delete_min(self):
        if self.current_size == 0:
            return
        min_item = self.array[1]
        self.array[1] = self.array[self.current_size]
        self.array[self.current_size] = None
        self.current_size -= 1
        self.percolate_down(1)
        return min_item

    def heap_sort(self, in_array):
        self.build(in_array)
        i = self.current_size
        while i >= 1:
            self.swap(self.array, 1, i)
            self.current_size -= 1
            self.percolate_down(1)
            i -= 1

    def swap(self, in_array, i, j):
        temp = in_array[i]
        in_array[i] = in_array[j]
        in_array[j] = temp


if __name__ == '__main__':
    heap = Heap()
    test_array = [13, 21, 16, 19, 68, 24, 31, 65, 26, 32]
    # for item in test_array:
    #     heap.insert(item)
    # print heap.array
    # heap.build(test_array)
    # print heap.array
    # print heap.delete_min()
    # print heap.array
    heap.heap_sort(test_array)
    print heap.array
