import csv,json
import pandas as pd
import numpy as np

# def foo_bar(x):
# 	return x.replace(' ','')
for i in range(32,43):
	try:
		df=pd.read_csv(str(i)+'.csv', encoding='ISO-8859-1')
		names=[]
		for name in list(df.columns.values):
			name=name.replace('\n','')
			name = " ".join(name.split())
			names.append(name)

		df.columns=names
		# sset=names[2]
		# df=df.dropna(subset=[sset])
		df.to_csv('l'+str(i)+'.csv', encoding='utf-8')
	except FileNotFoundError:
		print(i)
# for x in range(1,43):
# 	pass
# df = pd.read_csv('PC'+str(x)+'.csv',encoding="utf-8")
# col = df.columns.values
# for x in list(col):
# 	for y,a in zip(list(df[x]),range(0,len(list(df[x]))-1)):
# 		y = str(y)
# 		y = y.replace('\n','')
# 		y = y.replace('i','1').replace('S','5').replace('I','1').replace('!','1').replace(']','1').replace('l','1').replace('t','1').replace('J','3').replace('o','0').replace('O','0').replace('Q','0').replace('?','0').replace('.','').replace('\"','').replace('\'','').replace('T','7')
# 		y = " ".join(y.split())
# 		y = y.strip()
# 		try:
# 			df[x][a] = y
# 		except SettingWithCopyWarning:
# 			print(y)

# print()

# df.to_csv(str(x)+'.csv')

