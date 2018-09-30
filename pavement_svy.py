import os 
import numpy as np
import pandas as pd
import csv
from datetime import datetime
import math
import random
from itertools import compress

path = 'C:/Users/Declan/Desktop/Python/Pavement/Sample_files'
os.chdir(path)
cwd = os.getcwd()
print(cwd)
files = os.listdir(path)
print(files)

# list index locaiton of files with the correct extension .3L0
T_F = list()
for n in files:
	x = '.3L0' in n
	T_F.append(x)

# loop through list of files with index of correct files (T_F).
# file_list are all the files we will work with
file_list = list(compress(files, T_F))

# there may be some survey files in the list that are measuring other data
# we only want the files that start with 'chain' in the datatable.
# T_F will be overwritten with a list of lines of text from the files

T_F = list()
list_of_files = list()
for idx, n in enumerate(file_list):
	with open(n) as f:
		lines = list(f)
		if any('Chain' in t for t in lines):
			list_of_files.append(lines)
			T_F.append(idx)
		else:
			pass


pavement_data = dict()
for idx, val in enumerate(list_of_files):
	d = list()
	# load the metadata at the top of each file.
	# if ':' is not in the string stop reading the lines
	# d will be a list of meta data lines stripped from the top of each file
	for a in val:
		if ':' not in a:
			pass
		else:
			c = a.split(':')
			meta = list()
			for v in c:
				x = '_'.join(v.split())
				meta.append(x)
			d.append(meta)

	# read the dataframe in each survey file.
	# convert two lists into a dictionary.
	# meta data from above is now in dict format.
	# the datatable in each file can be read in pandas format.
	# the number of lines in the metadata will indicate where to start reading the table
	# NOTE: there are 3 lines between the end of the metadata and the start of the table.
	## this may be unstable.
	# the datatable will be stored with the key DATA.
	b = dict()
	for no, x in enumerate(d):
		i = iter(x)
		f = dict(zip(i,i))
		b.update(f)
		b['Data'] = pd.read_csv(open(file_list[T_F[idx]]), skiprows = len(d)+3, sep = '\t')
	
	pavement_data[file_list[T_F[idx]]] = b

# add survey file name as a column/key to each dataframe.
for key, value in pavement_data.items():
	value['Data']['Survey'] = key

# check the column names
pavement_data['8880290M.3L0']['Data'].columns

# join all the tables into one.
appended_data = []
for key, value in pavement_data.items():
	# get the data values for each dictionary.
	dat = value['Data']
	dat.columns = col
	appended_data.append(dat)
appended_data = pd.concat(appended_data)


appended_data.to_csv('test.csv')

