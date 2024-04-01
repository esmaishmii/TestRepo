import matplotlib.pyplot as plt
#linechart su za linije za funksije 
#kvadratna funkija 
x=[0,1,2,3,4]
y=[0,2,4,6,8]

plt.figure(figsize=(5,3))
plt.plot(x,y,label="2x",color='r',linewidth=1, linestyle='-',marker='*',markersize=10)
#color red isht r, linewidh dubljina linije,-- za prekidanu liniju , - za punu liniju , markeri su tacke u grafiku (*),marksize velicina tacke 
plt.title('Prva funksija', fontdict={'fontname':'Arial','fontsize':15})
plt.legend() # da bismo prikazali 2x odnosno koja funksija je to (label)

x2=[0,0.5,1,1.5,2,2.5,3,3.5,4,4.5]
y1=[elem**2 for elem in x2[:6]]
y2=[elem**2 for elem in x2[5:]]
""" y1=[]
for elem in x2[:6]:
    y1.append(elem**2)"""

plt.plot(x2[:6],y1, color='b',label='x^2')
plt.plot(x2[5:],y2,linestyle='--')
plt.xlabel('X osa ')
plt.ylabel('Y osa')

plt.savefig('funksija.png')
plt.show()