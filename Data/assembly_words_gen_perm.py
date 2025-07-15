
import os
import itertools
import dow_operations 


os.system('cls')


if __name__ == "__main__":

	#____________Size input with Error Detection______________________

	check=False
	max_num=7

	while check==False:

		try:
			n=input("What size assembly words do you want to produce?")
			
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


	#____________Create new file to store the words______________________


	newFileName="assembly_words_"+str(n)

	os.system('cls')
	print("Creating new file: ", newFileName)
	f=open(newFileName,"w")


	#____________Creating list of generators from the set [2n-1]*...*[3]*[1]______________________

	word_iterator= [1]

	for i in range(1,n):
		print(word_iterator)
		word_iterator=list(itertools.product(word_iterator,range(1,2*i+2)))
		print(word_iterator)
		for j in range(len(word_iterator)):
			word_iterator[j]=' '.join(str(t) for t in word_iterator[j])


	print (list(word_iterator))

	for i in range(len(word_iterator)):
		word_iterator[i]=tuple(int(x) for x in word_iterator[i].split())

	print()
	print('Final list of generators:',word_iterator)



	# ____________(w/o reversal) Creating list of assembly words from generators______________________


	assembly_words=[] 						#stores list of words
	dow_constructor=[None]*(2*n) 			#stores a single word generated
	dow=""
	number_of_assembly_words=0 				#talies up total number of words stored


	for generator in word_iterator:

		for i in range(n):
			for j in range(2*n):
				if dow_constructor[j] == None:
					dow_constructor[j]=str(i+1) #place next letter in first open spot
					break
				else: 
					continue

	#___place the same letter as dictated by the generator
			space_counter=int(generator[n-1-i]) #cuz generators are reversed
			for j in range(i+1,2*n):
				if dow_constructor[j] == None:
					if space_counter==1:
						dow_constructor[j]=str(i+1)
						break
					else:
						space_counter-=1
				else:
					continue

		dow=" ".join(str(t) for t in dow_constructor)
		dow_constructor=[None]*(2*n)


	#___check is the reverse of dow already exists in the file

		check=False
		rev=dow_operations.reverse(dow)
		# print()
		# print('Reverse:',rev)

		for word in assembly_words:
			if word == rev :
				check=True
				break
			else: 
				continue


	#___if the word is new, then it is saved in the file

		if check==False:
			assembly_words.append(str(dow))
			f.write(dow+"\n")
			#print("New word", dow,"was added.")
			number_of_assembly_words+=1

		# else: 
			#print("The word", dow, "already existed.")


	print()
	print()
	print("There is a total of", number_of_assembly_words, "assembly words of size", n)


	f.close()


