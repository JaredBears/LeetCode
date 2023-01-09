from typing import List
class Solution:
    # For this problem we need to determine the starting location where a car can travel around the circuit
    # once.  We can do this by iterating through the array.
    # First, initialize a variable to keep track of the current gas and total gas.  Initialize a variable to
    # keep track of the starting location. At first, this will be 0 for all variables.
    # We can then iterate through the array.  We can calculate the delta of the current station by subtracting
    # the cost from the gas.  We can then add the delta to the current gas and the total gas.  If the current
    # gas is less than 0, we reset the current gas to 0 and set the starting location to the next station.
    # If the total gas is less than 0, we will not be able to complete the circuit.  We can then return -1.
    # If the total gas is greater than or equal to 0, we can return the starting location.
    # Time Complexity: O(n) where n is the length of the array
    # Space Complexity: O(1)
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        curr = total = start = 0
        for i in range(N):
            delta = gas[i] - cost[i]
            curr += delta
            total += delta
            if curr < 0:
                curr = 0
                start = i+1
        return -1 if total < 0 else start