# -*- coding: utf-8 -*-
"""
Created on Tue May  5 18:13:17 2020

@author: Ashutosh Sharma
"""
import matplotlib.pyplot as plt
import numpy as np

fhandle=open("Bat-SARS.fasta")
fread=fhandle.read()
seq="".join(fread.split())

def countKmers(seq,k):
    kFreq={}
    for i in range(0,len(seq)-k+1):
        kmer=seq[i:i+k]
        #kFreq[kmer]=dict.get(kmer,0)+1
        
        if kmer in kFreq:
            kFreq[kmer]+=1
        else:
            kFreq[kmer]=1
            
    return kFreq

rf=countKmers(seq,3)
#print(len(rf))

trimers = ["AAA", "AAC" ,"AAG" ,"AAT" ,"ACA" ,
           "ACC" ,"ACG" ,"ACT" ,"AGA" ,"AGC" ,
           "AGG" ,"ATA" ,"ATC","ATG","CAA","CAC",
           "CAG","CCA","CCC","CCG","CGA","CGC",
           "CTA","CTC","GAA","GAC","GCA","GCC",
           "GGA","GTA","TAA","TCA"]
newd={}
for trimer in trimers:
    newd[trimer]=rf[trimer]
#print(newd)

No_of_kMers=len(seq)-3+1
Ncount=[x/No_of_kMers for x in newd.values()]
#print(Ncount)

plt.figure(figsize=(40,20))
plt.plot(trimers,Ncount,linewidth=5.0,color='blue')
plt.ylabel("Normalised frequency",fontsize=46,color='blue')
#plt.yticks(np.arange(0,0.07,0.01))
plt.xlabel("Trinucleotides",fontsize=46)
plt.xticks(rotation=60,fontsize=40)
plt.grid(True)
plt.savefig('Bat-SARS_trimes.png',format="png",bbox_inches='tight')
plt.show()
plt.draw()



