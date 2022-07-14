from collections import Counter

class Solution:
    def sortString(self, s: str) -> str:

        # Count characters and sort them alphabetically
        counts = sorted(Counter(s).items())

        # Initialize the result
        res = []

        # Keep track of if we want to go forward or backward
        reverse = False

        # Iterate until we used all character
        while len(res) != len(s):

            # Iterate through chracters in counts
            for i in range(len(counts)):

                # If reserve==False, i: 0,1,2,3,...
                # If reserve==True, i: -1,-2,-3,...
                i = -i - 1 if reverse else i

                # Get a character and its count
                char, count = counts[i]

                # If its count is 0, skip it
                if count == 0:
                    continue

                # Else, append the char to the result
                res.append(char)

                # Update the character count
                counts[i] = (char, count - 1)

            # Update iterative direction
            reverse = not reverse

        return "".join(res)