# -*- coding: utf-8 -*-
"""
Created on Tue May  5 19:14:01 2020

@author: Ashutosh Sharma
"""
import matplotlib.pyplot as plt
from Covid_19 import Ncount as nc0#sars-cov-2
from Sars_Cov import Ncount as nc1#sars-cov
from Bat_SARS_Cov import Ncount as nc2#bat-sars

trimers = ["AAA", "AAC" ,"AAG" ,"AAT" ,"ACA" ,
           "ACC" ,"ACG" ,"ACT" ,"AGA" ,"AGC" ,
           "AGG" ,"ATA" ,"ATC","ATG","CAA","CAC",
           "CAG","CCA","CCC","CCG","CGA","CGC",
           "CTA","CTC","GAA","GAC","GCA","GCC",
           "GGA","GTA","TAA","TCA"]

plt.figure(figsize=(40,20))
plt.plot(trimers,nc0,linewidth=5.0,color='red')
plt.plot(trimers,nc1,linewidth=5.0,color='green')
plt.plot(trimers,nc2,linewidth=5.0,color='blue')

plt.ylabel('Normalised frequency',fontsize=46)
plt.xlabel('Trinucleotides',fontsize=46)
plt.xticks(rotation=60,fontsize=40)
plt.grid(True)
plt.gca().legend(("Covid-19","SARS-CoV","BAT-SARS"),fontsize=40)
plt.savefig('combined.png',format='png',bbox_inches='tight')
plt.show()
plt.draw()