def rev(str1):
"""Take a string and returns it reversed

Parameters
----------
Input:
n:string
A collection of characters

Output:
revstr: string
A collectiong of characters rearranged to be the reverse of the original string


"""
    revstr = ""
    length = len(str1)
    while length >= 1:
        revstr += str1[length - 1]
        length -= 1
    print(revstr)
	
	
	
	
	
	
	
	
	
	

	
def sort_dict(n):
"""Takes a string, loops through each element and records each character in a dictionary

Parameters
----------
Input:
dct: dictionary
An empty dictionary to log occurrences of letters in and their counts
n:string
A collection of charactrs to be parsed

Output:
dct: dictionary
Filled in dictionary storing characters
"""
    dct = {}
    for elem in n:
        dct[elem] = dct.get(elem, 0) + 1 #check and add character to dictionary
	    return dct
	
def int_convert(dct):
""" Converts letter counts in order for them to be printed later on

Parameters
----------
Input:
dct: dictionary
A dictionary of string character keys and integer values

Output:
dct: dictionary
A dictionary of both string keys and values
"""
    dct1 = {k:str(v) for k,v in dct.items()} #Change integers to strings
    return dct1
	
def dict_print(dct1):
"""Takes a dictionary and appends the keyvalues pairs to a list

Parameters
----------
Input:
dct:dictionary
A dictionary of keys and values

Output:
lst: List
A list of nested lists containing letters and integers, both as strings
"""
    lst = []
    for key, val in dct.items():
        lst.append([key,val]) #Loop through and add nested list items to an empty list
    lst.sort()
    return lst
		
def display_comp(lst):
"""Loops through a list and returns characters followed by their count

Parameters
----------
Input:
lst:list
A list of letters and their occurrences

Output:
(Not entirely sure how to alter this so it prints out the values)

"""
    for elem in lst:
        print(elem, lst[elem])
		
		
		
		
		
		
		
		
		
def list_primes(n):
"""Takes an integer and returns all prime numbers less than it

Parameters
----------
Input:
n:Integer
A number greater than 0

Output:
lst: list
A list of integers that are listed up to the Integer/nearest prime number if the integer itself is not prime


    lst = []
    for p in range(2,n+1):
        for number in range (2,p):
            if p % number == 0:
                break
        else:
                lst.append(p)
            
    return lst
