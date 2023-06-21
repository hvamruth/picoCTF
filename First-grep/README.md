# First Grep
Points: 100

# Category
General Skills

# Description
Can you find the flag in file? This would be really tedious to look through manually, something tells me there is a better way.

# Hints
grep tutorials

# Solution
When we simply cat this file in the shell to find the flag, we are met with a lot of random noise. Here,we can use a grep command. 
What grep does is it filters for a specific expression in a plain-text. We know that picoCTF flags are all in the format of 
picoCTF{...}, so we can grep for the expression picoCTF. Specifically, we would do cat file | grep picoCTF.

# Flag
