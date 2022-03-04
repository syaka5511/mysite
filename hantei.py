# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 00:11:32 2022

@author: syaka

"""



from count_file import fileall



import random as rd
        
f = fileall()
no = list(range(1,f,1))

正解 = 1

while len(no) > 1 and 正解 == 1:
    new = rd.choice(no)
    no.remove(new)
    old = rd.choice(no)
    no.remove(old)
    判定 = new >= old
    答え = input("答えを入力してください")
    if str(判定) == str(答え):
        print("yes")
    else:
        print("no") 
        正解 = 0

    print(no)
   