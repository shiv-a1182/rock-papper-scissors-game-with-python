#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random
options = ["R", "P", "S"]
wc=[("R","S"),("S","P"),("P","R")]
c1=0
c2=0
while True:
    uc = input("R P S ").upper()
    cc=random.choice(options)
    print("Computer chose: ", cc)
    result = (uc, cc)
    if result in wc:
        print("You win!")
        c1=c1+1
        print("user: ",c1,"computer:",c2)
    elif result[::-1] in wc:
        print("Computer wins!")
        c2=c2+1
        print("user: ",c1,"computer:",c2)
    else:
        print("Tie!")
    if c2==5:
        print("computer win")
        break
    elif c1==5:
        print("user wins")
        break


# In[ ]:




