# User function template for Python3
class Solution:
    def findTriplets(self, arr):
        # Initialize the length of the input array
        n = len(arr)
        
        # Use a set to store unique triplets, avoiding duplicates
        temp = set()
        
        # Dictionary to store pairs of numbers and their indices in the array,
        # where the key is the sum of the pair and the value is a list of tuples
        # containing index pairs (i, j) such that arr[i] + arr[j] = sum
        hash = dict()
        
        # Populate the hash dictionary with all unique pairs and their sums
        for i in range(n):
            for j in range(i + 1, n):
                # Calculate the sum of the current pair (arr[i], arr[j])
                vis = arr[i] + arr[j]
                
                # If this sum is not already a key in the hash, initialize it with an empty list
                if vis not in hash:
                    hash[vis] = list()
                
                # Add the current pair (i, j) to the list for this sum
                hash[vis].append((i, j))
        
        # Iterate through the array to find a third element that complements the pairs
        for i in range(n):
            # Calculate the value needed to form a triplet that sums to zero
            more = -arr[i]
            
            # Check if this complementary value is in the hash dictionary
            if more in hash:
                # If it exists, iterate through each pair of indices that sum to 'more'
                for idx in hash[more]:
                    # Ensure that the indices are distinct (no repeated indices in the triplet)
                    if idx[0] != i and idx[1] != i:
                        # Sort the triplet indices to maintain consistency and avoid duplicate triplets
                        triplet = sorted([i, idx[0], idx[1]])
                        
                        # Add the triplet as a tuple to the set to prevent duplicates
                        temp.add(tuple(triplet))
        
        # Convert each tuple in the set to a list and return the result
        return [list(x) for x in temp]
