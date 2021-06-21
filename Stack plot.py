import matplotlib.pyplot as plt

days = [1,2,3,4,5]

sleep = [6,7,5,8,6]
eat =   [2,2,1,2,1]
work =  [5,7,10,8,6]
exercise=  [3,3,0,1,3]


plt.plot([],[],color='green', label='sleep', linewidth=3)
plt.plot([],[],color='blue', label='eat', linewidth=3)
plt.plot([],[],color='red', label='work', linewidth=3)
plt.plot([],[],color='black', label='play', linewidth=3)

plt.stackplot(days, sleep, eat, work, exercise, colors=['green','blue','red','black'])

plt.xlabel('days')
plt.ylabel('activities')
plt.title('5 DAY ROUTINE')
plt.legend()
plt.show()