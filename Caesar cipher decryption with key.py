# -*- coding: utf-8 -*-
"""HW3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BodHZ8NwETEKQR-a3iZkXZu7hQZKKsr8
"""

def enc(k, m):
    """Encode the message m
    with Caesar cipher and shift key k.
    Change only lowercase characters,
    Keep other characters"""
    c = []
    a = list(m.encode("ascii"))
    for i in range(len(a)):
      if a[i] in range(97,122):
        c+= [(a[i]-97+k)%26 +97]
    ans = bytes(c).decode("ascii")
    return ans

def enc2(k,msg):
  charCodes = list(msg.encode("ascii"))
  for i in range(len(charCodes)):
    if 97 <= charCodes[i] <= 122: # Check if the i-th character is a lowercase letter
      offset = charCodes[i] - 97# Compute the "index" of this letter wrt. letter 'a'
      offset = (offset + k) % 26# Compute the "index" shifted by k
      charCodes[i] = offset + 97# Compute the ascii code of the encrypted letter
 
  ciphertext = bytes(charCodes).decode("ascii")
  return ciphertext

# Main program
k = int(input("Encryption key k = "))
plaintext = input("Plaintext: ")
ciphertext = enc(k, plaintext)
print(f'The encryption of "{plaintext}" using key k={k} is "{ciphertext}"')



