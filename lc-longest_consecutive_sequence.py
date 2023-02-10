"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time - makes things hard
"""

class OptimalSolution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        (Visualize on the line how I solve the problem && spot the patters)
        
        How to identify what makes a sequence? How to start at the beginning of the sequence?
        Observation: the sequence start does NOT have the left neighbour, there does not exist element (n-1) --> n - start

        Idea: 1) identify the start of each sequence based on the observation
              2) Calc the length of each sequence (increment n + 1 and check whether it exists)
              3) Choose the max length sequence
              Prior to doing this - convert list(nums) to set(nums) so that constant element search in steps 1. and 2. 

        Time - O(n)
        Space - O(n)
        """
        
        # Avoid cases with repetitions, as they do not impact longest consecutive sequence
        # Lookup - contant O(1)
        unique_nums = set(nums)

        longest_seq_length = 0

        for num in unique_nums:

            # Is {num} start of sequence? --> yes, if no left neighbour exist 
            if (num - 1) not in unique_nums:
                curr_seq_length = 1

                # get the length of the sequence starting with {num}
                i = 1
                while (num + i) in unique_nums:
                    curr_seq_length += 1
                    i += 1
                
                # check with max seq length
                longest_seq_length = max(curr_seq_length, longest_seq_length)
        
        return longest_seq_length


class BruteForceSolution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Idea: 1) Sort nums 2) Iterate over sorted nums and find longest consecutive sequence

        Tricky part: [0,1,1,2] --> 3, if equal - keep consecutive sequence but do not increment count
        
        Time: O(nlog(n))
        Space: O(1)
        """

        # Edge case - empty list
        if not nums: return 0
        
        # O(nlog(n))
        nums.sort()

        # O(n)
        longest_consecutive_seq = 1
        curr_consecutive_seq = 1

        i = 0
        while i < len(nums)-1:
            
            # Calc the length of consecutive sequence
            j = i + 1
            
            while j<len(nums) and ((nums[j] == nums[i] + 1) or (nums[j] == nums[i])):
                # increment count iff consecutive elements
                if nums[j] == nums[i] + 1:
                    curr_consecutive_seq += 1
                i = j
                j += 1
            
            if curr_consecutive_seq > longest_consecutive_seq:
                longest_consecutive_seq = curr_consecutive_seq
            
            curr_consecutive_seq = 1
            i = j
        

        return longest_consecutive_seq


