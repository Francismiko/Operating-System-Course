class FIFOPageReplacement:
    def __init__(self, capacity):
        self.capacity = capacity
        self.page_queue = []

    def process_page(self, page):
        if page in self.page_queue:
            print(f"Page {page} is already in memory.")
        else:
            if len(self.page_queue) >= self.capacity:
                removed_page = self.page_queue.pop(0)
                print(f"Page {removed_page} is replaced with {page}.")
            self.page_queue.append(page)
            print(f"Page {page} is added to memory.")

        print(f"Current page queue: {self.page_queue}")


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.page_queue = []

    def process_page(self, page):
        if page in self.page_queue:
            self.page_queue.remove(page)
        elif len(self.page_queue) >= self.capacity:
            removed_page = self.page_queue.pop(0)
            print(f"Page {removed_page} is replaced with {page}.")

        self.page_queue.append(page)
        print(f"Page {page} is added to memory.")

        print(f"Current page queue: {self.page_queue}")


# 示例用法
fifo = FIFOPageReplacement(3)  # 设置FIFO内存容量为3
lru = LRUCache(3)  # 设置LRU内存容量为3

# 页面序列
page_sequence = [1, 2, 3, 4, 5, 2, 1, 6, 4]

print("FIFO Page Replacement Algorithm:")
[fifo.process_page(page) for page in page_sequence]

print("\nLRU Page Replacement Algorithm:")
[lru.process_page(page) for page in page_sequence]
