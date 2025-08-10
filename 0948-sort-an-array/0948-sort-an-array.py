class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    def quickSort(self, arr: list[int], low: int, high: int):
        if low >= high:
            return

        start = low
        end = high
        pivot = arr[low + (high - low) // 2]  # A more robust way to find the middle index

        while start <= end:
            while arr[start] < pivot:
                start += 1
            while arr[end] > pivot:
                end -= 1

            if start <= end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        self.quickSort(arr, low, end)
        self.quickSort(arr, start, high)
