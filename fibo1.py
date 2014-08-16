def fibo(n):
  if n == 0: return 0
  if n == 1: return 1
  else : result = fibo(n - 1) + fibo(n - 2)
  print("Вычислил для " + str(n) + "=" + str(result))
  return result
fibo(10)
