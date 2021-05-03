# -*- coding: utf-8 -*-
"""project2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rNaE3U_Ki6jTeV1iszj5fC4bAPzlsVtT
"""

#This program can calculate the result for 1 divided by any denominator you enter. 
#However, it is only for repeating decimals and the denominator has to be an integer.
#If you enter a denominator that will result in non-repeating decimal result, the program will never stop.
#The repeating decimal will be shown in brackets () meaning they will keep repeating.
from time import sleep  # For step-by-step display

d = int(input("Input a denominator: ")) 
print(f"1/{d} is being computed")

# Initialization
count = 0       # Counter of the number of steps/decimals
done = False    # Boolean used to detect end of computation
x = 1
qlist = []      #Initiate an empty list for all the quotients
rlist = []      #Initiate an empty list for all the remainders

# Main loop
while not done: # Keep doing until termination is detected
  count += 1
  x = x * 10
  quotient = x // d
  remainder = x % d
  qlist += [quotient]  #Keep adding new elements to the list
  rlist += [remainder]
  if len(qlist)>1:     #We need at least 2 elements to detect whether it's repeating or not
    num1 = qlist[0]    #Assign the first elements of both lists to variables num1 and num2
    num2 = rlist[0]
    for k in range(len(qlist)-1): 
      if qlist[k+1]==num1 and rlist[k+1]==num2: #if both upcoming quoteint AND remainder are the same as the first quoteint and remainder, it starts repeating
        done=True
  print(f"{count} : {quotient} ( {remainder} )")
  sleep(1)
  
  # Check if computation is over
  # If not over, prepare for next step
  if remainder == 0:
    done = True
  else:
    x = remainder
ans = ""  

if d==1:
  print(f"1/{d} = 1")               #When the denominator is 1, we don't want the asnwer to be 0.1
elif  rlist[len(rlist)-1] == 0:      #If it's terminating decimal, we don't need to repeat.
  for i in range(len(qlist)):
    ans += str(qlist[i])
  print(f"1/{d} = 0.{ans}")
else:
  for i in range(len(qlist)-1):     #We don't want the first repeating decimal yet.
    ans += str(qlist[i])
  print(f"1/{d} = 0.{ans}({ans})")  #decimals inside () will be the repeating decimal.



