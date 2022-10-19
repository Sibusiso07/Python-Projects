# Imports that I needed for the code.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pyexpat import features
from sklearn.decomposition import PCA
from IPython.display import clear_output

# Asking the user to choose a file they wish to use
dataSet1 = input('''Plese enter the file name you want to use: 
                    data1953
                    data2008
                    dataBoth \n''' ) 

# Using the if statement to read the data from the file the user selected and avoid the program from chashing by inputting unavailable option
if dataSet1 == "data1953":
    united_nations = pd.read_csv("data1953.csv")
elif dataSet1 == "data2008":
    united_nations = pd.read_csv("data2008.csv")
elif dataSet1 == "dataBoth":
    united_nations = pd.read_csv("dataBoth.csv")
else:
    print("Invalid choice, there is no file with such a name!")

# Selecting the features we will use in the program & Dropping all rows will a null value
features = ["BirthRate", "LifeExpectancy"]
united_nations = united_nations.dropna(subset=features)

# Coping the data to a new data frame that we will be using in the program
data = united_nations[features].copy()

# A function used to Create random centroids
def random_centroids(data, k):
    centroids = []
    for i in range(k):
        centroid = data.apply(lambda x: float(x.sample()))
        centroids.append(centroid)
    return pd.concat(centroids, axis=1)

# A function used to Label each data point based on the distance to each centroid
def get_label(data, centroids):
    distance = centroids.apply(lambda x: np.sqrt(((data-x)**2).sum(axis=1)))
    return distance.idxmin(axis=1)

# A function used to update the centroids with new data
def new_centroids(data, labels, k):
    return data.groupby(labels).apply(lambda x: np.exp(np.log(x).mean())).T

# Plotting the data
def plot_clusters(data, labels, centroids, iteration):
    pca = PCA(n_components=2)
    data_2d = pca.fit_transform(data)
    centroids_2d = pca.transform(centroids.T)
    clear_output(wait=True)
    plt.title(f'Iteration{iteration}')
    plt.scatter(x=data_2d[:,0], y=data_2d[:,1], c=labels, alpha=0.2)
    plt.scatter(x=centroids_2d[:,0], y=centroids_2d[:,1], marker="*", color='black')
    plt.show()

# The user will enter the max number of iterations the program can go through and the number of clusters the program will have
max_iterations = int(input("Please enter the number of maximum iterations that the program can go through: "))
k = int(input("Please enter the number of clusters: "))

# Creating variables the hold the data that is created by the functions and inserted as default in the program
centroids = random_centroids(data, k)
labels = get_label(data, centroids)
old_centroids = pd.DataFrame()
iteration = 1

# while loop used to to display the plotted data while going through the iretaration
while iteration < max_iterations and not centroids.equals(old_centroids):
    old_centroids = centroids
    
    labels = get_label(data, centroids)
    centroids = new_centroids(data, labels, k)
    plot_clusters(data, labels, centroids, iteration)
    iteration += 1

# Prints the number of how many countries are in each cluster
print("Number of Countries per cluster")
print(labels.value_counts())

# Printing the names of the countries in each cluster
i = 0
cluster = 0
while i < k:
    print("\nCountry name in cluster " + str(cluster))
    print(united_nations[labels==cluster]["Countries"])
    cluster += 1
    i += 1

# Prints the geometric mean of the BirthRate & LifeExpectancy of each cluster
print("\nMean for BirthRate & LifeExpectancy in each cluster: ")
print(new_centroids(data, labels, k))


# STEPS I USED WHEN APPROACHING THE PROGRAM
# Step 1: Read through the data in the files
# Step 2: Select features that I can used from the data in the file & Drop all rows will a null value
# Step 3: Create a new data frame so to not confuse myself about which data am I using
# Step 4: Create centroids at random
# Step 5: Label the data points or find the distance between the data points and centroids
# Step 6: Plot the data

# Refence: 
# https://www.askpython.com/python/examples/k-means-clustering-from-scratch
# https://realpython.com/k-means-clustering-python/
# https://www.youtube.com/watch?v=Xvwt7y2jf5E&t=1674s
# https://www.youtube.com/watch?v=iNlZ3IU5Ffw&t=366s
# https://www.youtube.com/watch?v=lX-3nGHDhQg&t=2s
# https://www.youtube.com/watch?v=wt-X61BnUCA
# https://anderfernandez.com/en/blog/kmeans-algorithm-python/