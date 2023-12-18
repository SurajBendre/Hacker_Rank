# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
l = int(input())
s = input().split()
r = int(input())
count = 0
lis = [i for i in list(combinations(s,r))]
for i in lis:
    if 'a' in i: count+=1
print(count/len(lis))


'''
The itertools module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination. Together, they form an iterator algebra making it possible to construct specialized tools succinctly and efficiently in pure Python.

To read more about the functions in this module, check out their documentation here.

You are given a list of  lowercase English letters. For a given integer , you can select any  indices (assume -based indexing) with a uniform probability from the list.

Find the probability that at least one of the  indices selected will contain the letter: ''.

Input Format

The input consists of three lines. The first line contains the integer , denoting the length of the list. The next line consists of  space-separated lowercase English letters, denoting the elements of the list.

The third and the last line of input contains the integer , denoting the number of indices to be selected.

Output Format

Output a single line consisting of the probability that at least one of the  indices selected contains the letter:''.

Note: The answer must be correct up to 3 decimal places.

Constraints



All the letters in the list are lowercase English letters.

Sample Input

4 
a a c d
2
Sample Output

0.8333
Explanation

All possible unordered tuples of length  comprising of indices from  to  are:


Out of these  combinations,  of them contain either index  or index  which are the indices that contain the letter ''.

Hence, the answer is .

Language
Python 3
More
1234567891011
print(count/len(lis))

Line: 11 Col: 1

Test against custom input
Congratulations
You solved this challenge. Would you like to challenge your friends?Share on FacebookShare on TwitterShare on LinkedIn

Test case 0

Test case 1

Test case 2

Test case 3

Test case 4

Test case 5

Test case 6

Test case 7

Test case 8

Test case 9

Test case 10

Test case 11
Compiler Message
Success
Input (stdin)
4
a a c d
2
Expected Output
0.833333333333
BlogScoring
'''