import pandas as pd
df=pd.read_csv('dbdump.csv')
print(df['IP'])
df2=df['ID'].describe()
print(df2)
df3=df['IP'].describe()
print(df3)
df4=df.describe()
print(df4)
df5=df['ID'].mean()
print(df5)
df6=df.head(5)
print(df6)
df7=df.tail(5)
print(df7)
df8=df['PICS'].value_counts()
print(df8)
import matplotlib.pyplot as plt
#plt.plot(df8)
#plt.ylabel('Count')
#plt.xlabel('Images')
#plt.show()

df8.plot.bar()
#plt.show()
plt.savefig('mygraph.png',bbox_inches='tight')

writer=pd.ExcelWriter('Report.xlsx',engine='xlsxwriter')
df8.to_excel(writer,sheet_name='DATA')
wb=writer.book
ws=wb.add_worksheet('GRAPH')
ws.insert_image('B2','mygraph.png')
writer.close()

df9=df[df['ID']>10]
print(df9)
df10=df[df['PICS'].str.endswith('jpg')]
print(df10)

df11=df.groupby(['PICS']).count()
print(df11)

#SLICING
df12=df.iloc[1,1]#(1,1) cell
df13=df.iloc[1]#row 1
df14=df.iloc[:,1]#first column
df15=df.iloc[1:10:2]#rows 1 to 9 step by 2
df16=df.iloc[:,0:5:2]#col 0 to 5 step by 2
df17=df.iloc[5:10,1:4]#in between
df18=df.iloc[[1,4,7]]# row 1,4,7
df19=df.iloc[[1,4,7],[1,3]]
