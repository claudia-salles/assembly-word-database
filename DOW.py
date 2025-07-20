
#____________ Saving & Displaying Error Mechanism ______________________
def show_exception_and_exit(exc_type, exc_value, tb):
    import traceback
    traceback.print_exception(exc_type, exc_value, tb)
    input("Press any key to exit.")
    sys.exit(-1)

import sys
sys.excepthook = show_exception_and_exit


# This script:
# 1. as its main function, it generates the properties of all assembly words of some size and saves them in a text file.
# 2. holds the class construction of DOW objects, holding all the properties of a given assembly word.
# 3. contains further functions: creating a DOW given a word and filtering through all words with certain properties.

# IMPORTANT: This file gathers data from the "Data" folder and imports functions from dow_operations.py, 
# so they must be located in the same folder in order to work.

import dow_operations 
import os

# string holding the location of this file, used to find the required data files
current_file_path = os.path.realpath(__file__) 
current_file_name = os.path.basename(__file__)
for i in range(len(current_file_name)):
    current_file_path=current_file_path[:-1]


class DOW:

	def __init__(self, w, n, an, pal, w_i, s_i):
			self.word = w 				#string
			self.size = n 				#int
			self.assembly_number= an 	#int
			self.palindromic = pal		#bool
			self.weakly_irr = w_i 		#bool
			self.strongly_irr = s_i 	#bool


	def __str__(self):
		return "[{0}, {1}, {2}, {3}, {4}, {5}]".format(self.word, self.size, self.assembly_number, self.palindromic, self.weakly_irr, self.strongly_irr)


def createDowProperties(dow): #creates a DOW object that holds all the propeties of a DOW

	# checks if input is a Double Occurance Word first, then its properties are retrieved
	if dow_operations.isDOW(dow)==True and dow == dow_operations.ascending(dow):
		n=dow_operations.getSize(dow)
		an=dow_operations.getAssemblyNumber(dow)
		pal=dow_operations.isPalindromic(dow)
		w_i=dow_operations.isWeaklyIrreducible(dow)

		if w_i == True: #since all s_i words are also w_i, s_i is checked only is the word is already w_i.
			s_i=dow_operations.isStrictlyIrreducible(dow)
		else:
			s_i= False

		print('Storing properties for dow:', dow)
		return DOW(dow, n, an, pal, w_i, s_i)

	else: 
		print('Object could not be be created for input:', dow)



def getWordsFromProp(size, an, pal, w_i, s_i): # given the property request, words are searched and stored with such properties
	word_list=[]

	def isSatisfactory(prop):
		if an =='' or prop[2]==an:
			if pal=='0' or (pal=='1' and prop[3]=='True') or (pal=='2' and prop[3]=='False'):
				if w_i=='0' or (w_i=='1' and prop[4]=='True') or (w_i=='2' and prop[4]=='False'):
					if s_i=='0' or (s_i=='1' and prop[5]=='True') or (s_i=='2' and prop[5]=='False'):
						return True
		return False

	# the most imporatnt computing factor is size, so only the file of interest is retrieved
	if size=='': 
		for i in range(1,8):
			file_name=current_file_path+"Data/assembly_word_properties_"+str(i)
			try:

				file=open(file_name, 'r')

				with file:
					for line in file:
						prop_list=line.strip().replace("[", "").replace("]", "").split(', ')
						if isSatisfactory(prop_list)==True:
							word_list.append(prop_list[0])


			except OSError:
				print ("Could not open/read file:", file_name)
				print ("Make sure that the desired file have been generated and that they are stored in the same directory as the DOW.py, dow_operations.py and main.py scripts.")

	else: 
		try:
			file_name=current_file_path+"Data/assembly_word_properties_"+str(size)
			file=open(file_name, 'r')
			for line in file:
				prop_list=line.strip().replace("[", "").replace("]", "").split(', ')
				if isSatisfactory(prop_list)==True:
					word_list.append(prop_list[0])
				
		except OSError:
			print ("Could not open/read file:", file_name)
			print ("Make sure that the desired file have been generated and that they are stored in the same directory as the DOW.py, dow_operations.py and main.py scripts.")

	return word_list

		


if __name__ == '__main__': # generates the properties of all assembly words of some size and saves them in a text file

	#____________Size input with Error Detection______________________

	check=False
	max_num=7

	while check==False:

		try:
			n=input("What size assembly words do you want to compute the properties of?")
			
			n=int(n)

		except ValueError:
			os.system('cls')
			print("Invalid input, please input an integer.")
			print()
			print()
		
		else:
			if n<=max_num and n>0:
				check=True
				print(n)
			else:
				os.system('cls')
				print("The number you inputted was out of range. The current program can only compute assmebly words up to size", max_num,".")
				print()
				print()

	print ('Strating: computing properties of assembly words of size', n)
	file_name=current_file_path+"Data/assembly_words_"+str(n)

	try:

		file=open(file_name, 'r')


		with file:
			print(file_name, 'has successfully been opened.')
			new_file_name=current_file_path+"Data/assembly_word_properties_"+str(n)
			new_file=open(new_file_name, 'w')


			# for every assembly word, a DOW object is created and their property information is saved
			for line in file:
				dow_prop=createDowProperties(line.strip()).__str__()
				new_file.write(dow_prop+"\n")


	except OSError:
		print ("Could not open/read file:", file_name)
		print ("Make sure that the desired file have been generated and that they are stored in the same directory as the DOW.py, dow_operations.py and main.py scripts.")



