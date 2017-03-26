#-*- coding:utf-8 -*-
'''
@author birdy qian
'''
import os 
import sys
import pprint, pickle
from nltk import PorterStemmer

def readfile(filename):
	input = open(filename, 'r')																	#titles that need to be handled
	all_the_file =input.read( )
	words = all_the_file.split()																		#split the file at '\n' or ' '
	input.close()																							#close the data
	return words

def getdata():
	pkl_file = open('data.pkl', 'rb')																#index is saved in the file 'data.pkl'
	data1 = pickle.load(pkl_file)																	#change the type
	#pprint.pprint(data1)
	pkl_file.close()																						#close the file
	return  data1																						#close the data

def output( result ):
	#print result
	if result == None:												#if the words is not in the index (one word return None)
		print None
		return
	if len(result) == 0 :											#if the words is not in the index (more than one words return [] )
		print None
		return 

	if len(result) < 10 :												#if the records is less than 10
		print result

	else:																	#if the records is more than 10
		print 'get '+ str(len(result)) + ' records'																			#the record number
		for i in range( 0 , len(result) / 10 +1):
			print '10 records start from ' +str(i*10+1)

			if 10 * i + 9 < len(result) :																							#print from 10 * i to 10 * i + 10
				print result[ 10 * i : 10 * i + 10 ]
			else:																															#print from 10 * i to end
				print result[ 10 * i :  len(result) ]
				break
			getstr = raw_input("Enter 'N' for next ten records & other input to quit : ")
			if getstr != 'N':
				break



#main function
def main(): 
	data_list = getdata()																									#read data																	
	STOPWORDS = readfile('stop_word.txt') 
	stemmer = PorterStemmer()																						#prepare for stemming

	while True:
		get_str = raw_input("Enter your query('\\'to quit): ")
		if get_str == '\\' : 																									#leave the loop
			break

		get_str = get_str.lower()
		for ch in  STOPWORDS:																							#cancel the stopwords
			get_str = get_str.replace(ch, " ")	
		query_list=get_str.split()																							#split the file at '\n' or ' '
		query_list = [stemmer.stem(plural) for plural in query_list]										#handling stemming


		while True:		
			if query_list != [] :
				break
			get_str = raw_input("Please enter more information: ")
			get_str = get_str.lower()
			for ch in  STOPWORDS:																						#cancel the stopwords
				 get_str = get_str.replace(ch, " ")	
			query_list=get_str.split()
			query_list = [stemmer.stem(plural) for plural in query_list]									#handling stemming



		result=[]
		for k in range( 0 , len(query_list) ):	
			if k==0:																											#if the list has not been built 
				result = data_list.get( query_list[0] )
			else:																													#if the list has been built 
				result = list( set(result).intersection(data_list.get( query_list[k] ) ) )
		output( result )

	
#runfile
if __name__ == '__main__': 
    main() 