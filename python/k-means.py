import numpy as np
from sklearn.cluster import KMeans

if __name__=='__main__':
    data.cityNmae = loadData('city.txt')
    km = KMeans(n_cluster=3)
    label = km.fit_predict(data)
    expenses = np.sum(km.cluster_centers_axis=1)
    #print(expenses)
    CityCluster = [[],[],[]]
   for i in range(len(cityName[i])):
        CityCluster(label[i].append(cityName[i]))
    
