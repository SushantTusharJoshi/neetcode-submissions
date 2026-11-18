class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:                  # stop at one number left
            mid = (l + r) // 2
            if nums[mid] > nums[r]:   # mid is on the high stair → the cut is to the right
                l = mid + 1
            else:                     # mid might be the cut → keep it
                r = mid
        pivot = l

        if nums[pivot] <= target <= nums[-1]:
            l, r = pivot, len(nums) - 1
        else:
            l, r = 0, pivot - 1

    # Step 3: plain binary search (704)
        while l <= r:                     # throws mid out → run until the window is empty
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1                     