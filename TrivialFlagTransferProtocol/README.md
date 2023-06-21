# Trivial Flag Transfer Protocol

Tags : Foreinsics

Author : DANNY

Points : 90

# Description
Figure out how they moved the flag.

# Hints
What are some other ways to hide data?

# Solution
When looking at the packet capture using Wireshark, I noticed there were a lot of files.
To extract the files on Wireshark:

which shows all the files recorded in the packet capture

files

Click "Save All" to save them.

The files included instructions.txt, plan, program.deb, picture1.bmp, picture2.bmp, and picture3.bmp. Let's analyze each of them individually.

# instructions.txt
Here are the contents of instructions.txt:

GSGCQBRFAGRAPELCGBHEGENSSVPFBJRZHFGQVFTHVFRBHESYNTGENAFSRE.SVTHERBHGNJNLGBUVQRGURSYNTNAQVJVYYPURPXONPXSBEGURCYNA

Its ROT13 encrypted.
Lets decode it.


TFTPDOESNTENCRYPTOURTRAFFICSOWEMUSTDISGUISEOURFLAGTRANSFER.FIGUREOUTAWAYTOHIDETHEFLAGANDIWILLCHECKBACKFORTHEPLAN

Adding space inbetween gives,

TFTP DOESNT ENCRYPT OUR TRAFFIC SO WE MUST DISGUISE OUR FLAG TRANSFER. FIGURE OUT A WAY TO HIDE THE FLAG AND I WILL CHECK BACK FOR THE PLAN

So as mentioned lets check the Plan file.

# Plan

VHFRQGURCEBTENZNAQUVQVGJVGU-QHRQVYVTRAPR.PURPXBHGGURCUBGBF

Its ROT13 encrypted.
Lets decode it.

IUSEDTHEPROGRAMANDHIDITWITH-DUEDILIGENCE.CHECKOUTTHEPHOTOS

Adding space inbetween gives,

I USED THE PROGRAM AND HID IT WITH - DUEDILIGENCE. CHECK OUT THE PHOTOS

Program.deb
After extracting program.deb we shall find that it has the files related to steghide.
So now let's use steghide to analyse the bmp files.
There are three bmp images - picture1.bmp picture2.bmp picture3.bmp.
We need a password to exctract the file if anything is hidden inside.
In the previous file we got a hint that I USED THE PROGRAM AND HID IT WITH-DUE DILIGENCE.
So DUEDILIGENCE is the password.
After trying the steghide command in all three images, the flag.txt was found in the image picture3.bmp.

steghide extract -sf picture3.bmp

# Flag

