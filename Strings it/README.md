# Strings it

Tags : General Skills

AUTHOR: SANJAY C/DANNY TUNITIS

# Description
Can you find the flag in file without running it?

# Hints
strings

# Solution

The title and tutorial in the hint seems to point towards using the strings command like strings strings to get the flag. However, we are met with a lot of plain-text upon doing so, which would be quite the hassle to sort through manually. Instead, we can use the grep command which filters for specifc expressions in plain-text. Since we know the format of picoCTF flags is picoCTF{...}, we can grep for picoCTF. The command would then be strings 
'strings | grep picoCTF'

# Flag
