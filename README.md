# READ ME: Assembly Word Database

This package contains data generators and a database interface to filter the propeties of assembly words; a type of mathematcial object used to study the process of DNA sequence rearangement. See [here](https://www.google.com) for information on its mathematical definition, propeties and use in mathematical biology.

For now, it holds information on the properties of all assembly words of size at most 7. 

In short, *main.py* executes the database interface, where the input on the desired properties of assembly words is gathered and then the filtered set of words is displayed. The data used is retrieved from the Data folder included in the dowload, but if one wants to generate the data for themselves then: 
- *assembly_words__gen_perm.py:* generates all assembly words of a given size and stores them in a text file. Creates files by the name *"assembly_words_i"* for words of size i. 
- (*assembly_words__gen.py:* does the same but prints them to the command line instead.)
- *DOW.py:* computes and stores the properties of assembly graphs of a given size. The above data corresponding to the desried size must be generated first. It creates data files by the name *"assembly_word_properties_i"* for words of size i. 

## Dowload Information: 
For the correct functioning of interface and the data generators, **all files must be stored in the same directory when executed.** 
No extra libraries need to be installed, all packages are included in the core Python 3.13+ (latest version at the time). 
