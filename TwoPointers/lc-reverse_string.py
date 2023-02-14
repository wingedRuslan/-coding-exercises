class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Two-pointer technique - start --> , <-- end, swap elements at start and end. 

        Time - O(n)
        Space - O(1)
        """

        # Iterate the array from two ends to the middle.
        i = 0
        j = len(s) - 1

        while i < j:
            # Swap elements at two pointers
            s[i], s[j] = s[j], s[i]
            
            i += 1
            j -= 1

        return s

