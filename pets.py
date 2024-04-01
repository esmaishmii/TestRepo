import matplotlib.pyplot as plt 
import csv
#napravite csv fajl 
f = open('pets.csv')
sadrzaj=csv.DictReader(f)
data=next(sadrzaj)
print(data)

pets=list(data.keys())
num_pets=[row for row in data.values()]
plt.pie(num_pets,labels=pets)
plt.savefig('pie.png')