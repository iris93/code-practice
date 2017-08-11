# -*- coding: utf-8 -*-
import sys
from numpy import *

try:
    file=open("../data/genotype_change.dat","r")
except IOError:
    print >> sys.stderr, "File could not be opened"
    sys.exit(1)

records_lines=file.readlines()
# data_length = len(records_lines)
# print records_lines[1]
data_length = len(records_lines)       #总的数据长度，即样本数
data_rows = 16          #单个数据行数，即基因编码后的种类数
data_cols = 9445        #单个数据列数，总研究的位点数
# data_cols = 4
       

data_dir = '../data/testdata/'
locas = records_lines[0].strip().split(' ')  #读取位点
save(data_dir+'locas',asarray(locas))
locas = load(data_dir+'locas.npy')

locas_out = []
locas_out1=[]
def safe_int(num):
    try:
        return int(num)
    except ValueError:
        result = []
        for c in num:
            if not ('0' <= c <= '9'):
                break
            result.append(c)
        if len(result) == 0:
            return 0
        return int(''.join(result))
temp = data_rows*data_cols
# fl=open('locas_out.txt', 'w')
for i in range(1,data_length):
    lineArr = records_lines[i].strip().split(' ')
    print i
    geno_coded = zeros([data_rows,data_cols]) #用16×9445的数组来表示一个编码后的基因
    geno_coded1 = zeros(data_cols)
    for j in range(0,data_cols):
        geno = safe_int(lineArr[j])
        geno_coded[geno-1][j] = 1
        geno_coded1[j] = geno
    # geno_temp = geno_coded.reshape(temp)
    print 'geno_coded',i+1
    print geno_coded
    # locas_out.append(geno_temp)
    locas_out.append(geno_coded)
    locas_out1.append(geno_coded1)

    # write data

# fl.write(str(locas_out))


save(data_dir+'locas_out',asarray(locas_out))
genos = load(data_dir+'locas_out.npy')
print  genos

save(data_dir+'locas_out1',asarray(locas_out1))
genos1 = load(data_dir+'locas_out1.npy')
print len(genos1)

# read multi_phenos

multi_phenos = [[],[],[],[],[],[],[],[],[],[],[]]
try:
    file=open("../data/phenotype.txt","r")
except IOError:
    print >> sys.stderr, "File could not be opened"
    sys.exit(1)
records_lines=file.readlines()
for item in records_lines:
    item = item.split('\n')
    multi_phenos[0].append(int(item[0]))

try:
    file=open("../data/multi_phenos.txt","r")
except IOError:
    print >> sys.stderr, "File could not be opened"
    sys.exit(1)
records_lines=file.readlines()
for item in records_lines:
    item = item.split('\n')
    # print len(item)
    item = item[0].split(' ')
    for i in range(1,len(multi_phenos)):
        multi_phenos[i].append(int(item[i-1]))

save(data_dir+'multi_phenos0-10',asarray(multi_phenos))
multi_phenos = load(data_dir+'multi_phenos0-10.npy')