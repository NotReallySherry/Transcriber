import random
import sys

# 600 15 2 128

outfile = open("test_files/basic_test.txt", 'w')
j = 0
    
# c1 c1
for i in range(0, 256):
    if (i == 128):
        outfile.write(f"{j},0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0\n")
        j+= 15625
    outfile.write(f"{j},0:2,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0\n")
    j += 15625
    
# f1
for i in range(0, 128):
    outfile.write(f"{j},0:0,1:0,0:0,3:0,4:0,5:0,6:0,7:0,8:2,9:0,10:0,11:0,12:0,13:0,14:0\n")
    j += 15625
    
# g# 4
for i in range(0, 30):
    outfile.write(f"{j},0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:2,10:0,11:0,12:0,13:0,14:0\n")
    j += 15625

# c' 64
for i in range(0, 2):
    outfile.write(f"{j},0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:1,9:0,10:0,11:0,12:0,13:0,14:0\n")
    j += 15625

# A 16
for i in range(0, 8):
    outfile.write(f"{j},0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:2,8:0,9:0,10:0,11:0,12:0,13:0,14:0\n")
    j += 15625
    
for i in range (0, 4):
    outfile.write(f"{j},0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0\n")
    j += 15625
