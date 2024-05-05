def caching_fibonacci():
  cache_results = {}

  def fibonacci(n):
    if n <= 0:
      return 0
    
    if n == 1:
      return 1
    
    if n in cache_results:
      print(f"Cache hit! Cache n = {n}")
      return cache_results[n]
    
    cache_results[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return cache_results[n]
  
  return fibonacci

fibonacci = caching_fibonacci()

result1 = fibonacci(10)
result2 = fibonacci(15)


print(result1, result2)