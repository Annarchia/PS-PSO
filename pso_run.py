import os
import numpy as np
import matplotlib.pyplot as plt
import cv2

from pso import PSO
from utils import plot_pso, make_gif_from_folder, fitness

### User-set inputs

img = "input_images/fratty.png"
p_per_side = 10  # swarm size = p_per_side**2
inertia = .4
cognitive = 1.5
attractive = .5
repel_centre = 3
repel_neigh = 4
max_generations = 200
fitness_weight = .4

# Image processing
image = cv2.imread(img,0)
image = cv2.resize(image, dsize=(256,256), interpolation=cv2.INTER_CUBIC)
image = cv2.GaussianBlur(image, ksize=(9,9), sigmaX=5, sigmaY=5)
image = cv2.flip(image,0)
X = np.arange(image.shape[0])
Y = np.arange(image.shape[1])
meshgrid = np.meshgrid(X,Y)

# Create swarm
offset = 0.5
n_particles = p_per_side**2
X_coords, Y_coords = np.meshgrid(
                        np.arange(start=offset, stop=np.sqrt(n_particles)+offset),
                        np.arange(start=offset, stop=np.sqrt(n_particles)+offset)
                    )

swarm = np.vstack([X_coords.ravel(), Y_coords.ravel()]).swapaxes(0, 1)
swarm *= (image.shape[0] // np.sqrt(n_particles)-offset)
v = (np.random.random((n_particles, 2))- .5) / 10

pso = PSO(
    swarm.copy(),
    v.copy(), 
    fitness, 
    w = inertia, 
    c1 = cognitive, 
    c2 = attractive, 
    c3 = repel_centre, 
    c4 = repel_neigh, 
    max_g = max_generations,
    auto_coefs = True, 
    distancing = True, 
    fit_weight = fitness_weight, 
    landscape = image)

root = 'gifs/'
filename = 'gif_dark.gif'
save = True

if save:
    tmp_dir = os.path.join(root, 'gif_dark')
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)

while pso.next():
    fig = plt.figure()
    save_path = None if not save else os.path.join(tmp_dir, f'{pso.iter:05d}.png')

    ax = fig.add_subplot(1, 1, 1)
    plot_pso(meshgrid, image, pso.swarm, pso.v, ax=ax)
    ax.set_title(str(pso))
        
    if save_path is None:
        plt.show()
    else:
        plt.savefig(save_path)
    plt.close()

if save:
    make_gif_from_folder(tmp_dir, os.path.join(root, filename))
    # Save best swarm
    with open("gifs/swarm.txt", "w") as f:
        for particle in pso.best_swarm:
            str_line = str(particle)
            f.write(str_line + "\n")

    x = [p[0] for p in pso.best_swarm]
    y = [p[1] for p in pso.best_swarm]
    
    plt.plot(np.array(y),np.array(x),'o', color = "green")
    plt.xlim(0,image.shape[0])
    plt.ylim(0,image.shape[1])
    plt.show()