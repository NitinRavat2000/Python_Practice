import time
print("Practical-7")
print("Enrollment no.=180130107086\n", "Time: ", time.ctime())
INF = 100000
def min(x, y):
  if x < y:
    return x
  return y

#k is number of denominations of the coin or length of d
def coin_change(d, n, k):
  M = [0]*(n+1)

  for j in range(1, n+1):
    minimum = INF

    for i in range(1, k+1):
      if(j >= d[i]):
        minimum = min(minimum, 1+M[j-d[i]])
    M[j] = minimum
  return M[n]

if __name__ == '__main__':
  # array starting from 1, element at index 0 is fake
  d = [1, 2, 5, 7]
  print("coins :",coin_change(d, 12, 3)) #to make 5. Number of denominations = 3



