import numpy as np
import statistics

quan =int(input("enter array quantity : "))
arr = np.random.randint(0,10,quan)
print(arr)
again_arr = np.array([],dtype=int)


for i in range(0,quan-1):
    for j in range(i+1,quan):
        if arr[i] == arr[j]:
            value = arr[i]
            again_arr = np.append(again_arr,value)
            value = 0



print(f"arr : {again_arr}")


most_again_arr = statistics.mode(again_arr)
print(f"most again arr : {most_again_arr}")







