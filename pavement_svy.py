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
		if any ('Seconds' in t for t in lines):
			pass
		else:
			list_of_files.append(lines)
			T_F.append(idx)

pavement_data = dict()
for idx, val in enumerate(list_of_files):
	d = list()
	for a in val:
		if ':' not in a:
			pass
		else:
			c = a.split(':')
			c_b = list()
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



f = pd.DataFrame(b, index = [0])
f.to_csv('test.csv')

txt = open(file_list[idx])
pd.read_csv(txt, skiprows = len(d)+3, sep = '\t')