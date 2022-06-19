#  File: DNA.py

#  Description: Write an algorithim that prints out the longest common sequence(s) for the two strings in alphabetical order. 

#  Student Name: Neha Kondaveeti

#  Student UT EID: nk8975

#  Partner Name: Salomone Martinez

#  Partner UT EID: sm72364

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 01/22

#  Date Last Modified: 01/22

import sys

# Input: string s
# Output: returns a list of all substrings of s
def all_substrs(s):
    # create a list to store the substrings
    substrs = []

    # get the size of the window
    wnd = len(s)

    # find all substrings
    while (wnd >0):
        start_idx = 0
        while ((start_idx + wnd) <= len(s)):
            sub_string = s[start_idx:start_idx + wnd]
            substrs.append(sub_string)
            start_idx += 1
        wnd = wnd -1
    return substrs

# Input: s1 and s2 are two strings that represent strands of DNA
# Output: returns a sorted list of substrings that are the longest 
# common subsequence. The list is empty if there are no common subsequences.

def longest_subsequence (s1, s2):
    sequences = []

    for x in s1:
        if x in s2:
            sequences.append(x)

    lg_sequences = []
    for y in sequences:
        if len(sequences[0]) == len(y):
            lg_sequences.append(y)

    copyoflist = lg_sequences.copy()
    aset = set()
    for z in copyoflist:
        aset.add(z)

    finallist = []
    for n in aset:
        finallist.append(n)


    return sorted(finallist)
    


def main():
    # read the number of pairs
    num_pairs = sys.stdin.readline()
    num_pairs = num_pairs.strip()
    num_pairs = int(num_pairs)

  # for each pair call longest_subsequence
    for i in range (num_pairs):
        st1 = sys.stdin.readline()
        st2 = sys.stdin.readline()

        st1 = st1.strip()
        st2 = st2.strip()

        st1 = st1.upper()
        st2 = st2.upper()

        # write out result(s)

        if len(longest_subsequence(all_substrs(st1),all_substrs(st2))) == 0:
            print("No Common Sequence Found")
        else:
            for y in longest_subsequence(all_substrs(st1),all_substrs(st2)):
                print(y)
            print("")

if __name__ == "__main__":
    main()
  