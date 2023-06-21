# Easy 1

Cryptography, 100 points

# Description
The one time pad can be cryptographically secure, but not when you know the key. 
Can you solve this? We've given you the encrypted flag, key, and a table to help 
UFJKXQZQUNB with the key of SOLVECRYPTO. Can you use this table to solve it?.

# Solution
This is a classic [Vigenère cipher](url). It's easily solvable using any online decoder, such as Cyberchef.

In order to decode the message manually, we use the following algorithm:

For each letter in the key:
Find the row corresponding the the letter
In the row, find the column which contains the matching ciphertext letter
The matching plaintext letter is noted at the top of the column
In our case, the plaintext is CRYPTOISFUN.
