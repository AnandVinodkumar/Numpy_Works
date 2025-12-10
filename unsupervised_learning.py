"""
Unsupervised Learning
------------------------------------

Clustering
-----------------------
Here the models are trained with only input data
We need to generate the output by dividinng the input data which is called clustering
Clustering mainly used in marketing segmentation

items = ['apple','cat',orange','dog','grape','deer']

clusters
===============
animals  ['cat','dog','deer']
fruits   ['apple','orange','grape']


clustering   >>>   k-means
                   hierarchical

"""

# Steps for k-means
"""
1) Initialize the no of clusters
    if k = 2, we need 2 clusters from the input features
2) Select cenntroid values
3) Calculate the distance between the centroid and all points
4) Assign each point to the nearest centroid
    After calculation, each point selects the closest centroid
5) Recalculate the centroid
    new_centroid = mean of all points in the cluster
6) Repeat the steps until a new centroid is not created again
7) Finally divide the input labels into 2 clusters
8) Prediction
"""