def median(nums1, nums2):
    
    if nums1[-1] > nums2[-1]:
        large = nums1
        small = nums2
    else:
        large = nums2
        small = nums1
    l = len(large)
    s = len(small)

    