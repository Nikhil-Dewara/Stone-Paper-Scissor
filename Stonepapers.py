# """Redmi
#
# 1-we take input from user(Stone,Paper,Scissor)
# 2-Computer Choice randomly There we use Randint
# 3-Result Print
#
# Cases:
# A-Rock
# Rock - Rock= tie
# Rock - Paper= Paper win
# Rock - Scissor = Rock win
#
# B- Paper
#
# Paper - Paper= tie
# Paper - Rock= Paper win
# Paper - Scissor= Scissor win
#
# C- Scissor
#
# Scissor - Scissor= tie
# Scissor - Rock= Rock win
# Scissor - Paper= Scissor win
# """
#
# import random
# item_list=["Rock","Paper","Scissor"]
#
# user_choice=input("Enter your move: = Rock, Paper , Scissor ")
# comp_choice=random.choice(item_list)
#
# # f is use for string formate
# print(f"User Choice = {user_choice} , Computer Choice = {comp_choice}")
#
# if user_choice == comp_choice:
#     print(" Both Choose same : = Match Tie !")
#
# elif user_choice=="Rock":
#     if comp_choice=="Paper":
#         print("Paper Cover Rock! = Computer Win ")
#     else:
#         print("Rock Smashes Scissor! = You Win ")
#
# elif user_choice=="Paper":
#     if comp_choice=="Scissor":
#         print("Scissor Cut Paper! = Computer Win ")
#     else:
#         print("Paper Cover Rock! = You Win ")
#
# elif user_choice=="Scissor":
#     if comp_choice=="Paper":
#         print("Scissor Cuts Paper! = You Win ")
#     else:
#         print("Rock Smashes Scissor! = Computer Win ")


# n=int(input("Enter  number you want to add in list"))
# l=[]
# for i in range(n):
#     data=int(input("Enter a number "))
#     l.append(data)
# print(l)
#
# list1=list(filter(lambda x: x%2==0,l))
# print(list1)




