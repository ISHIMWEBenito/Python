import os

current_directory = os.getcwd()
print(current_directory)
#folder_path = 'C:\Users\Windows10\Documents\GitHub-directory'
#result = os.listdir(folder_path)
#print(result)
os.mkdir('Tits')
os.rename('test', 'new test')
os.rename('test', 'C:\Users\Windows10\Documents\test')
os.listdir()
>>> ['new_one', 'old.txt']
>>> os.listdir()
['new_one', 'old.txt']

>>> os.remove('old.txt')
>>> os.listdir()
['new_one']

>>> os.rmdir('new_one')
>>> os.listdir()
[]

import shutil

shutil.rmtree('tree')