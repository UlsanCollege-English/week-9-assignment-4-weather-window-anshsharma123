import heapq

def sliding_window_max(nums, k):
    """
    Return a list of the maximums for each sliding window of size k.
    Uses a max-heap implemented via (-value, index) and lazy deletion.
    """
    if not nums or k <= 0:
        return []
    
    n = len(nums)
    if k >= n:
        return [max(nums)]

    heap = []
    result = []

    for i in range(n):
        # Push current element with negative value to simulate max-heap
        heapq.heappush(heap, (-nums[i], i))

        # Remove elements outside the current window
        while heap[0][1] <= i - k:
            heapq.heappop(heap)

        # Record max for windows that have fully formed
        if i >= k - 1:
            result.append(-heap[0][0])

    return result
