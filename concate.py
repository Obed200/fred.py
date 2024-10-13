# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 15:37:02 2024

@author: USER
"""

listed=["kamali",'ni','umucuruzi.']
print(listed)
new_listed=" ".join(listed)
print(new_listed)
new_listed=','.join(listed)
print(new_listed)
new_listed='-'.join(listed[1:])
print(new_listed)


print('-------------------string format with %s----------------------')
name='cohort' 
value='90%'

print('%s %s' %(name,value))