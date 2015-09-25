0. eight = 8
1. b = eight
2. print(b)
3.  if x is 'a' or x is 'b:
        return True
    else:
	    return False
4. if x > 10 and x%2 != 0:
       return True
5. def param(n):
       return(n)
6. def triple_print(n):
       x = 0
	   while x != 3:
	       print(n)
		   x += 1
7. def wage():
       h = eval(input("Enter Hours: "))
	   r = eval(input("Enter Rate: "))
	   p = h*r
	   print("Pay: ", p)
8.  str1 + str2 
	#This will return a temporary copy, 
	#to retain the concatenated value See below
	str3 = str1 + str2
9. str1[4], str1[-1]
10. str1 * 3
11. lst = [0,1,2,3,4,5,6,7,8,9,10]
12. lst.append('hi')
13. lst.remove(4)
14. 5 in lst
15. for elem in lst[:10]:
	    print(elem)
16. for elem in lst:
	    print(elem)
17. for elem in lst:
	    print(elem * 2)
18. x = 0
	while x = 0:
	    print(x)
		x += 10
19. def check_empty(n):
	    if n == None:
			return None
20. ('a',)
21. ('a','b')
22. Actor1 = ('Dicaprio',43)
	Name, Age = Actor1
23. dct = {}
24. dct.update({'one':1,'two':2,'three':3})
25. dct['two'] = 'dos'
26. del dct['two']
27. for key in dct:
	    print(key)
28. for val in dct.values():
	    print(val)
29. for key, val in dct.items()
	    print(key, val)
30. for pairs in dct.items():
	    print(pairs)
		
31. #Dictionaries are mutable unlike tuples and can be useful for 
	#counting and cataloguing occurrences of words/integers in files
	
32. #Mutability and Immutability pertain to the nature of various datatypes in programming languages
	#Immutable types such as strings and tuples cannot be altered once created and in order to 
	#change them a copy of them needs to be made to change them.  Mutable items such as integers,
	#dictionaries(values are mutable, keys are not) and lists can be altered in place without the need 
	#to make copies of them in order to alter them

33. #Examples of homogeneous datatypes are strings where characters/integers enclosed in apostrophes/quotes
	#are all the same type. Heterogeneous datatypes include lists and dictionaries where combinations of integers, strings
	#and even nested lists and dictionaries can be inserted and removed

34. #Overflow is related to the set capacity of variables and objects created in programming, for example
	#in a range of numbers from 0 to 4 there are only 5 possible numbers and when looping through the range
	#the loop would be unable to continue beyond/overflow past the number 4

35. #Abstraction is the process in programming/mathematics/logic referring to reasoning in a manner that deals with
	#focusing on the basic components of a problem and breaking them down into their simplest parts in order to
	#understand the process step by step
36. # Modularization is a concept in programming that relates to elegantly and efficiently breaking down a program
	# into numerous small and functional components.  
	#To modularize for example 1+1,although it would be excessive one could make four functions 
	#to process it, the first function to intake the first integer (1), 
	#the second function to intake the second integer (1), 
	#a third function to arithmetically add them (1+1)
	#and a fourth function to return the sum (2)
37. string:IM/HO
	list: M/HE
	tuple: IM/HE
	dictionary: M/HE
38. #Printing returns a displayed output to the user whereas return is useful for feeding
	#results into other functions without displaying the intermediate results and only the 
	#final results when print is used at the end of a program
