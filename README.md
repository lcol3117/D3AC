# D3AC
Delta Density Distance Agglomerative Clustering

# Use

`import D3AC`

`result=D3AC.cluster(data,w)`

*w is the only hyperparameter*

# Algorithm

At each point, increase the size of the circle around that point by w until this torus created by removing the circle of radius w-1 from one with radius w has a higher density than the previous one. 

Then, all circles that intersect are considered clusters. 
