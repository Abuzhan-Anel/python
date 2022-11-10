import numpy as np

arr = [
  [1, 2, 3, 7 ],
  [4, 5, 6, 15],
  [7, 8, 9, 24],
  [12,15,18,45]
]



a1= np.sum(arr, axis = 1)
a2 = np.sum(arr, axis = 0)
l=[]
for i in range(len(a1)):
  for j in range(len(a2)):
    if a1[i] != (arr[i][len(a1)-1])*2 and a2[j] !=(arr[len(a1)-1][j])*2:
      qqq= a1[i]- (arr[i][len(a1)- 1])*2
      print(arr[i][j],i,j)
      if i == len(a1)-1 or j == len(a2) - 1:
        arr[i][j]= arr[i][j]+ qqq
      else:
        arr[i][j]= arr[i][j] - qqq