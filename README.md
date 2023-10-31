# PS-PSO: Paul Signac Particle Swarm Optimisation

Particle Swarm Optimisation (PSO) is a heuristic optimisation algorithm inspired by flocks of birds or swarms of insects. It is a population based scheme in which a swarm of possible solutions is updated in search of the *best* set of solutions.

PS-PSO implements a standard PSO algorithm, with some inspiration to the Social Force Model, defined on a continuous cost function derived from an image.

### Class Definition

The class ``PSO`` (``pso.py``) defines and implements the PSO algorithm. At any time, each particle in a swarm is defines by a vector $(x, v, f(x))$ where:

- $x$ is the particle position
- $v$ is the particle velocity
- $f(x)$ is the value of the cost (fitness) function at position $x$

A particle perceives performance and position of its neighbours and remembers its own position where it obtained the best performance. PS-PSO employs a circular list-based neighbourhood, i.e. the particle with index $i$ sees as neighbours particles $i-1$ and $i+1$.

### Getting creative with Processing

In order to run the .pyde files contained in the processing folder you should keep unvaried the names of the folder which contains them (bew_circles and coloured_circles). You should make sure to download Processing and use the Python module. Once you have the environment set, you can open the file and run the script.