#lesser of two evens, write a function that returns the lesser of two given fucntions if both numbers are even
#but returns the greater if one or btoh are odd

# lesser_of_two_evens(2,4) ---> 2
# lesser_of_two_evens(2,5) ---> 5

# def lesser_of_two_evens(a,b):
#
#     if a%2 == 0 and b%2 == 0:
#     #both numbers are even so we want to return lesser of both numbers
#         result = min(a, b)
#     # else:
#     #    if a > b:
#     #       result = a
#     # else:
#     #       result = b
#     else:
#         result = max(a, b)
#
#     return result
#
#
# # print(lesser_of_two_evens(2, 4))
# print(lesser_of_two_evens(2, 7))

#can use the min function to run above code faster and simpler commented out and added new way above

#Questin 2 - write a function that takes a two word string and returns true if both words begin with the same letter:

# def animal_crackers(text):
#     wordlist = text.split() #variable wordlist and use split to get the letters
#     print(wordlist)
#
#     first = wordlist[0]
#     second = wordlist[1]
#
#     return first[0] == second[0]
#
# print(animal_crackers('Levelheaded Lama'))
# print(animal_crackers('Crazy Kanagroo'))

# #question 3 - given two intergers return True if the sum of the intergers is 20 or if one of the intergers is 20, if not return false
# def makes_twenty(n1,n2):
#     if n1 + n2 == 20:
#        return True
#     elif n1 == 20:
#         return True
#     elif n2 == 20:
#         return True
#     else:
#         return False
# print(makes_twenty(3,5))







