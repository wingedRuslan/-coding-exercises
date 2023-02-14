"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""


class OptimalSolution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Keep nums frequencies in a hashmap
        !Idea!: introduce 2D auxiliary array, at index i (=freq) keep nums having such freq
        Reverse the 2D array to find Top k most frequent nums
        Time - O(n)
        Space - O(n)
        """

        count = {}  # num : freq
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # main idea - at index i (freq) keep nums having such freq
        frequency = [[] for i in range(len(nums) + 1)]
        for num, freq in count.items():
            frequency[freq].append(num)

        # return Top K nums
        res = []
        for freq in range(len(frequency) - 1, 0, -1):
            for num in frequency[freq]:
                res.append(num)

                if len(res) == k:
                    return res

        return res


class BruteForseSolution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Keep nums frequencies in a hashmap
        Output the K most frequent elements by using auxiliary arrays
        Time: O(n) + O(p)*O(k)
        Space: O(p) + 2*O(k)

        n - len(nums)
        p - number unique elements in nums
        """

        count = {}  # num : freq
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # auxiliary arrays to keep track of Top k most frequent arrays
        frequencyKList = [-1] * k
        numsKList = [-1] * k

        for curr_num, curr_freq in count.items():
            for ind, freq in enumerate(frequencyKList):
                if curr_freq > freq:
                    # "slice" - select less frequent nums than <curr_num>
                    # the least frequent num will be removed
                    less_frequent_nums = numsKList[ind:-1]
                    less_freqs = frequencyKList[ind:-1]

                    numsKList[ind] = curr_num
                    frequencyKList[ind] = curr_freq

                    # shift the rest freqs and nums to the right starting from ind
                    numsKList[ind + 1:] = less_frequent_nums
                    frequencyKList[ind + 1:] = less_freqs

                    break

        return numsKList
