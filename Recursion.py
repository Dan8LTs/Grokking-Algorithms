# 4.1
nums = [12, 32, 6, 8]
def list_sum(nums):
    if nums == []:
        return 0
    else:
        return nums[0] + list_sum(nums[1:])
print(list_sum(nums))

# 4.2
def list_count(nums):
    if nums == []:
        return 0
    else:
        return 1 + list_count(nums[1:])
print(list_count(nums))

# 4.3
def list_max(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return max(nums[0], list_max(nums[1:]))
print(list_max(nums))

def quick_sort(nums):
    if len(nums) < 2:
        return nums
    else:
        base_element = nums[len(nums) // 2]
        less = [i for i in nums[0:len(nums) // 2] + nums[len(nums) // 2 + 1:] if i <= base_element]
        bigger = [i for i in nums[0:len(nums) // 2] + nums[len(nums) // 2 + 1:] if i > base_element]
        return quick_sort(less) + [base_element] + quick_sort(bigger)
print(quick_sort(nums))

