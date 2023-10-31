import os
import numpy as np
import matplotlib.pyplot as plt
import cv2
from torch import meshgrid
from pso import PSO
from utils import fitness

n_particles = 20**2
n_swarms = 3
best_swarms = []

# Image processing
# img = "dog.jpg"
img = "input_images/fratty.png"
#img = "flower.jpg"
img = cv2.imread(img,1)
img = cv2.resize(img, dsize=(256,256), interpolation=cv2.INTER_CUBIC)
img = cv2.GaussianBlur(img, ksize=(9,9), sigmaX=5, sigmaY=5)
X = np.arange(img.shape[0])
Y = np.arange(img.shape[1])
meshgrid = np.meshgrid(X,Y)
plt.xlim(0,img.shape[0])
plt.ylim(0,img.shape[1])

for i in np.arange(n_swarms):
    image = img[:,:,i]

    # Create swarm
    offset = 0.5
    X_coords, Y_coords = np.meshgrid(
                            np.arange(start=offset, stop=np.sqrt(n_particles)+offset),
                            np.arange(start=offset, stop=np.sqrt(n_particles)+offset)
                        )

    swarm = np.vstack([X_coords.ravel(), Y_coords.ravel()]).swapaxes(0, 1)
    swarm *= (image.shape[0] // np.sqrt(n_particles)-offset)
    v = (np.random.random((n_particles, 2))- .5) / 10

    pso = PSO(swarm.copy(), v.copy(), fitness, w=.5, c1=1, c2=.5, c3=6, c4=6, max_g = 100, max_g_no_improvement=100,
    auto_coefs=True, distancing = True, fit_weight=1, landscape=image)
    
    while pso.next():
        continue

    # Save best swarm
    best_swarms.append(np.array(pso.best_swarm))
    colors = ["red","green","blue"]

#os.remove("best_swarm/colours.npy")
np.save("best_swarm/colours.npy", np.asarray(best_swarms))