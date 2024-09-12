import matplotlib.pyplot as plt
a = 1
c = 8
l = 8

xadrez = [[ [255*((i + j)%2), 255*((i + j)%2), 255*((i + j)%2)] for i in range(c)] for j in range(l)]

plt.imshow(xadrez)
plt.axis('off')
plt.show()