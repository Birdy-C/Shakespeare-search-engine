#-*- coding:utf-8 -*-
'''
@author birdy qian
'''
import sys
from nltk import *																							#import natural-language-toolkit
from operator import itemgetter																	#for sort

def output_count(fdist):																				#output the relative information
	#vocabulary =fdist.items()
	vocabulary =fdist.items()																			#get all the vocabulary 

	
	vocabulary=sorted(vocabulary, key=itemgetter(1),reverse=True)				#sort the vocabulary in decreasing order
	print vocabulary[:250]																				#print top 250 vocabulary and its count on the screen
	print 'drawing plot.....'																				#show process
	fdist.plot(120 , cumulative=False)																#print the plot

	#output in file
	file_object = open('thefile.txt', 'w')																#prepare the file for writing
	for j in vocabulary:
		file_object.write( j[0] + ' ')																		#put put all the vocabulary in decreasing order 
	file_object.close( )																						#close the file
	

def pre_file(filename): 
	print("read file %s.txt....."%filename) 															#show process
	content = open( str(filename) + '.txt', "r").read()
	content = content.lower()
	for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_бо{|}~' :											#cancel the punction
		content = content.replace(ch, " ")

	plurals = content.split()																				#split the file at '\n' or ' '

	stemmer = PorterStemmer()																		#prepare for stemming
	singles = [stemmer.stem(plural) for plural in plurals]									#handling stemming

	return singles



#main function
def main(): 
	print "read index....."																					#show process
	input = open('index.txt', 'r')																		#titles that need to be handled
	all_the_file =input.read( )
	file=all_the_file.split()																					#split the file at '\n' or ' '
	input.close()																								#close the file
	fdist1=FreqDist()																						#create a new dist
	
	for x in range( 0, len(file) ):
		#print file[x]
		txt = pre_file( file[x] )																					#pre handing the txt

		for words in txt :
			words =words.decode('utf-8').encode(sys.getfilesystemencoding())		#change string typt from utf-8 to gbk
			fdist1[words] +=1																					#add it to the dist
		

	
	output_count(fdist1)
	

		
#runfile
if __name__ == '__main__': 
    main() 