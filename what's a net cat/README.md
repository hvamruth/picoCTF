AUTHOR: SANJAY C/DANNY TUNITIS

# Description
Using netcat (nc) is going to be pretty important. 
Can you connect to jupiter.challenges.picoctf.org at port 64287 to get the flag?

# Hints
nc tutorials

# Solution
As the problem statement has given us the host and the port, all we have to do is talk to it. Simply echo the message gotten when connecting to it using 'echo | nc 2019shell1.picoctf.com 64287'.

# Flag
picoCTF{nEtCat_Mast3ry_284be8f7}
