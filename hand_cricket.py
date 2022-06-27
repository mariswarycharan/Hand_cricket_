from ast import While
from calendar import different_locale
import random
from secrets import choice
from tkinter import W
a=int(input("enter starting number:"))
b=int(input("enter ending number:"))
print()
print("""ready for toss say even or odd !!!!!!!!!!
       if you want to say even please enter  1 (even = 1) 
       if you want to say odd please enter 2 (odd = 2 )""")

  
def first_innings():
    total_run=0
    while True:
        bowler=random.randint(a,b) 
        batsman=int(input("you are bating:"))
        print("ball put by bowler is",bowler)
        if batsman>b:
            print(""" invaided input 
                    and please enter value inbetween 1 and 6""")
            break
        if batsman==bowler:
            if total_run == 0:
                print("you are duck out")
            print("you are out")
            print("total run:",total_run)
            break
            
        else:
            total_run+=batsman
            print("current runs:",total_run)
            
        print()
        
    print()    
    print("target for computer:",total_run)   
    print("now you is bowling ready to bowl") 
    print()       

    total_score=0
    while True:
        batsman=random.randint(a,b)
        bowler=int(input("you is bowling:"))
        print("shot hit by batsman is",batsman)
        if bowler>b:
            print("""invaided input 
                     and  please enter value between 1 and 6""")
            break
        if bowler==batsman:
            if total_score==0:
                print("computer is duck out")
            print("computer is out")
            print("total runs hit by computer:",total_score)
            break
        
            
        else:
            total_score+=batsman
            print("current score hit by computer :",total_score)
            if total_run<total_score:
                break
        print()
        
        
    if total_run>total_score:
        print("final result !!!!!!!!!!!!!!!!!")
        print("total run hit by you :",total_run)
        print("total run hit by computer :",total_score)
        print("you won the match")
    elif total_run<total_score:
        print("final result !!!!!!!!!!!!!!!!!")
        print("total run hit by you :",total_run)
        print("total run hit by computer :",total_score)
        difference = total_score - total_run
        print("you lost the match by",difference)
            
    
    
        
def second_innings():
    total_score=0
    while True:
        batsman=random.randint(a,b) 
        bowler=int(input("you is bowling:"))
        print("shot hit by batsman is",batsman)
        if bowler>b:
            print("enter value between 1 and 6")
            break
        if bowler==batsman:
            if total_score==0:
                print("computer is duck out")
            print("computer is out")
            print("total run hit by computer:",total_score)
            break
            
        else:
            total_score+=batsman
            print("current score hit by computer:",total_score)
        print()
    print()    
    print("target for me:",total_score)    
    print("now you are bating and ready to bat")        
    print()    
    total_run=0
    while True:
        bowler=random.randint(a,b) 
        batsman=int(input("you are bating:"))
        print("ball put by bowler is",bowler)
        if batsman>b:
            print("enter value between 1 and 6")
            break
        if batsman==bowler:
            if total_run==0:
                print("you are duck out")
            print("you are out")
            print("total run:",total_run)
            break
            
        else:
            total_run+=batsman
            print("current runs:",total_run)
            if total_run>total_score:
                break
        print()
        
    if total_run>total_score:
        print("final result !!!!!!!!!!!!!!!!!")
        print("total run hit by you :",total_run)
        print("total run hit by computer :",total_score)
        print("you won the match")
    elif total_run<total_score:
        print("final result !!!!!!!!!!!!!!!!!")
        print("total run hit by you :",total_run)
        print("total run hit by computer :",total_score)
        difference = total_score - total_run
        print("you lost the match by",difference) 
        

choice = int(input("enter value 1 or 2 to select even or odd:"))        
c=int(input("enter your number between 1 and 6 for  toss: "))
d=random.randint(a,b)
print("number put by computer for toss:",d)
v = c + d        

if choice > 2 or choice < 0 :
    while True:    
        print("you entered invaided choice for toss")
        break
        
if choice == 1:
    
    if v % 2 == 0:
        print("yes!!! it is even so you won toss ")
        print("""decide bating or bowling 
            if you like bat first enter value = 1 (bating=1)
            if you like bowl first enter value = 2 (bowling=2)""")
        g=int(input("decide bating or bowling enter value 1 or 2 :"))
        
        if g > 2 or g < 0:
            while True:
                print("you entered invaided decision for bating or bowling ")
                break
        
        if g == 1:
            print("you decided to bat first")
            x=first_innings()
            print(x)

        if g== 2:
            print("you decided to bowl first and you are chasing ")
            y=second_innings()
            print(y)
            
    if v % 2 != 0: 
        print(" ohhh it is odd so you loss the toss")
        print()
        h=random.randint(1,2)
        print("""decide bating or bowling 
            if you like bat first enter value = 1 (bating=1)
            if you like bowl first enter value = 2 (bowling=2)""")
        print("value put by computer to decide bating or bowling:",h)
        if h == 1:
            print(" computer decided to bat first")
            y=second_innings()
            print(y)
        if h == 2:
            print(" computer decided to bowl first and you are chasing ")
            x=first_innings()
            print(x)
            
                
        
if choice == 2:
    if v % 2 != 0:
        print("yes!!!! it is odd so you won toss")
        print()
        
        g=int(input("decide bating or bowling enter value 1 or 2 :"))
        
        if g > 2 or g < 0:
            while True:
                print("you entered invaided decision for bating or bowling ")
                break
        
        if g == 1:
            print("you decided to bat first")
            x=first_innings()
            print(x)
        if g == 2:
            print("you decided to bowl first and you are chasing ")
            y=second_innings()
            print(y)    
    if v % 2 == 0:
        print("ohhh it is even so you loss the toss")
        print()
        h=random.randint(1,2)
        print("""decide bating or bowling 
            if you like bat first enter value = 1 (bating=1)
            if you like bowl first enter value = 2 (bowling=2)""")
        print("value put by computer to decide bating or bowling:",h)
        if h == 1:
            print(" computer decided to bat first")
            y=second_innings()
            print(y)
        if h == 2:
            print(" computer decided to bowl first and you are chasing ")
            x=first_innings()
            print(x)
                
              
                

