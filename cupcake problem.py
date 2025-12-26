#  you are given an array A of size N, where each element respresent the number of cupcakes sold in as in single transcation.your task is to find and return an integer value respresenting the sum of the sum of the cupcakes from the transactions where 5 for or more cupcakes were sold. return 0 if there is no transactions with more than 5 cupcakes sold?
def cupcakes(n,arr):
  sum=0
  for i in range(n):
    if arr[i]>=5:
      sum+=arr[i]
  print(sum)
n=5
arr=[1,2,5,3,8,7]
cupcakes(n,arr)
