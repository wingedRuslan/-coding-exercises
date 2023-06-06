class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        Merge Sort ~ Divide & Conquer

        mergeSort(array)
        - mergeSort(array left half)
        - mergeSort(array right half)
        - merge(sorted array left half && sorted array right half)

        Time: O(n logn)
        Space: O(n) - merging n/2 and n/2 halves together
        """

        # Base Case
        if len(nums) == 1:
            return nums
        
        # Calc the middle of the (sub)array
        mid = len(nums) // 2

        # Divide into halves until base case reached
        left_half = self.sortArray(nums[0:mid])
        right_half = self.sortArray(nums[mid:])  
        
        # Merge the left and right parts
        nums = self.merge(left_half, right_half)
        
        return nums
        
    def merge(self, left: List[int], right: List[int]) -> List[int]:
        
        # Temp array to return 
        sorted_arr = [0] * (len(left) + len(right))

        # Set pointers for each array to compare elements of each array
        left_p = 0
        right_p = 0

        # Keep track of index to put elements to <result> array
        index = 0

        # Insert the elements in ascending order into the final array 
        while left_p < len(left) and right_p < len(right):
            if left[left_p] <= right[right_p]:
                sorted_arr[index] = left[left_p]
                left_p += 1
            else:
                sorted_arr[index] = right[right_p]
                right_p += 1
            index += 1

        # if we reached the end of one array
        # iterate over the other array and insert each element into the final array
        while left_p < len(left):
            sorted_arr[index] = left[left_p]
            left_p += 1
            index += 1
        
        while right_p < len(right):
            sorted_arr[index] = right[right_p]
            right_p += 1
            index += 1
        
        return sorted_arr


##########
# Divide and Merge by reference and Two Pointers
# --> Save some memory rather than copying some parts of the input array
##########

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergeSort(arr, l, r):
            if l == r:
                return arr
            
            m = (l + r) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m + 1, r)
            merge(arr, l, m, r)

            return arr


        def merge(arr, L, M, R):
            left, right = arr[L:M+1], arr[M+1:R+1]
            i, j, k = L, 0, 0    # pointer over arr, left, right
            
            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1
            
            while j < len(left):
                arr[i] = left[j]
                j += 1
                i += 1
            
            while k < len(right):
                arr[i] = right[k]
                k += 1
                i += 1
        
        return mergeSort(nums, 0, len(nums) - 1)

