
#____________ Saving & Displaying Error Mechanism ______________________
def show_exception_and_exit(exc_type, exc_value, tb):
    import traceback
    traceback.print_exception(exc_type, exc_value, tb)
    input("Press key to exit.")
    sys.exit(-1)

import sys
sys.excepthook = show_exception_and_exit


# Assembly words have many properties and operations; all their functions are saved here.

# IMPORTANT: This file gathers data from the "Data" folder, 
# so they must be located in the same folder in order to work.

import itertools
import os

# string holding the location of this file, used to find the required data files
current_file_path = os.path.realpath(__file__)
current_file_name = os.path.basename(__file__)
for i in range(len(current_file_name)):
    current_file_path=current_file_path[:-1]


def ascending(dow): # given a dow, return the same word in acending order (first number is 1, then 2, etc)
	size=int((len(dow)+1)/4)

	substitution=[None]*size
	counter=0

	for i in range(4*size-1):
		# print(dow[i])
		if dow[i]!=' ' and dow[i]!= None:
			if  not dow[i] in substitution:
				substitution[counter]=dow[i]
				counter+=1


	dictionary={ord(substitution[i]) : ord(str(i+1)) for i in range(size)}
	ascending_dow = dow.translate(dictionary)
	return ascending_dow




def reverse(dow): # returns string reversed

	reverse_dow=dow [::-1]	
	ascending_reverse_dow=ascending(reverse_dow)

	return ascending_reverse_dow


def isDOW(dow): # checks if input is a double occurance word in ascending order, if so, returns True
	
	try:
		dow_list=dow.split()
		dow_list=[int(x) for x in dow_list]

		for i in range(max(dow_list)):

			occurance=0

			for j in range(len(dow_list)):
				if dow_list[j]==i+1:
					occurance+=1

			if occurance!=2:
				# print('The DOW was not inputted in the correct format.')
				return False

		dow_word=" ".join(str(x) for x in dow_list)

		if dow_word==dow:
			return True
		else:
			# print('The DOW was not inputted in the correct format.')
			return False

	except ValueError:
		# print('The DOW was not inputted in the correct format.')
		return False
	
	

def getSize(dow): # retunrs size of word (its highest integer element), based on dow string format
	return int((len(dow)+1)/4)


def getAssemblyNumber(dow): #searches An_2 and An_3 files, returns a word's assembly number

	for i in range(2,4):

		file_name=current_file_path+"Data/An"+str(i)


		try:
			f=open(file_name, 'r')

			with f:
				for line in f:
					if line.strip()==dow:
						return i


		except OSError:
			print ("Could not open/read file:", file_name)
			print ("Make sure that the desired file have been generated and that they are stored in the same directory as the DOW.py, dow_operations.py and main.py scripts.")


	return 1


def isPalindromic(dow): #returns True if a word is equivalent un to isomorphism (in ascending order) to its reverse 

	reverse_dow=reverse(dow)

	if reverse_dow==dow:
		return True
	else: 
		return False



def isWeaklyIrreducible(dow): #returns True if the word cannot be split into two assembly words

	n=getSize(dow)
	
	for i in range(n-1):
		if isDOW(dow[:(4*i+3)]) == True:
			return False
						
	return True	



def isStrictlyIrreducible(dow): #returns True if the word does not contain a smaller size assembly word as a sub string
	
	#checks if s.i. given that it is w.i. already (a.k.a doesn't check subwords starting with 1)

	n=getSize(dow)
	dow_list=dow.split()
	
	if n==1:
		return True

	for j in range(2,n+1):
		number_list=[str(j)]
		for i in number_list:
			counter=dow_list.index(i)+1

			while dow_list[counter]!=i and counter<len(dow_list):				
				if not (dow_list[counter] in number_list):
					number_list.append(dow_list[counter])
				counter+=1

		if len(number_list)!=n:
			return False
	
	return True

