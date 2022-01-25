# KBC Game


status = True
price=0
count=0

while status:
   print("\n    Welcomt TO KBC...    \n")
   print('Select Life Line by Press = "L" [2 Life line Available for you]\n')

   print("1)What is it that is available outside for free and in the hospital for money?")  # A
   print('''
   [A] Oxygen   [B] Room
   [C] Doctors   [D] Painkiller 
   ''')

   ans=input("Enter Your Answer : ")
 
   if ans=="a" or ans=="A":
      print("\nRight Answer")
      price+=2000
      print(f"You Win {price} Rs")
   
   elif ans=="L" or ans=="l":
      if count<2:
         count+=1
         print("\nAnswer is [A] Oxygen")
         
      else:
         print("\nYour Life line is over.")
         print("****Game Over****")
         break

   else:
      print("\n-Wrong Answer-")
      print("****Game Over****")
      break

   # ================================================================
   
   print("\n2) Which question's answer changes all the time?") # D
   print('''
   [A] Is this your car   [B] Where do you live
   [C] Do you have a job   [D] What is the time 
   ''')
    
   ans=input("Enter Your Answer : ")

   if ans=="D" or ans=='d':
      price+=2000
      print("\nRight Ansewer")
      print(f"You Won {price} Rs")
   
   elif ans=="L" or ans=="l":
      if count<2:
         count+=1
         print("\nAnswer is [D] What is the time")

      else:
         print("\nYour Life line is over.")
         print("****Game Over****")
         break


   else:
      print("\n-Wrong Answer-")
      print("****Game Over****")
      break

   # ================================================================

   print("\n3) Which city has Juhu Beach?") # B
   print('''
   [A] Surat   [B] Mumbai
   [C] Goa   [D] Delhi 
   ''')
    
   ans=input("Enter Your Answer : ")

   if ans=="B" or ans=='b':
      price+=2000
      print("\nRight Ansewer")
      print(f"You Won {price} Rs")
   
   elif ans=="L" or ans=="l":
      if count<2:
         count+=1
         print("\nAnswer is [B] Mumbai")
          
      else:
         print("\nYour Life line is over.")
         print("****Game Over****")
         break

   else:
      print("\n-Wrong Answer-")
      print("****Game Over****")
      break

   # ================================================================
   
   print("\n4) What is it that we can see but cannot touch?") # C
   print('''
   [A] Animals   [B] Light
   [C] Dream   [D] Wall 
   ''')
    
   ans=input("Enter Your Answer : ")

   if ans=="C" or ans=='c':
      price+=2000
      print("\nRight Ansewer")
      print(f"You Won {price} Rs")
   
   elif ans=="L" or ans=="l":
      if count<2:
         count+=1
         print("\nAnswer is [C] Dream")
          
      else:
         print("\nYour Life line is over.")
         print("****Game Over****")
         break

   else:
      print("\n-Wrong Answer-")
      print("****Game Over****")
      break

   # ================================================================
   
   print("\n5) What is it that grows by giving?") # B
   print('''
   [A] Money   [B] Knowledge
   [C] Hair   [D] Idea 
   ''')
    
   ans=input("Enter Your Answer : ")

   if ans=="B" or ans=='b':
      price+=2000
      print("\nRight Ansewer")
      print(f"You Won {price} Rs")
   
   elif ans=="L" or ans=="l":
      if count<2:
         count+=1
         print("\nAnswer is [B] Knowledge")
          
      else:
         print("\nYour Life line is over.")
         print("****Game Over****")
         break

   else:
      print("\n-Wrong Answer-")
      print("****Game Over****")
      break

   # ================================================================
   
   print("\n6) Which of the following states is correct?") # D
   print('''
   [A] Chennai   [B] Kochi
   [C] Kolkata   [D] Gujarat 
   ''')
    
   ans=input("Enter Your Answer : ")

   if ans=="D" or ans=='d':
      price+=2000
      print("\nRight Ansewer")
      print(f"You Won {price} Rs")
   
   elif ans=="L" or ans=="l":
      if count<2:
         count+=1
         print("Answer is [D] Gujarat")
          
      else:
         print("\nYour Life line is over.")
         print("****Game Over****")
         break

   else:
      print("\n-Wrong Answer-")
      print("****Game Over****")
      break

   # ================================================================
   
   print("\n7) What is always in front of you but can't be seen?") # D
   print('''
   [A] Future   [B] Truck
   [C] Animals   [D] TV 
   ''')
    
   ans=input("Enter Your Answer : ")

   if ans=="A" or ans=='a':
      price+=2000
      print("\nRight Ansewer")
      print(f"You Won {price} Rs")
   
   elif ans=="L" or ans=="l":
      if count<2:
         count+=1
         print("Answer is [A] Future")
          
      else:
         print("\nYour Life line is over.")
         print("****Game Over****")
         break

   else:
      print("\n-Wrong Answer-")
      print("****Game Over****")
      break

   # ================================================================
   
   print("\n8) What is the thing that breaks just by speaking?") # B
   print('''
   [A] Table   [B] Silence
   [C] Mirror   [D] Tv 
   ''')
    
   ans=input("Enter Your Answer : ")

   if ans=="B" or ans=='b':
      price+=2000
      print("\nRight Ansewer")
      print(f"You Won {price} Rs")
   
   elif ans=="L" or ans=="l":
      if count<2:
         count+=1
         print("Answer is [B] Silence")
          
      else:
         print("\nYour Life line is over.")
         print("****Game Over****")
         break

   else:
      print("\n-Wrong Answer-")
      print("****Game Over****")
      break

   # ================================================================
   
   print("\n9) What is something that does not get wet even in water?") # C
   print('''
   [A] Book   [B] Clothes
   [C] Shadow   [D] Vegitables 
   ''')
    
   ans=input("Enter Your Answer : ")

   if ans=="C" or ans=='c':
      price+=2000
      print("\nRight Ansewer")
      print(f"You Won {price} Rs")
   
   elif ans=="L" or ans=="l":
      if count<2:
         count+=1
         print("Answer is [C] Shadow")
          
      else:
         print("\nYour Life line is over.")
         print("****Game Over****")
         break

   else:
      print("\n-Wrong Answer-")
      print("****Game Over****")
      break
   
   # ================================================================
   
   print('''\n10) Find the missing element in the series given below:
            ABD EFH IJL MNP QRT ? ''') # D
   print('''
   [A] ZXA   [B] WXY
   [C] XYZ   [D] UVX 
   ''')
    
   ans=input("Enter Your Answer : ")

   if ans=="D" or ans=='d':
      price+=2000
      print("Right Ansewer")
      print("\n**Congratulation**")
      print(f"You Won {price} Rs")
   
   elif ans=="L" or ans=="l":
      if count<2:
         count+=1
         print("Answer is [D] UVX")
         print("\n**Congratulation**")
         print(f"You Won {price} Rs")

      else:
         print("\nYour Life line is over.")
         print("****Game Over****")
         break

   else:
      print("-Wrong Answer-")
      print("****Game Over****")
      break

   status=False