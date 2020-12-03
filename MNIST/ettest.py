import numpy as np
import matplotlib.pyplot as plt

x = np.array([[1,2,3],[6,5,4],[9,9,9]])
y = np.arange(10)
for i in range(x.shape[0]):
	param = 'HP' + str(i+1) 
	plt.plot(x[i],label = param)
plt.xticks(range(0,9))

plt.title('Accuracy plot of different parameters vs each fold(0-9)')
plt.xlabel('Folds')
plt.ylabel('Accuracy')
plt.legend()
plt.show()



# x = np.zeros((6000,28,28,1))
# y = np.ones((2,2,2,2))
# w = np.array([[0,0],[1,1]])



# a = np.array([[0,0,0],[1,1,1],[2,2,2]])

# b = np.array([[0,0],[1,1],[2,2]])

# s = np.arange(a.shape[0])
# np.random.shuffle(s)
# a = a[s]
# b = b[s]

# print(x.shape[0])
# print(b)