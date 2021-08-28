# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 21:05:18 2021

@author: yixing
"""




class ChkBloodType:
    def chkBlood(self, father, mother):
 
        sDict = {}
        sDict['OO'] = ['O']
        sDict['AO'] = ['A','O'] #double 
        sDict['OA'] = ['A','O'] #double 
        sDict['AA'] = ['A','O']
        sDict['AB'] = ['A','AB','B','O']
        sDict['BA'] = ['A','AB','B','O']
        sDict['AAB'] = ['A','AB','B']
        sDict['ABA'] = ['A','AB','B']
        sDict['BO'] = ['B','O']
        sDict['OB'] = ['B','O']
        sDict['BB'] = ['B','O']
        sDict['BAB'] = ['A','AB','B']
        sDict['ABB'] = ['A','AB','B']
        sDict['ABO'] = ['A','B']
        sDict['OAB'] = ['A','B']
        sDict['ABAB'] = ['A','AB','B']
 
        return sDict.get(father+mother)
    
print(ChkBloodType().chkBlood('A','A'))