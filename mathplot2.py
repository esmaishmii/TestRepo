import matplotlib.pyplot as plt 
#bar chart
labeles=['A','B','C']
values=[1,2,6]
bars=plt.bar(labeles,values)
bars[0].set_hatch('/')
bars[1].set_hatch('o')
plt.savefig('barchart.png')
