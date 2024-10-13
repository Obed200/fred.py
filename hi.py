# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 09:59:25 2024

@author: USER
"""
print("______________________________________")
class java():
   while (True):
       def sumOfMultiples(limit):
           
           sum = 0
           for i in range(limit):
               if i % 3 == 0 or i % 5 == 0:
                   sum += i
           return sum
       limit = int(input("Enter a limit: "))

       result = sumOfMultiples(limit)
       print(f"the sum of multiples of 3 and 5 less than {limit} is: {result}")
       
       def countUpperOrLower(inputString):
           upperCount=0
           lowerCount=0
           
           for char in inputString:
               if char.isupper():
                   upperCount +=1
               elif char.islower():
                   lowerCount +=1
           print("Number of uppercase latters:",upperCount)
           print("Number of lowercase latters:",lowerCount)
           
       sampleInputString = input(" Enter any string to count : ")
       countUpperOrLower(sampleInputString)
       
       def sumOfListNumbers(inputList):
           return sum(inputList)
       sampleList = [8,2,4,7,0,3]
       result = sumOfListNumbers(sampleList)
       print("Sum of numbers in the list: ",result)
       
       def repalace_vowels(input_string):
           vowels = "aeiouAOUEI"
           result_string = ""
            
           for char in input_string:
               if char in vowels:
                   
                  result_string += '*'
               else:
                   result_string += char
           return result_string
       inputStr = input("enter a string you want: ")
       outputStr = repalace_vowels(inputStr)

       print("Original String: ", inputStr)
       print("replace a string with a vowels by a *: ",outputStr)                
       
       decision = input('enter "Q" or "q" to quit :')
       if decision != "Q" and decision != 'q':
           continue
       else :
           break
           