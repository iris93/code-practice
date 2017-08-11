import numpy as np 
import pandas as pd 

# csv_input = pd.read_csv('data.csv')
# print csv_input    

print '====================================  split line  ================================================='
frame = pd.DataFrame(np.arange(4).reshape(2,2))
print frame.to_html()

frame = pd.DataFrame(np.random.random((4,4)), index=['white', 'black', 'red','blue'],columns=['up', ' down','left', 'right'])
print frame

