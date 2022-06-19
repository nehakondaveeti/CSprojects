#  File: TestCipher.py

#  Description: 

#  Student's Name: Neha Kondaveeti

#  Student's UT EID: nk8975

#  Course Name: CS 313E 

#  Unique Number: 51120

#  Date Created: 02/4

#  Date Last Modified: 02/4

import sys

#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is encoded with
#          rail fence algorithm
def rail_fence_encode ( strng, key ):
    x_positions = []
    y_positions = []

    # gives us each letter's y position
    # all good
    for y in range(len(strng)):
        y_positions.append(y)
    #return y_positions. strng

    # gives us each letter's x position
    min_value = 1 
    max_value = int(key)
    x = min_value
    x_positions.append(x)
    while len(x_positions) < len(strng):
        while x < max_value and len(x_positions) < len(strng):
            x += 1
            x_positions.append(x)
        while x > min_value and len(x_positions) < len(strng):
            x -= 1
            x_positions.append(x)
    #return x_positions

    # create 2-D list strng x key size

    rail_fence_list = []
    for x in range(int(key)):
        row_list = []
        for y in range(len(strng)):
            row_list.append("")
        rail_fence_list.append(row_list)

    for i in range(len(x_positions)):
        # indexing all x_position values
        rail_fence_list[x_positions[i]-1][i] = strng[i]

    astring = ""
    for n in rail_fence_list:
        for s in n:
            if s != "":
                astring = astring + s
    return astring
    

#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is decoded with
#          rail fence algorithm
def rail_fence_decode ( strng, key ):
    x_positions = []

    # 2-d list
    rail_fence_list = []
    for x in range(int(key)):
        row_list = []
        for y in range(len(strng)):
            row_list.append("")
        rail_fence_list.append(row_list)

    #list of x positions
    min_value = 1 
    max_value = int(key)
    x = min_value
    x_positions.append(x)
    while len(x_positions) < len(strng):
        while x < max_value and len(x_positions) < len(strng):
            x += 1
            x_positions.append(x)
        while x > min_value and len(x_positions) < len(strng):
            x -= 1
            x_positions.append(x)
    #return x_positions

    for i in range(len(x_positions)):
        # indexing all x_position values
        rail_fence_list[x_positions[i]-1][i] = "*"
    index = 0
    og_text = ""
    #traverse through list
    for n in range(len(rail_fence_list)):
        for s in range(len(rail_fence_list[n])):
            if rail_fence_list[n][s] == "*":
                rail_fence_list[n][s] = strng[index]
                index += 1

    #return rail_fence_list

    # traverse diag
    og_text = ""
    for i in range(len(x_positions)):
        # indexing all x_position values
        og_text = og_text + rail_fence_list[x_positions[i]-1][i]
    return og_text
            

#  Input: strng is a string of characters
#  Output: function converts all characters to lower case and then
#          removes all digits, punctuation marks, and spaces. It
#          returns a single string with only lower case characters
def filter_string ( strng ):
    strng = strng.lower()
    print(strng)

  # remove other char
    final_string = ""
    for x in strng:
      if ord(x) >= 97 and ord(x) <= 122:
          final_string = final_string + x
    return final_string

#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character encoded using the 
#          Vigenere algorithm. You may not use a 2-D list 
def encode_character (p, s):
    main_lst = []
    # make array of letters
    
    for i in range(26):
        sub_lst = []
        for j in range(26):
            x = 97 + (i + j)%26
            sub_lst.append(chr(x))
        main_lst.append(sub_lst)
    np = ord(p)-97
    ns = ord(s)-97
    
    return main_lst[ord(p)-97][ord(s)-97]
    return main_lst

#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character decoded using the 
#          Vigenere algorithm. You may not use a 2-D list 
def decode_character (p, s):
    main_lst = []
    for i in range(26):
        sub_lst = []
        for j in range(26):
            x = 97 + (i + j)%26
            sub_lst.append(chr(x))
        main_lst.append(sub_lst)
    return chr(97+main_lst[ord(p)-97].index(s))

  	# placeholder for actual return statement

#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is encoded with
#          Vigenere algorithm
def vigenere_encode ( strng, phrase ):
    out_string = ""
    for i in range(len(strng)):
        p = phrase[i%len(phrase)]
        s = strng[i]
        sub_string = encode_character(p,s)
        out_string = out_string + sub_string
    return out_string	# placeholder for the actual return statement

#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is decoded with
#          Vigenere algorithm
def vigenere_decode ( strng, phrase ):
    out_string = ""
    for i in range(len(strng)):
        p = phrase[i%len(phrase)]
        s = strng[i]
        sub_string = decode_character(p,s)
        out_string = out_string + sub_string
    return out_string	# placeholder for the actual return statement

def main():
  # read the plain text from stdin
    plain_text = sys.stdin.readline()
    plain_text = plain_text.strip()

  # read the key from stdin
    key = sys.stdin.readline()
    key = key.strip()

  # encrypt and print the encoded text using rail fence cipher
    print(rail_fence_encode(plain_text,key))

  # read encoded text from stdin
    cipher_text = sys.stdin.readline()
    cipher_text = cipher_text.strip()

  # read the key from stdin
    key_encrypt = sys.stdin.readline()
    key_encrypt = key_encrypt.strip()

  # decrypt and print the plain text using rail fence cipher
    print(rail_fence_decode(cipher_text,key_encrypt))

  # read the plain text from stdin
    plain_text_1 = sys.stdin.readline()
    plain_text_1 = plain_text.strip()

  # read the pass phrase from stdin
    pass_phrase = sys.stdin.readline()
    pass_phrase = pass_phrase.strip()
    #print(encode_character(pass_phrase[0],plain_text_1[0])) 
  # encrypt and print the encoded text using Vigenere cipher
    print(vigenere_encode(plain_text_1,pass_phrase))

  # read the encoded text from stdin
    cipher_text_1 = sys.stdin.readline()
    cipher_text_1 = cipher_text_1.strip()

  # read the pass phrase from stdin
    pass_phrase_1 = sys.stdin.readline()
    pass_phrase_1 = pass_phrase_1.strip()

  # decrypt and print the plain text using Vigenere cipher
    print(vigenere_decode(cipher_text_1,pass_phrase_1))

    print(filter_string("$$M*&ont@y !?Pyt23h5on (an]{d =t\h~e ##Hol&y G<ra?.il"))

# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()