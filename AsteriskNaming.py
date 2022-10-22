# Assignment 1:
# Create a program that will print your nickname using only asterisk character (*)

#Nickname: JEN

#This will be my reference:

#     *  *****  *   *
#     *  *      **  *
#     *  *****  * * *
# *   *  *      *  **
#  ***   *****  *   *

Name = "JEN"

printJ = [[" " for i in range(5)] for j in range(5)]
printE = [[" " for i in range(5)] for j in range(5)]
printN = [[" " for i in range(5)] for j in range(5)]

#LETTER J
for row in range(5):
   for col in range(5):
      if (col == 0 and row == 3) or (row == 4 and (col != 0 and col != 4)) or (col == 4 and row != 4):
         printJ[row][col] = "*"

#LETTER E
for row in range(5):
   for col in range(5):
      if (row == 0 or row == 2 or row == 4) or (col == 0 or row == 1 and row == 3):
         printE[row][col] = "*"

#LETTER N
for row in range (5):
   for col in range (5):
      if col == 0 or col == 4 or (row == col and (col>0 and col <4)):
         printN[row][col] = "*"

#DISPLAYING WHOLE NICKNAME (JEN)
for i in range(5):
   for j in range(5):
      print(printJ[i][j], end = " ")
   print(end = "  ")
   for j in range(5):
      print(printE[i][j], end = " ")
   print(end = "  ")
   for j in range(5):
      print(printN[i][j], end = " ")
   print()

