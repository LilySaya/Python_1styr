# -*- coding: utf-8 -*-
"""project 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fg43DBZaWkQxZ1-uB2AmTI0rnJJ1aMBZ
"""

import matplotlib.pyplot as plt
import copy as copy

count = 0

def print_pegs(pegs):
    """Prints the pegs and the disks they contain."""
    for i, peg in enumerate(pegs):
        print(f"{i}: {pegs[i]}")

def hanoi(n):
    global data
    """Solves the "Tower of Hanoi" puzzle for n disks."""
   
    if n <= 0: raise AssertionError("n must be positive")
    
    # Initialization: the two lines below create the game with 3 pegs
    # and insert n disks on the leftmost peg (peg at index 0)
    # the largest disk is n, then n-1, then ..., until disk 2, and disk 1
    pegs = [[] for _ in range(3)]     # 3 empty pegs
    pegs[0] = list(range(n-1, -1, -1))   # fill the leftmost peg (peg 0) with n disks
    
    data = [[[]for _ in range (3)] for _ in range(2**n)]
    # Display the initial configuration.
    print("Starting configuration")
    print_pegs(pegs)
    
    move_tower(pegs, n, 0, 1)
    print(data)
    
    # move the tower (=the n disks)
    # from the letftmost peg (peg 0) to the central peg (peg 1)

def move_disk(pegs, source, dest):
    """Moves a single disk from peg source to peg dest.

    Args:
        pegs (array):       Array holding the pegs
        source ({0,1,2}):   Source peg
        dest ({0,1,2}):     Destination peg
    """
    global count
    global data
    
    if source not in [0,1,2]:    raise AssertionError("source index out of bounds")
    if dest not in [0,1,2]:      raise AssertionError("destination index out of bounds")
    if pegs[source] == []:       raise AssertionError("source peg is empty")
    disk = pegs[source][-1] # disk is the top disk in the source peg
    if pegs[dest] and (pegs[dest][-1] <= disk): raise AssertionError("destination has smaller disk")

    # The move is valid so (i) we print the move on the screen
    print(f"STEP{count+1}: move disk {disk} from peg {source} to peg {dest}")
    # then (ii) we execute the move

    pegs[source].pop()       # Take the disk on top of the source peg
    pegs[dest].append(disk)  # and move it to the top of the destination peg
    
    data[0][0]=list(range(n-1,-1,-1))
    data[count+1]= copy.deepcopy(data[count]) #took me a few hours here trying to copy. I didn't know about "deepcopy"
    data[count+1][source].pop()
    data[count+1][dest].append(disk)
    
    count+=1
    
    # and (iii) we display the new configuration
    print_pegs(pegs)

def move_tower(pegs, nb_disk, source, dest):
    """Moves a whole tower of nb_disk disks from source peg to dest peg.
    
    Args:
        pegs (array):        Array holding the pegs
        nb_disk ({1,...,n}): Number of disks to move (i.e. height of the tower)
        source ({0,1,2}):    Source peg (i.e., in which the tower is originally)
        dest ({0,1,2}):      Destination peg (i.e., where to put the tower)
    """
    # spare is the third peg (i.e., neither source nor dest)
    spare = 3 - source - dest
  
    if nb_disk == 2:
       move_disk(pegs,source,spare)
       move_disk(pegs,source,dest)
       move_disk(pegs,spare,dest)

    else:
       move_tower(pegs,nb_disk-1,source,spare)
       move_disk(pegs,source,dest)
       move_tower(pegs,nb_disk-1,spare,dest)

# Main program
n = int(input("n = "))
hanoi(n)
print(f"number of times to move the disk = {count} ")

from matplotlib import rc
rc('animation', html='jshtml')

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter, ImageMagickWriter

fig, ax = plt.subplots(figsize=(10,4),
                       subplot_kw=dict(xlim=(-5,25),
                                       ylim=(-0.5,15),
                                       xticks=[],
                                       yticks=[]))
widthlist = []
for i in range(n):
  widthlist.append(1.5*i+2)
plt.bar([0, 10, 20], 14, width=1, color="black")
disks = plt.bar([0]*n, 2, bottom=list(range(n-1, -1, -1)), width=widthlist)

def update(frame):
  # for a given frame, we need to look at the position in SOLUTION[frame]
  # More specifically, we need to find where each disk is located.
  configuration = data[frame]
  for k in range(3):
    peg = configuration[k]   # I am now looking at peg k of current configuration
    # There can be 0, 1, 2, or maybe 3 disks on this peg
    for index, diskNumber in enumerate(peg):
      disks[diskNumber].set_xy( (10*k - disks[diskNumber].get_width()/2,   # 10k is for the peg position (ie 0, 10, 20) and witdh/2 is to center the disk
                                 index)      )                               # index is for the vertical height
     
  return disks

anim = FuncAnimation(fig, update, frames=len(data), interval=1000)

anim

# Let's try to save the animation in video
anim.save('hanoi.mp4', writer=FFMpegWriter(fps=1))
# You can download the video from the files in the left menu
# Unfortunatley, the conversion is not very good and I do not know why
# There is some conversion byg that I cannot solve, but it may be due to Google Colab

# This command is not useful for you,
# but it allows me to display the video on the course website :)
# You can check the following link: https://titechcomp.github.io/y20-bonnet/hanoi.html
anim.to_html5_video()

#I copied everything inclucing comments to save the file as a whole.