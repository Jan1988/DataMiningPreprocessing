import os
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

import numpy as np

from Obj_Movie_With_Genres import MovieWithGenres


if __name__ == '__main__':

    # Movies with Genres from CSV
    csv_file = os.path.join('Assets', 'MOVIELEGACYINFLATION_final.csv')
    e = open(csv_file, "r")
    e.readline()

    i = 0

    gross_values = []
    x_values = []

    for e_line in e:
        split_list = e_line.split(';')

        gross_values.append(int(split_list[3]))

        x_values.append(i)
        i += 1

    sorted_gross_values = sorted(gross_values, reverse=True)

    cluster_count = 5
    L = len(gross_values)
    cluster_size = int(L / cluster_count)

    cluster_thres_1 = round(sorted_gross_values[cluster_size],-6)
    cluster_thres_2 = round(sorted_gross_values[cluster_size*2],-6)
    cluster_thres_3 = round(sorted_gross_values[cluster_size*3],-6)
    cluster_thres_4 = round(sorted_gross_values[cluster_size*4],-6)
    cluster_thres_5 = round(sorted_gross_values[cluster_size*5],-6)

    print(str(cluster_thres_1) + ' - ' + str(cluster_thres_2) + ' - ' + str(cluster_thres_3) + ' - ' + str(cluster_thres_4) + ' - ' + str(cluster_thres_5))





    # n_samples = i
    # prep_data = np.column_stack((x_values, gross_values))
    #
    # k_means = KMeans(n_clusters=5).fit(prep_data)
    #
    # plt.scatter(x_values, gross_values, c=k_means.labels_)
    #
    # axes = plt.gca()
    # axes.set_xlim([0, 2600])
    # plt.show()



    # Write into .csv file
    gross_cluster = os.path.join('Assets', 'Gross_Cluster.csv')
    g = open(gross_cluster, 'w')
    g.write('Gross_Cluster\n')

    clusters = ['Flop', 'Low', 'Medium', 'High',  'Extreme']
    for gross in gross_values:

        if gross > cluster_thres_1:
            cluster_val = clusters[4]
        elif gross > cluster_thres_2:
            cluster_val = clusters[3]
        elif gross > cluster_thres_3:
            cluster_val = clusters[2]
        elif gross > cluster_thres_4:
            cluster_val = clusters[1]
        elif gross > cluster_thres_5:
            cluster_val = clusters[0]
        else:
            print('error - no cluster for: ' + str(gross))

        g.write(cluster_val + '\n')
    g.close()
    # j = 0

    # for gross in gross_values:
    #     cluster_val = clusters[k_means.labels_[j]]
    #
    #     g.write(cluster_val + '\n')
    #     j += 1
    # g.close()




