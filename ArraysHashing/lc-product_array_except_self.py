"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Hard Constraints: You must write an algorithm that runs in O(n) time and without using the division operation.
"""

class OptimalSolution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Idea: two-pass (-->, <--) over nums list && record the product elements before (-->) and after (<--) element at index i.
        Use two lists to keep info of product before (and after) element at index i

        Product of array except self = (product elements before self) * (product elements after self)

        Time - O(n)
        Space - O(n)

        To avoid using space - save productLeft in {answer} (1st pass) and then just * with productRight during 2nd pass.
        Do not use additional arrays but directly save intermediate (and final) results in answer 
        """
        
        answer = [None] * len(nums)

        productLeft = [None] * len(nums)  # at index - product elements before nums[index]
        productRight = [None] * len(nums) # at index - product elements after nums[index]
		
        product_left = 1
        for ind in range(len(nums)):
            productLeft[ind] = product_left
            product_left *= nums[ind]
        
        product_right = 1
        for ind in range(len(nums)-1, -1, -1):
            productRight[ind] = product_right
            product_right *= nums[ind]
        
        for i in range(len(answer)):
            answer[i] = productLeft[i] * productRight[i]

        return answer


class BruteForceSolution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    	"""
    	Brute Forse Solution: for each element at position pos, keep track of the elements product before pos
    	and calculate the product of elements after pos.
    	Time - O(n**2)
    	n - len(nums)
    	"""
        
        answer = [None] * len(nums)
        
        productBeforePos = 1

        for pos in range(len(nums)):
            
            productNextPos = 1
            for pos_next in range(pos+1, len(nums)):
                productNextPos *= nums[pos_next]

            answer[pos] = productBeforePos * productNextPos

            productBeforePos *= nums[pos]

        return answer


