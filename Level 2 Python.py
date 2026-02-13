#Level 2: Lists (indexing, scanning)

#Find max in a list

#Input: nums

#Output: max value (don’t use max())
def FindMax(nums):
    if not nums:
        return None  # Handle empty list case
    max_value = nums[0]
    for num in nums:
        if num > max_value:
            max_value = num
    return max_value    

print(FindMax([122222222222222222222222, 2, 3, 4, 5, 38735295, 35987239857, 38957893275, -1]))
print(FindMax([-10, -5, -3, -1, 0, 1, 2, 3]))

######################################################################################################
#Reverse a list
#Input: list
#Output: reversed list (first without slicing, later with slicing)
def ReverseList(lst):
    reversed_lst = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

print(ReverseList([1, 2, 3, 4, 5]))

def ReverseListSlicing(lst):
    return lst[::-1]
print(ReverseListSlicing([1, 2, 3, 4, 5]))

#Count occurrences
#Input: list nums, value x
#Output: how many times x appears
def CountOccurrences(nums, x):
    count = 0
    for num in nums:
        if num == x:
            count += 1
    return count
print(CountOccurrences([1, 2, 3, 2, 4, 2, 5, 8], 2))
print(CountOccurrences([1, 2, 3, 4, 5,6], 6)) 

#Second largest
#Input: list of integers
#Output: second largest distinct value
def SecondLargest(nums):
    if len(nums) < 2:
        return None  # Not enough elements for second largest
    first = second = float('-inf')
    for num in nums:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None
print('Second largest Number in list : ' + str(SecondLargest([1, 2, 3, 4, 5])))
print('Second largest Number in list : ' + str(SecondLargest([5, 5, 4, 4, 3, 2, 1])))
print('Second largest Number in list : ' + str(SecondLargest([1, 1, 1, 1])))          # Should return None since there's no second largest distinct value
