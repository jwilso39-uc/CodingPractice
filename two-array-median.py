def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    #exchange lists if nums2 had less elements
    if len(nums2) < len(nums1):
        nums1, nums2 = nums2, nums1
    #calculate midpoint of two arrays
    n = len(nums1)
    m = len(nums2)
    half = (n + m) // 2
    #binary search to find how many elements in nums1 are part of the left partition
    left = 0
    right = n
    while left <= right:
        if left > n or right < 0:
            break
        mid = left + (right - left) // 2
        #ensure maximum elements are larger than both minimum elements
        if mid == 0:
            min1 = None
        else:
            min1 = nums1[mid-1]
        if half-mid == 0:
            min2 = None
        else:
            min2 = nums2[half-mid-1]
        if mid == len(nums1):
            max1 = None
        else:
            max1 = nums1[mid]
        if half - mid == len(nums2):
            max2 = None
        else:
            max2 = nums2[half - mid]
        #valid partition
        if (min1 is None or max2 is None or min1 <= max2) and (min2 is None or max1 is None or min2 <= max1):
            valid_mid = mid
            right = mid - 1
        else:
            left = mid + 1
    #figure out how to calculate median based on total length of both arrays
    totlen = (m + n)
    if valid_mid == len(nums1):
        min1 = 1000001
    else:
        min1 = nums1[valid_mid]
    if half - valid_mid == len(nums2):
        min2 = 1000001
    else:
        min2 = nums2[half - valid_mid]
    if half - valid_mid == 0:
        max2 = -1000001
    else:
        max2 = nums2[half-valid_mid-1]
    if valid_mid == 0:
        max1 = -1000001
    else:
        max1 = nums1[valid_mid-1]
    #calculate median and return
    if totlen % 2 == 0:
        return (max(max1, max2) + min(min1, min2)) / 2
    else:
        return min(min1, min2)
        
print(findMedianSortedArrays([0,0], [0,0]))