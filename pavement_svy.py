import os 
import numpy as np
import pandas as pd
import csv
from datetime import datetime
import math
import random
from itertools import compress

path = 'C:/Users/Declan/Desktop/Python/Pavement'
os.chdir(path)
cwd = os.getcwd()
print(cwd)
files = os.listdir(path)
print(files)


T_F = list()
for n in files:
	x = '.3L0' in n
	T_F.append(x)

file_list = list(compress(files, T_F))

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
	for a in val:
		if ':' not in a:
			pass
		else:
			c = a.split(':')
			meta = list()
			for v in c:
				x = '_'.join(v.split())
				c_b.append(x)
			d.append(c_b)

	txt = open(file_list[idx])

	b = dict()
	for no, x in enumerate(d):
		i = iter(x)
		f = dict(zip(i,i))
		b.update(f)
		b['Data'] = pd.read_csv(open(file_list[T_F[idx]]), skiprows = len(d)+3, sep = '\t')
	
	pavement_data[file_list[T_F[idx]]] = b


for key, value in pavement_data.items():
	value['Data']['Survey'] = key

col = pavement_data['8880290M.3L0']['Data'].columns

appended_data = []
for key, value in pavement_data.items():
	dat = value['Data']
	dat.columns = col
	appended_data.append(dat)
appended_data = pd.concat(appended_data)

appended_data.to_csv('test.csv')

