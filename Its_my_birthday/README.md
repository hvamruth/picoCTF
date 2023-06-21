# It is my Birthday

Tags : Web Exploitation

Author : MADSTACKS

# Description
--
I sent out 2 invitations to all of my friends for my birthday! I'll know if they get stolen because the two invites look similar, and they even have the same md5 hash, but they are slightly different! You wouldn't believe how long it took me to find a collision. Anyway, see if you're invited by submitting 2 PDFs to my website. http://mercury.picoctf.net:55343/

# Hints
--
1. Look at the category of this problem.
2. How may a PHP site check the rules in the description?

Points : 100

# Solution
I searched up "MD5 collision" and eventually found [this]([url](https://www.mscs.dal.ca/~selinger/md5collision/)) website. It provided 2 executable files ([hello]([url](https://www.mscs.dal.ca/~selinger/md5collision/hello.exe)) and [erase]([url](https://www.mscs.dal.ca/~selinger/md5collision/erase.exe))) which have the same MD5 hash. I downloaded those files and changed the extension to a .pdf file.
I uploaded those two files and the website redirected to the PHP:


The flag can be found in a comment at the end of the PHP (before the HTML portion, line 37)


# Flag
--
picoCTF{c0ngr4ts_u_r_1nv1t3d_aad886b9}
