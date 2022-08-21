# Median of two Sorted Arrays

Given two already sorted arrays of integers,
find the median of all the values.

**Example 1**

if a = [1, 3] and b = [2], then the median is 2

**Example 2**

if a = [1, 3] and b [2, 4], then the median is 2.5

## Solution 1 - O(n+m)

The first solution is the simplests, but also the most
inefficient. It consists of merge the two already sorted
arrays into a single one and then find the median.
As merge two sorted arrays can be done in O(n+m), where 
n and m are the length of the respective arrays, then
the total time to find the median is O(n+m).