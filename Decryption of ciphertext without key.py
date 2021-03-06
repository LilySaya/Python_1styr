# -*- coding: utf-8 -*-
"""project3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OzohqcSrREr9cWsEvMW9dVpQP1Ka4TuG
"""

def enc(k, msg):
    """Encode the message m
    with Caesar cipher and shift key k.
    Change only lowercase characters,
    Keep other characters"""
    a = list(msg.encode("ascii"))
    for i in range(len(a)):
      if a[i] in range(97,123):
          
    ans = bytes(a).decode("ascii")
    return ans

def dec(k, code):
    a = list(code.encode("ascii"))
    for i in range(len(a)):
      if a[i] in range(97,123):
        a[i]= (a[i]-97-k)%26 +97
    ans = bytes(a).decode("ascii")
    return ans

####################
### MAIN PROGRAM ###
####################
# You do not need to modify anything here
# (except if you find some errors...)
def caesarCipher():
  print("Caesar Cipher Application")
  print("What do you want to do?")

  # Ask the use to choose between enc or dec
  # There is a loop to keep asking until the user makes a valid choice!
  # Note the use of the 'break' statement here to exist the loop
  while True:
    task = input("Type 'enc' for encryption and 'dec' for decryption: ")
    if task == "enc" or task == "dec":
      break    # <- exit the main loop when the choice is valid
    print("Invalid command. Try again!")

  # A small example to handle basic errors
  # If the use does not write a valid number
  # Then we write a message and use a default value
  try:
    k = int(input("Encryption key k = "))
  except ValueError:
    print("Invalid key; I will use k=3 by default")
    k = 3

  if task == "enc":
    plaintext = input("Write the plaintext: ")
    ciphertext = enc(k, plaintext)
    print("The corresponding ciphertext is:")
    print(ciphertext)
  else:
    ciphertext = input("Write the ciphertext: ")
    plaintext = dec(k, ciphertext)
    print("The corresponding plaintext is:")
    print(plaintext)

# Execute the main program
caesarCipher()

# You can define some functions to help you here
def findenckey(text):
    a = list(text.encode("ascii"))
    freq = {}
    for i in range(len(a)):
        if a[i] in freq:
            freq[a[i]] += 1
        else:
            freq[a[i]] = 1
    values = list(freq.values())
    maxfreq = values[0]
    for k in range(len(values)):
      if values[k]>=maxfreq:
        maxfreq = values[k] 
    for key,value in freq.items():
      if value == maxfreq:
        enckey = key-101
   
   
    return enckey

def dec(k, code):
    a = list(code.encode("ascii"))
    for i in range(len(a)):
      if a[i] in range(97,123):
        a[i]= (a[i]-97-k)%26 +97
    ans = bytes(a).decode("ascii")
    return ans
    


####################
### MAIN PROGRAM ###
####################
def caesarCryptanalysis():
  print("Caesar Cipher Cryptanalysis")
  print("Write the ciphertext and I will try to decode it for you!")
  ciphertext = input("Ciphertext: ")
  enckey = findenckey(ciphertext)
  print(f"The enckey is {findenckey(ciphertext)}")
  print(dec(enckey,ciphertext))


  # TOWRITE

# Execute the main program
caesarCryptanalysis()



