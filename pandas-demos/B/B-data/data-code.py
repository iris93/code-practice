# -*- coding: utf-8 -*-
import numpy as np 
import pandas as pd 

genotype = pd.read_table('genotype.dat',sep ='\s*')
phenotype = pd.read_table('phenotype.txt',sep ='\s*',header = None,names=['phenotype'])
print len(genotype.columns)
# print genotype.ix[0]
# print genotype[0:1]

columns = genotype.columns
codes = []
def codesingle(strs):
	if str(strs) not in codes:
		print str(strs)
		codes.append(str(strs))
		return len(codes)-1
	else:return codes.index(strs)
#'''
# get gonotype_coded16
# for i in range(0,len(columns)):
# 	genotype[columns[i]]= genotype[columns[i]].apply(codesingle)
# print genotype[columns[0:3]]
# print codes
# genotype.to_csv('genotype_coded16.csv',index = False)
#'''

#'''
# get genotype_coded3
# for i in range(0,len(columns)):
# 	codes = []
# 	genotype[columns[i]]= genotype[columns[i]].apply(codesingle)
# 	print codes

# print codes
# print genotype[columns[0:3]]
# genotype.to_csv('genotype_coded3.csv',index = False)

#'''

genotype_coded3 = pd.read_csv('genotype_coded3.csv')
# print genotype_coded3['phenotype'][499]
# print genotype_coded3['phenotype'][500]
genotype_coded16 = pd.read_csv('genotype_coded16.csv')

# print phenotype['phenotype']



import matplotlib  
matplotlib.use('Agg') 
import matplotlib.pylab as plt
from matplotlib.pyplot import plot,savefig 

corr3_tmp = pd.Series()
corr3_tmp = genotype_coded3.corrwith(phenotype['phenotype'])
# corr3_inorder = np.sort(corr3)
# corr3_inorder = corr3_tmp.order()
corr3_inorder = corr3_tmp.sort_values()
print corr3_inorder

fig = plt.figure('corr3_inorder',figsize=(10,10))
ax = fig.add_subplot(111)
plt.title('corr3_inorder')
plt.plot(corr3_inorder,'*b', label='corr3_inorder')
plt.legend(bbox_to_anchor=(0.7, 1.01), loc=3, borderaxespad=0.)
leg = plt.gca().get_legend()
ltext  = leg.get_texts()
plt.setp(ltext, fontsize='small')
savefig('corr3_inorder.jpg') 

corr16_tmp = pd.DataFrame([],columns = ['corr'])
corr16_tmp['corr'] = genotype_coded16.corrwith(phenotype['phenotype'])
corr16_inorder = corr16_tmp.sort_values(by = 'corr')
# print corr16_inorder
fig = plt.figure('corr16_inorder',figsize=(10,10))
ax = fig.add_subplot(111)
plt.title('corr16_inorder')
plt.plot(corr16_inorder,'*b', label='corr16_inorder')
plt.legend(bbox_to_anchor=(0.7, 1.01), loc=3, borderaxespad=0.)
leg = plt.gca().get_legend()
ltext  = leg.get_texts()
plt.setp(ltext, fontsize='small')
savefig('corr16_inorder.jpg') 