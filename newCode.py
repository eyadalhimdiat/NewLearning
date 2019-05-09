import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
from matplotlib import style
from collections import Counter

style.use('fivethirtyeight')

dataset = {'k':[[1,2],[2,3],[3,1]], 'r':[[6,5], [7,7],[8,6]]}

new_feature = [5,7] 

def k_nearest_neighbors(data, predict, k =3):
    if len(data) >= k:
        warnings.warn("K is less than data")
    distances = []
    for group in data:
        for features in data[group]:
            euclidean_distance = np.linalg.norm(np.array(features) - np.array(predict))
            print(euclidean_distance)
            print("11111111111111111111111111111111111")
            distances.append([euclidean_distance, group])
    
    votes = [i[1] for i in sorted(distances)[:k]]
    print(sorted(distances))
    print("neeeeeeeeeeeeeeeew")
    print(votes)
    print("222222222222222222222222222")
    print(Counter(votes).most_common(1))
    print("333333333333333333333333333333")
    vote_result = Counter(votes).most_common(1)[0][0]
    return vote_result  

result = k_nearest_neighbors(dataset, new_feature, k=3)       
print(result)
print("444444444444444444444444")
for i in dataset:
    for ii in dataset[i]:
        plt.scatter(ii[0], ii[1], s = 100, color = i)

plt.scatter(new_feature[0], new_feature[1], s = 100, color = "g")       
plt.show()          