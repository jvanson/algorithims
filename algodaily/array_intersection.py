# Can you write a function that takes two arrays as inputs and returns
# their intersection? We can call the method intersection.
# Let 's return the intersection of the two inputs in the
# form of an array. As a reminder, the definition of an intersection of
# two sets A and B is the set containing all elements of A that also belong
# (or equivalently, all elements of B that also belong to A).
#
# const nums1 = [1, 2, 2, 1];
# const nums2 = [2, 2];
#
# intersection(nums1, nums2);
# // [2]
# And here's another one:
#
# const nums1 = [4,9,5];
# const nums2 = [9,4,9,8,4];
#
# intersection(nums1, nums2);
# // [9, 4]

nums1 = [1, 2, 2, 1]
nums2 = [2,2]

store_array = []
for num1 in nums1:
    if num1 in nums2:
        if num1 not in store_array:
            store_array.append(num1)

print(store_array)