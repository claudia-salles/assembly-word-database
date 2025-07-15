

def ascending(dow):
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




def reverse(dow):

	reverse_dow=dow [::-1]	
	ascending_reverse_dow=ascending(reverse_dow)

	return ascending_reverse_dow


def isDOW(dow):
	
	try:
		dow_list=dow.split()
		dow_list=[int(x) for x in dow_list]

		for i in range(max(dow_list)):

			occurance=0

			for j in range(len(dow_list)):
				if dow_list[j]==i+1:
					occurance+=1

			if occurance!=2:
				print('The DOW was not inputted in the correct format.')
				return False

		dow_word=" ".join(str(x) for x in dow_list)
		print(dow_word)

		if dow_word==dow:
			return True
		else:
			print('The DOW was not inputted in the correct format.')
			return False

	except ValueError:
		print('The DOW was not inputted in the correct format.')
		return False
	
	

def getSize(dow):
	return int((len(dow)+1)/4)



def isPalindromic(dow):

	reverse_dow=reverse(dow)

	if reverse_dow==dow:
		return True
	else: 
		return False

# print(isPalindromic('1 2 2 1')) # True
# print(isPalindromic('1 1 2 2')) # True
# print(isPalindromic('1 2 1 2 3 3')) # False 



def isWeaklyIrreducible(dow):

	n=getSize(dow)

	for i in range(n-1):

		file_name="Data/assembly_words_"+str(i+1)

		try:
			f=open(file_name, 'r')

			with f:
				for line in f:
					if line.strip()==dow[:(4*i+3)]:

						return False

		except OSError:
			print ("Could not open/read file:", file_name)

	return True	

# print(isWeaklyIrreducible('1 2 2 1')) # True
# print(isWeaklyIrreducible('1 1 2 2')) # False
# print(isWeaklyIrreducible('1 2 1 2')) # True
# print(isWeaklyIrreducible('1 2 3 1 2 3 4 4')) # False 



# def isStrictlyIrreducible(dow): #checks if s.i. given that it is w.i. already (doen't check subwords starting with 1)

# 	n=getSize(dow)
# 	my_list=[]

# 	def inBetween(number_list):

# 		for i in number_list:
# 			counter=dow.find(str(i))+2

# 			while dow[counter]!=number_list[i] and counter<len(dow):
# 				if not (dow[counter] in number_list):
# 					my_list=my_list.append(dow[counter])
# 				counter+=2

# 	for i in range(n):
# 		if i in

# 	my_list=my_list.append(inBetween(my_list))

# 	for i in range(n):


def getAssemblyNumber(dow):



	for i in range(2,4):

		file_name="Data/An"+str(i)


		try:
			f=open(file_name, 'r')

			with f:
				for line in f:
					if line.strip()==dow:
						return i


		except OSError:
			print ("Could not open/read file:", file_name)

	return 1


# print(getAssemblyNumber('1 2 2 1')) # 1
# print(getAssemblyNumber('1 2 3 1 2 3 4 4')) # 1 
# print(getAssemblyNumber('1 1 2 3 3 2 4 4')) # 2
# print(getAssemblyNumber('1 1 2 3 3 2 4 4 5 6 6 5 7 7')) # 3


