class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        end = len(nums) - 1
        while end > 0 and nums[end] == nums[0]:
            end -= 1
        
        l,r = 0, end
        while l < r:
            mid = (r + l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        pivot = l
        
        if nums[pivot] <= target <= nums[end]:
            l,r = pivot, end
        else:
            l,r = 0, pivot - 1
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False