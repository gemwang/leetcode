"""
Python的标准库 heapq：从小从大排序的 heap。 heap[0] 就是 smallest。 
0) heapify
1）push 
2) pop

"""


class KthLargest:

    def __inti__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heaqpfiy(nums)
        while len(leap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            heapq.heappushpop(self.heap, val)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


"""
bitset
"""
